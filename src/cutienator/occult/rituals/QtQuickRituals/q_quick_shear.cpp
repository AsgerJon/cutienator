//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QQuickShear::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickShear10metaObjectEv(
    const QQuickShear *self) {
  return self->metaObject();
}

//  QString QQuickShear::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickShear2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShear::tr(s, c, n));
}

//  QQuickShear::QQuickShear(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickShear *ritual_ZN11QQuickShearC1EP7QObject(QObject *parent) {
  return new QQuickShear(parent);
}

//  QVector3D QQuickShear::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuickShear6originEv(const QQuickShear *self) {
  return new QVector3D(self->origin());
}

//  void QQuickShear::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShear9setOriginERK9QVector3D(
    QQuickShear *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QQuickShear::xFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickShear7xFactorEv(const QQuickShear *self) {
  return self->xFactor();
}

//  void QQuickShear::setXFactor(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShear10setXFactorEd(QQuickShear *self, qreal a0) {
  self->setXFactor(a0);
}

//  qreal QQuickShear::yFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickShear7yFactorEv(const QQuickShear *self) {
  return self->yFactor();
}

//  void QQuickShear::setYFactor(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShear10setYFactorEd(QQuickShear *self, qreal a0) {
  self->setYFactor(a0);
}

//  qreal QQuickShear::xAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickShear6xAngleEv(const QQuickShear *self) {
  return self->xAngle();
}

//  void QQuickShear::setXAngle(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShear9setXAngleEd(QQuickShear *self, qreal a0) {
  self->setXAngle(a0);
}

//  qreal QQuickShear::yAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickShear6yAngleEv(const QQuickShear *self) {
  return self->yAngle();
}

//  void QQuickShear::setYAngle(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickShear9setYAngleEd(QQuickShear *self, qreal a0) {
  self->setYAngle(a0);
}

//  void QQuickShear::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuickShear7applyToEP10QMatrix4x4(
    const QQuickShear *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickShear::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QQuickShear7applyToEP10QMatrix4x4(
    const QQuickShear *self,
    QMatrix4x4 *matrix) {
  self->QQuickShear::applyTo(matrix);
}
