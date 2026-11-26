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
#include <QtQml/QQmlListProperty>

//  const QMetaObject *QQuickCumulativeDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickCumulativeDirection10metaObjectEv(
    const QQuickCumulativeDirection *self) {
  return self->metaObject();
}

//  void *QQuickCumulativeDirection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickCumulativeDirection11qt_metacastEPKc(
    QQuickCumulativeDirection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickCumulativeDirection::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickCumulativeDirection11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickCumulativeDirection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QQuickDirection> QQuickCumulativeDirection::directions()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickDirection> *ritual_ZN25QQuickCumulativeDirection10directionsEv(
    QQuickCumulativeDirection *self) {
  return new QQmlListProperty<QQuickDirection>(self->directions());
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

//  a QQmlListProperty<QQuickDirection> a ritual of QQuickCumulativeDirection
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickCumulativeDirection__QQmlListProperty_QQuickDirection(
    QQmlListProperty<QQuickDirection> *self) {
  delete self;
}
