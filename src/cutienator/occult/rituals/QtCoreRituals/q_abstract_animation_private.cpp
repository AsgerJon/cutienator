//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qabstractanimation.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstractAnimationPrivate::QAbstractAnimationPrivate()
extern "C" Q_DECL_EXPORT
QAbstractAnimationPrivate *ritual_ZN25QAbstractAnimationPrivateC1Ev() {
  return new QAbstractAnimationPrivate();
}

//  QAbstractAnimationPrivate::~QAbstractAnimationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivateD1Ev(
    QAbstractAnimationPrivate *self) {
  delete self;
}

//  QAbstractAnimationPrivate
//      *QAbstractAnimationPrivate::get(QAbstractAnimation *q)
extern "C" Q_DECL_EXPORT
QAbstractAnimationPrivate *ritual_ZN25QAbstractAnimationPrivate3getEP18QAbstractAnimation(
    QAbstractAnimation *q) {
  return QAbstractAnimationPrivate::get(q);
}

//  void QAbstractAnimationPrivate::setState(QAbstractAnimation::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate8setStateEN18QAbstractAnimation5StateE(
    QAbstractAnimationPrivate *self,
    QAbstractAnimation::State state) {
  self->setState(state);
}

//  void
//      QAbstractAnimationPrivate::setDirection(QAbstractAnimation::Direction
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate12setDirectionEN18QAbstractAnimation9DirectionE(
    QAbstractAnimationPrivate *self,
    QAbstractAnimation::Direction direction) {
  self->setDirection(direction);
}

//  void QAbstractAnimationPrivate::emitDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate20emitDirectionChangedEv(
    QAbstractAnimationPrivate *self) {
  self->emitDirectionChanged();
}

//  void QAbstractAnimationPrivate::setCurrentTime(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate14setCurrentTimeEi(
    QAbstractAnimationPrivate *self,
    int msecs) {
  self->setCurrentTime(msecs);
}

//  void QAbstractAnimationPrivate::emitCurrentLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate22emitCurrentLoopChangedEv(
    QAbstractAnimationPrivate *self) {
  self->emitCurrentLoopChanged();
}

//  QAbstractAnimation *QAbstractAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZN25QAbstractAnimationPrivate6q_funcEv(
    QAbstractAnimationPrivate *self) {
  return self->q_func();
}

//  const QAbstractAnimation *QAbstractAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractAnimation *ritual_ZNK25QAbstractAnimationPrivate6q_funcEv(
    const QAbstractAnimationPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(animation)
