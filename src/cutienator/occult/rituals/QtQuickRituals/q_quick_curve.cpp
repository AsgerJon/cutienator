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
#include <QtCore/qdebug.h>

//  const QMetaObject *QQuickCurve::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickCurve10metaObjectEv(
    const QQuickCurve *self) {
  return self->metaObject();
}

//  void *QQuickCurve::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QQuickCurve11qt_metacastEPKc(
    QQuickCurve *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickCurve::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QQuickCurve11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickCurve *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickCurve::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickCurve2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCurve::tr(s, c, n));
}

//  void QQuickCurve::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve22qt_qmlMarker_anonymousEv(QQuickCurve *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickCurve::QQuickCurve(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickCurve *ritual_ZN11QQuickCurveC1EP7QObject(QObject *parent) {
  return new QQuickCurve(parent);
}

//  qreal QQuickCurve::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickCurve1xEv(const QQuickCurve *self) {
  return self->x();
}

//  void QQuickCurve::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve4setXEd(QQuickCurve *self, qreal x) {
  self->setX(x);
}

//  bool QQuickCurve::hasX()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickCurve4hasXEv(QQuickCurve *self) {
  return self->hasX();
}

//  qreal QQuickCurve::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickCurve1yEv(const QQuickCurve *self) {
  return self->y();
}

//  void QQuickCurve::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve4setYEd(QQuickCurve *self, qreal y) {
  self->setY(y);
}

//  bool QQuickCurve::hasY()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickCurve4hasYEv(QQuickCurve *self) {
  return self->hasY();
}

//  qreal QQuickCurve::relativeX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickCurve9relativeXEv(const QQuickCurve *self) {
  return self->relativeX();
}

//  void QQuickCurve::setRelativeX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve12setRelativeXEd(QQuickCurve *self, qreal x) {
  self->setRelativeX(x);
}

//  bool QQuickCurve::hasRelativeX()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickCurve12hasRelativeXEv(QQuickCurve *self) {
  return self->hasRelativeX();
}

//  qreal QQuickCurve::relativeY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickCurve9relativeYEv(const QQuickCurve *self) {
  return self->relativeY();
}

//  void QQuickCurve::setRelativeY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve12setRelativeYEd(QQuickCurve *self, qreal y) {
  self->setRelativeY(y);
}

//  bool QQuickCurve::hasRelativeY()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickCurve12hasRelativeYEv(QQuickCurve *self) {
  return self->hasRelativeY();
}

//  void QQuickCurve::addToPath(QPainterPath &a0, const QQuickPathData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve9addToPathER12QPainterPathRK14QQuickPathData(
    QQuickCurve *self,
    QPainterPath *a0,
    const QQuickPathData *a1) {
  self->addToPath(*a0, *a1);
}

//  void QQuickCurve::xChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve8xChangedEv(QQuickCurve *self) {
  self->xChanged();
}

//  void QQuickCurve::yChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve8yChangedEv(QQuickCurve *self) {
  self->yChanged();
}

//  void QQuickCurve::relativeXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve16relativeXChangedEv(QQuickCurve *self) {
  self->relativeXChanged();
}

//  void QQuickCurve::relativeYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickCurve16relativeYChangedEv(QQuickCurve *self) {
  self->relativeYChanged();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QQuickCurve *curve)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK11QQuickCurve(
    const QDebug *debug,
    const QQuickCurve *curve) {
  return new QDebug(operator<<(*debug, curve));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
