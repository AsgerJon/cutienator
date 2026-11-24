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

//  QPanGesture *QPanGesturePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPanGesture *ritual_ZN18QPanGesturePrivate6q_funcEv(
    QPanGesturePrivate *self) {
  return self->q_func();
}

//  const QPanGesture *QPanGesturePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPanGesture *ritual_ZNK18QPanGesturePrivate6q_funcEv(
    const QPanGesturePrivate *self) {
  return self->q_func();
}

//  QPanGesturePrivate::QPanGesturePrivate()
extern "C" Q_DECL_EXPORT
QPanGesturePrivate *ritual_ZN18QPanGesturePrivateC1Ev() {
  return new QPanGesturePrivate();
}

//  qreal QPanGesturePrivate::horizontalVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QPanGesturePrivate18horizontalVelocityEv(
    const QPanGesturePrivate *self) {
  return self->horizontalVelocity();
}

//  void QPanGesturePrivate::setHorizontalVelocity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPanGesturePrivate21setHorizontalVelocityEd(
    QPanGesturePrivate *self,
    qreal value) {
  self->setHorizontalVelocity(value);
}

//  qreal QPanGesturePrivate::verticalVelocity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QPanGesturePrivate16verticalVelocityEv(
    const QPanGesturePrivate *self) {
  return self->verticalVelocity();
}

//  void QPanGesturePrivate::setVerticalVelocity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPanGesturePrivate19setVerticalVelocityEd(
    QPanGesturePrivate *self,
    qreal value) {
  self->setVerticalVelocity(value);
}

#endif  // !defined(QT_NO_GESTURES)
