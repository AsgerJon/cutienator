//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickFlickableVisibleArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickFlickableVisibleArea10metaObjectEv(
    const QQuickFlickableVisibleArea *self) {
  return self->metaObject();
}

//  QString QQuickFlickableVisibleArea::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickFlickableVisibleArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlickableVisibleArea::tr(s, c, n));
}

//  void QQuickFlickableVisibleArea::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFlickableVisibleArea22qt_qmlMarker_anonymousEv(
    QQuickFlickableVisibleArea *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickFlickableVisibleArea::QQuickFlickableVisibleArea(QQuickFlickable
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFlickableVisibleArea *ritual_ZN26QQuickFlickableVisibleAreaC1EP15QQuickFlickable(
    QQuickFlickable *parent) {
  return new QQuickFlickableVisibleArea(parent);
}

//  qreal QQuickFlickableVisibleArea::xPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQuickFlickableVisibleArea9xPositionEv(
    const QQuickFlickableVisibleArea *self) {
  return self->xPosition();
}

//  qreal QQuickFlickableVisibleArea::widthRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQuickFlickableVisibleArea10widthRatioEv(
    const QQuickFlickableVisibleArea *self) {
  return self->widthRatio();
}

//  qreal QQuickFlickableVisibleArea::yPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQuickFlickableVisibleArea9yPositionEv(
    const QQuickFlickableVisibleArea *self) {
  return self->yPosition();
}

//  qreal QQuickFlickableVisibleArea::heightRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQuickFlickableVisibleArea11heightRatioEv(
    const QQuickFlickableVisibleArea *self) {
  return self->heightRatio();
}

//  void QQuickFlickableVisibleArea::updateVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFlickableVisibleArea13updateVisibleEv(
    QQuickFlickableVisibleArea *self) {
  self->updateVisible();
}
