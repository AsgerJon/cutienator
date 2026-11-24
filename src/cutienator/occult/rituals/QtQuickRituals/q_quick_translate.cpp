//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTranslate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTranslate10metaObjectEv(
    const QQuickTranslate *self) {
  return self->metaObject();
}

//  QString QQuickTranslate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTranslate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTranslate::tr(s, c, n));
}

//  QQuickTranslate::QQuickTranslate(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTranslate *ritual_ZN15QQuickTranslateC1EP7QObject(QObject *parent) {
  return new QQuickTranslate(parent);
}

//  qreal QQuickTranslate::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTranslate1xEv(const QQuickTranslate *self) {
  return self->x();
}

//  void QQuickTranslate::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTranslate4setXEd(QQuickTranslate *self, qreal a0) {
  self->setX(a0);
}

//  qreal QQuickTranslate::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTranslate1yEv(const QQuickTranslate *self) {
  return self->y();
}

//  void QQuickTranslate::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTranslate4setYEd(QQuickTranslate *self, qreal a0) {
  self->setY(a0);
}

//  void QQuickTranslate::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQuickTranslate7applyToEP10QMatrix4x4(
    const QQuickTranslate *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickTranslate::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK15QQuickTranslate7applyToEP10QMatrix4x4(
    const QQuickTranslate *self,
    QMatrix4x4 *matrix) {
  self->QQuickTranslate::applyTo(matrix);
}
