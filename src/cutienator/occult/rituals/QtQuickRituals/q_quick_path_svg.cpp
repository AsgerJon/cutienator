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

//  const QMetaObject *QQuickPathSvg::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickPathSvg10metaObjectEv(
    const QQuickPathSvg *self) {
  return self->metaObject();
}

//  void *QQuickPathSvg::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QQuickPathSvg11qt_metacastEPKc(
    QQuickPathSvg *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPathSvg::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQuickPathSvg11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPathSvg *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPathSvg::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickPathSvg2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathSvg::tr(s, c, n));
}

//  QQuickPathSvg::QQuickPathSvg(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathSvg *ritual_ZN13QQuickPathSvgC1EP7QObject(QObject *parent) {
  return new QQuickPathSvg(parent);
}

//  QString QQuickPathSvg::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQuickPathSvg4pathEv(const QQuickPathSvg *self) {
  return new QString(self->path());
}

//  void QQuickPathSvg::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathSvg7setPathERK7QString(
    QQuickPathSvg *self,
    const QString *path) {
  self->setPath(*path);
}

//  void QQuickPathSvg::addToPath(QPainterPath &path, const QQuickPathData
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathSvg9addToPathER12QPainterPathRK14QQuickPathData(
    QQuickPathSvg *self,
    QPainterPath *path,
    const QQuickPathData *a1) {
  self->addToPath(*path, *a1);
}

//  void QQuickPathSvg::pathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathSvg11pathChangedEv(QQuickPathSvg *self) {
  self->pathChanged();
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
