//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpathinterpolator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpathinterpolator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickPathInterpolator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickPathInterpolator10metaObjectEv(
    const QQuickPathInterpolator *self) {
  return self->metaObject();
}

//  QString QQuickPathInterpolator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickPathInterpolator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathInterpolator::tr(s, c, n));
}

//  QQuickPathInterpolator::QQuickPathInterpolator(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathInterpolator *ritual_ZN22QQuickPathInterpolatorC1EP7QObject(
    QObject *parent) {
  return new QQuickPathInterpolator(parent);
}

//  QQuickPath *QQuickPathInterpolator::path() const
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZNK22QQuickPathInterpolator4pathEv(
    const QQuickPathInterpolator *self) {
  return self->path();
}

//  void QQuickPathInterpolator::setPath(QQuickPath *path)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathInterpolator7setPathEP10QQuickPath(
    QQuickPathInterpolator *self,
    QQuickPath *path) {
  self->setPath(path);
}

//  qreal QQuickPathInterpolator::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickPathInterpolator8progressEv(
    const QQuickPathInterpolator *self) {
  return self->progress();
}

//  void QQuickPathInterpolator::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathInterpolator11setProgressEd(
    QQuickPathInterpolator *self,
    qreal progress) {
  self->setProgress(progress);
}

//  qreal QQuickPathInterpolator::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickPathInterpolator1xEv(
    const QQuickPathInterpolator *self) {
  return self->x();
}

//  qreal QQuickPathInterpolator::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickPathInterpolator1yEv(
    const QQuickPathInterpolator *self) {
  return self->y();
}

//  qreal QQuickPathInterpolator::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickPathInterpolator5angleEv(
    const QQuickPathInterpolator *self) {
  return self->angle();
}

//  void QQuickPathInterpolator::_q_pathUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathInterpolator14_q_pathUpdatedEv(
    QQuickPathInterpolator *self) {
  self->_q_pathUpdated();
}

#endif  // QT_CONFIG(quick_path)
