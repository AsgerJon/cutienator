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

//  void *QQuickTranslate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickTranslate11qt_metacastEPKc(
    QQuickTranslate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTranslate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickTranslate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTranslate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuickTranslate::xChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTranslate8xChangedEv(QQuickTranslate *self) {
  self->xChanged();
}

//  void QQuickTranslate::yChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTranslate8yChangedEv(QQuickTranslate *self) {
  self->yChanged();
}

//  QQuickTranslatePrivate *QQuickTranslate::d_func()
extern "C" Q_DECL_EXPORT
QQuickTranslatePrivate *ritual_ZN15QQuickTranslate6d_funcEv(
    QQuickTranslate *self) {
  return self->d_func();
}

//  const QQuickTranslatePrivate *QQuickTranslate::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTranslatePrivate *ritual_ZNK15QQuickTranslate6d_funcEv(
    const QQuickTranslate *self) {
  return self->d_func();
}

//  void QQuickTranslate::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK15QQuickTranslate7applyToEP10QMatrix4x4(
    const QQuickTranslate *self,
    QMatrix4x4 *matrix) {
  self->QQuickTranslate::applyTo(matrix);
}
