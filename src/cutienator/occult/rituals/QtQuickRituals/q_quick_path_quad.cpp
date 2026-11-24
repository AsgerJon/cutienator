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

//  const QMetaObject *QQuickPathQuad::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickPathQuad10metaObjectEv(
    const QQuickPathQuad *self) {
  return self->metaObject();
}

//  QString QQuickPathQuad::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickPathQuad2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathQuad::tr(s, c, n));
}

//  QQuickPathQuad::QQuickPathQuad(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathQuad *ritual_ZN14QQuickPathQuadC1EP7QObject(QObject *parent) {
  return new QQuickPathQuad(parent);
}

//  qreal QQuickPathQuad::controlX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathQuad8controlXEv(const QQuickPathQuad *self) {
  return self->controlX();
}

//  void QQuickPathQuad::setControlX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathQuad11setControlXEd(
    QQuickPathQuad *self,
    qreal x) {
  self->setControlX(x);
}

//  qreal QQuickPathQuad::controlY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathQuad8controlYEv(const QQuickPathQuad *self) {
  return self->controlY();
}

//  void QQuickPathQuad::setControlY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathQuad11setControlYEd(
    QQuickPathQuad *self,
    qreal y) {
  self->setControlY(y);
}

//  qreal QQuickPathQuad::relativeControlX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathQuad16relativeControlXEv(
    const QQuickPathQuad *self) {
  return self->relativeControlX();
}

//  void QQuickPathQuad::setRelativeControlX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathQuad19setRelativeControlXEd(
    QQuickPathQuad *self,
    qreal x) {
  self->setRelativeControlX(x);
}

//  bool QQuickPathQuad::hasRelativeControlX()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickPathQuad19hasRelativeControlXEv(QQuickPathQuad *self) {
  return self->hasRelativeControlX();
}

//  qreal QQuickPathQuad::relativeControlY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickPathQuad16relativeControlYEv(
    const QQuickPathQuad *self) {
  return self->relativeControlY();
}

//  void QQuickPathQuad::setRelativeControlY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickPathQuad19setRelativeControlYEd(
    QQuickPathQuad *self,
    qreal y) {
  self->setRelativeControlY(y);
}

//  bool QQuickPathQuad::hasRelativeControlY()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickPathQuad19hasRelativeControlYEv(QQuickPathQuad *self) {
  return self->hasRelativeControlY();
}

#endif  // QT_CONFIG(quick_path)
