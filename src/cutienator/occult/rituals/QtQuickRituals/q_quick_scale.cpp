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

//  const QMetaObject *QQuickScale::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickScale10metaObjectEv(
    const QQuickScale *self) {
  return self->metaObject();
}

//  void *QQuickScale::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QQuickScale11qt_metacastEPKc(
    QQuickScale *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickScale::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QQuickScale11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickScale *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickScale::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickScale2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScale::tr(s, c, n));
}

//  QQuickScale::QQuickScale(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScale *ritual_ZN11QQuickScaleC1EP7QObject(QObject *parent) {
  return new QQuickScale(parent);
}

//  QVector3D QQuickScale::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuickScale6originEv(const QQuickScale *self) {
  return new QVector3D(self->origin());
}

//  void QQuickScale::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale9setOriginERK9QVector3D(
    QQuickScale *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QQuickScale::xScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickScale6xScaleEv(const QQuickScale *self) {
  return self->xScale();
}

//  void QQuickScale::setXScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale9setXScaleEd(QQuickScale *self, qreal a0) {
  self->setXScale(a0);
}

//  qreal QQuickScale::yScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickScale6yScaleEv(const QQuickScale *self) {
  return self->yScale();
}

//  void QQuickScale::setYScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale9setYScaleEd(QQuickScale *self, qreal a0) {
  self->setYScale(a0);
}

//  qreal QQuickScale::zScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickScale6zScaleEv(const QQuickScale *self) {
  return self->zScale();
}

//  void QQuickScale::setZScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale9setZScaleEd(QQuickScale *self, qreal a0) {
  self->setZScale(a0);
}

//  void QQuickScale::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuickScale7applyToEP10QMatrix4x4(
    const QQuickScale *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickScale::originChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale13originChangedEv(QQuickScale *self) {
  self->originChanged();
}

//  void QQuickScale::xScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale13xScaleChangedEv(QQuickScale *self) {
  self->xScaleChanged();
}

//  void QQuickScale::yScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale13yScaleChangedEv(QQuickScale *self) {
  self->yScaleChanged();
}

//  void QQuickScale::zScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale13zScaleChangedEv(QQuickScale *self) {
  self->zScaleChanged();
}

//  void QQuickScale::scaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickScale12scaleChangedEv(QQuickScale *self) {
  self->scaleChanged();
}

//  QQuickScalePrivate *QQuickScale::d_func()
extern "C" Q_DECL_EXPORT
QQuickScalePrivate *ritual_ZN11QQuickScale6d_funcEv(QQuickScale *self) {
  return self->d_func();
}

//  const QQuickScalePrivate *QQuickScale::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickScalePrivate *ritual_ZNK11QQuickScale6d_funcEv(
    const QQuickScale *self) {
  return self->d_func();
}

//  void QQuickScale::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QQuickScale7applyToEP10QMatrix4x4(
    const QQuickScale *self,
    QMatrix4x4 *matrix) {
  self->QQuickScale::applyTo(matrix);
}
