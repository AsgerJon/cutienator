//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QQuickGrabGestureEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickGrabGestureEvent10metaObjectEv(
    const QQuickGrabGestureEvent *self) {
  return self->metaObject();
}

//  void *QQuickGrabGestureEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickGrabGestureEvent11qt_metacastEPKc(
    QQuickGrabGestureEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGrabGestureEvent::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickGrabGestureEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGrabGestureEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickGrabGestureEvent::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGrabGestureEvent24qt_qmlMarker_uncreatableEv(
    QQuickGrabGestureEvent *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickGrabGestureEvent::grab()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickGrabGestureEvent4grabEv(QQuickGrabGestureEvent *self) {
  self->grab();
}

//  bool QQuickGrabGestureEvent::wantsGrab() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickGrabGestureEvent9wantsGrabEv(
    const QQuickGrabGestureEvent *self) {
  return self->wantsGrab();
}

//  QQmlListProperty<QObject> QQuickGrabGestureEvent::touchPoints()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN22QQuickGrabGestureEvent11touchPointsEv(
    QQuickGrabGestureEvent *self) {
  return new QQmlListProperty<QObject>(self->touchPoints());
}

//  qreal QQuickGrabGestureEvent::dragThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickGrabGestureEvent13dragThresholdEv(
    const QQuickGrabGestureEvent *self) {
  return self->dragThreshold();
}

//  a QQmlListProperty<QObject> a ritual of QQuickGrabGestureEvent gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGrabGestureEvent__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
