//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgesture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgesture.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgesture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSwipeGesture *QSwipeGesturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSwipeGesture *ritual_ZN20QSwipeGesturePrivate6q_funcEv(
    QSwipeGesturePrivate *self) {
  return self->q_func();
}

//  const QSwipeGesture *QSwipeGesturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSwipeGesture *ritual_ZNK20QSwipeGesturePrivate6q_funcEv(
    const QSwipeGesturePrivate *self) {
  return self->q_func();
}

//  QSwipeGesturePrivate::QSwipeGesturePrivate()
extern "C" Q_DECL_EXPORT
QSwipeGesturePrivate *ritual_ZN20QSwipeGesturePrivateC1Ev() {
  return new QSwipeGesturePrivate();
}

//  qreal QSwipeGesturePrivate::velocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QSwipeGesturePrivate8velocityEv(
    const QSwipeGesturePrivate *self) {
  return self->velocity();
}

//  void QSwipeGesturePrivate::setVelocity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSwipeGesturePrivate11setVelocityEd(
    QSwipeGesturePrivate *self,
    qreal value) {
  self->setVelocity(value);
}

#endif  // !defined(QT_NO_GESTURES)
