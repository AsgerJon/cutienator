//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickPathArc::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickPathArc10metaObjectEv(
    const QQuickPathArc *self) {
  return self->metaObject();
}

//  QString QQuickPathArc::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickPathArc2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathArc::tr(s, c, n));
}

//  QQuickPathArc::QQuickPathArc(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathArc *ritual_ZN13QQuickPathArcC1EP7QObject(QObject *parent) {
  return new QQuickPathArc(parent);
}

//  qreal QQuickPathArc::radiusX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickPathArc7radiusXEv(const QQuickPathArc *self) {
  return self->radiusX();
}

//  void QQuickPathArc::setRadiusX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathArc10setRadiusXEd(QQuickPathArc *self, qreal a0) {
  self->setRadiusX(a0);
}

//  qreal QQuickPathArc::radiusY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickPathArc7radiusYEv(const QQuickPathArc *self) {
  return self->radiusY();
}

//  void QQuickPathArc::setRadiusY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathArc10setRadiusYEd(QQuickPathArc *self, qreal a0) {
  self->setRadiusY(a0);
}

//  bool QQuickPathArc::useLargeArc() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQuickPathArc11useLargeArcEv(const QQuickPathArc *self) {
  return self->useLargeArc();
}

//  void QQuickPathArc::setUseLargeArc(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathArc14setUseLargeArcEb(
    QQuickPathArc *self,
    bool a0) {
  self->setUseLargeArc(a0);
}

//  ArcDirection QQuickPathArc::direction() const
extern "C" Q_DECL_EXPORT
QQuickPathArc::ArcDirection ritual_ZNK13QQuickPathArc9directionEv(
    const QQuickPathArc *self) {
  return self->direction();
}

//  void QQuickPathArc::setDirection(ArcDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathArc12setDirectionENS_12ArcDirectionE(
    QQuickPathArc *self,
    QQuickPathArc::ArcDirection direction) {
  self->setDirection(direction);
}

//  qreal QQuickPathArc::xAxisRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QQuickPathArc13xAxisRotationEv(const QQuickPathArc *self) {
  return self->xAxisRotation();
}

//  void QQuickPathArc::setXAxisRotation(qreal rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickPathArc16setXAxisRotationEd(
    QQuickPathArc *self,
    qreal rotation) {
  self->setXAxisRotation(rotation);
}

#endif  // QT_CONFIG(quick_path)
