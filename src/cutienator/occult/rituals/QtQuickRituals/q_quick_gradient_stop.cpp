//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QQuickGradientStop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickGradientStop10metaObjectEv(
    const QQuickGradientStop *self) {
  return self->metaObject();
}

//  void *QQuickGradientStop::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickGradientStop11qt_metacastEPKc(
    QQuickGradientStop *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGradientStop::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickGradientStop11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGradientStop *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGradientStop::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickGradientStop2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGradientStop::tr(s, c, n));
}

//  QQuickGradientStop::QQuickGradientStop(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickGradientStop *ritual_ZN18QQuickGradientStopC1EP7QObject(
    QObject *parent) {
  return new QQuickGradientStop(parent);
}

//  qreal QQuickGradientStop::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickGradientStop8positionEv(
    const QQuickGradientStop *self) {
  return self->position();
}

//  void QQuickGradientStop::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGradientStop11setPositionEd(
    QQuickGradientStop *self,
    qreal position) {
  self->setPosition(position);
}

//  QColor QQuickGradientStop::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QQuickGradientStop5colorEv(
    const QQuickGradientStop *self) {
  return new QColor(self->color());
}

//  void QQuickGradientStop::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGradientStop8setColorERK6QColor(
    QQuickGradientStop *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickGradientStop::updateGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickGradientStop14updateGradientEv(
    QQuickGradientStop *self) {
  self->updateGradient();
}
