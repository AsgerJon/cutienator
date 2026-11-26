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

//  const QMetaObject *QQuickPathMultiline::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPathMultiline10metaObjectEv(
    const QQuickPathMultiline *self) {
  return self->metaObject();
}

//  void *QQuickPathMultiline::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickPathMultiline11qt_metacastEPKc(
    QQuickPathMultiline *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPathMultiline::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickPathMultiline11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPathMultiline *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPathMultiline::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickPathMultiline2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathMultiline::tr(s, c, n));
}

//  QQuickPathMultiline::QQuickPathMultiline(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathMultiline *ritual_ZN19QQuickPathMultilineC1EP7QObject(
    QObject *parent) {
  return new QQuickPathMultiline(parent);
}

//  QVariant QQuickPathMultiline::paths() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickPathMultiline5pathsEv(
    const QQuickPathMultiline *self) {
  return new QVariant(self->paths());
}

//  void QQuickPathMultiline::setPaths(const QVariant &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathMultiline8setPathsERK8QVariant(
    QQuickPathMultiline *self,
    const QVariant *paths) {
  self->setPaths(*paths);
}

//  void QQuickPathMultiline::setPaths(const QList<QList<QPointF>> &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathMultiline8setPathsERK5QListIS0_I7QPointFEE(
    QQuickPathMultiline *self,
    const QList<QList<QPointF>> *paths) {
  self->setPaths(*paths);
}

//  QPointF QQuickPathMultiline::start() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QQuickPathMultiline5startEv(
    const QQuickPathMultiline *self) {
  return new QPointF(self->start());
}

//  void QQuickPathMultiline::addToPath(QPainterPath &path, const
//      QQuickPathData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathMultiline9addToPathER12QPainterPathRK14QQuickPathData(
    QQuickPathMultiline *self,
    QPainterPath *path,
    const QQuickPathData *a1) {
  self->addToPath(*path, *a1);
}

//  void QQuickPathMultiline::pathsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathMultiline12pathsChangedEv(
    QQuickPathMultiline *self) {
  self->pathsChanged();
}

//  void QQuickPathMultiline::startChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathMultiline12startChangedEv(
    QQuickPathMultiline *self) {
  self->startChanged();
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
