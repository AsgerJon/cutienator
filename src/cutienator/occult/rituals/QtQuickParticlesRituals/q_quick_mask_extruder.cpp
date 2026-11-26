//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickmaskextruder_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickmaskextruder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>

//  const QMetaObject *QQuickMaskExtruder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickMaskExtruder10metaObjectEv(
    const QQuickMaskExtruder *self) {
  return self->metaObject();
}

//  void *QQuickMaskExtruder::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickMaskExtruder11qt_metacastEPKc(
    QQuickMaskExtruder *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMaskExtruder::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickMaskExtruder11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMaskExtruder *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMaskExtruder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickMaskExtruder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMaskExtruder::tr(s, c, n));
}

//  QQuickMaskExtruder::QQuickMaskExtruder(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMaskExtruder *ritual_ZN18QQuickMaskExtruderC1EP7QObject(
    QObject *parent) {
  return new QQuickMaskExtruder(parent);
}

//  QPointF QQuickMaskExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN18QQuickMaskExtruder7extrudeERK6QRectF(
    QQuickMaskExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->extrude(*a0));
}

//  bool QQuickMaskExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickMaskExtruder8containsERK6QRectFRK7QPointF(
    QQuickMaskExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->contains(*bounds, *point);
}

//  QUrl QQuickMaskExtruder::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickMaskExtruder6sourceEv(
    const QQuickMaskExtruder *self) {
  return new QUrl(self->source());
}

//  void QQuickMaskExtruder::sourceChanged(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickMaskExtruder13sourceChangedERK4QUrl(
    QQuickMaskExtruder *self,
    const QUrl *arg) {
  self->sourceChanged(*arg);
}

//  void QQuickMaskExtruder::setSource(const QUrl &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickMaskExtruder9setSourceERK4QUrl(
    QQuickMaskExtruder *self,
    const QUrl *arg) {
  self->setSource(*arg);
}

//  void QQuickMaskExtruder::startMaskLoading()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickMaskExtruder16startMaskLoadingEv(
    QQuickMaskExtruder *self) {
  self->startMaskLoading();
}

//  void QQuickMaskExtruder::finishMaskLoading()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickMaskExtruder17finishMaskLoadingEv(
    QQuickMaskExtruder *self) {
  self->finishMaskLoading();
}

//  void QQuickMaskExtruder::ensureInitialized(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickMaskExtruder17ensureInitializedERK6QRectF(
    QQuickMaskExtruder *self,
    const QRectF *r) {
  self->ensureInitialized(*r);
}

//  QPointF QQuickMaskExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN18QQuickMaskExtruder7extrudeERK6QRectF(
    QQuickMaskExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->QQuickMaskExtruder::extrude(*a0));
}

//  bool QQuickMaskExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickMaskExtruder8containsERK6QRectFRK7QPointF(
    QQuickMaskExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->QQuickMaskExtruder::contains(*bounds, *point);
}
