//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickPathPolyline::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickPathPolyline10metaObjectEv(
    const QQuickPathPolyline *self) {
  return self->metaObject();
}

//  QString QQuickPathPolyline::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickPathPolyline2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathPolyline::tr(s, c, n));
}

//  QQuickPathPolyline::QQuickPathPolyline(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathPolyline *ritual_ZN18QQuickPathPolylineC1EP7QObject(
    QObject *parent) {
  return new QQuickPathPolyline(parent);
}

//  QVariant QQuickPathPolyline::path() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQuickPathPolyline4pathEv(
    const QQuickPathPolyline *self) {
  return new QVariant(self->path());
}

//  void QQuickPathPolyline::setPath(const QVariant &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPathPolyline7setPathERK8QVariant(
    QQuickPathPolyline *self,
    const QVariant *path) {
  self->setPath(*path);
}

//  void QQuickPathPolyline::setPath(const QList<QPointF> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPathPolyline7setPathERK5QListI7QPointFE(
    QQuickPathPolyline *self,
    const QList<QPointF> *path) {
  self->setPath(*path);
}

//  QPointF QQuickPathPolyline::start() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickPathPolyline5startEv(
    const QQuickPathPolyline *self) {
  return new QPointF(self->start());
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
