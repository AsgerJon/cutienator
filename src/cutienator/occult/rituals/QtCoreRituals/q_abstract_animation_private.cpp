//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/qabstractanimation.h>
#endif
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

//  size_t QAbstractAnimationPrivate::_qt_property_state_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QAbstractAnimationPrivate25_qt_property_state_offsetEv() {
  return QAbstractAnimationPrivate::_qt_property_state_offset();
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

//  size_t QAbstractAnimationPrivate::_qt_property_direction_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QAbstractAnimationPrivate29_qt_property_direction_offsetEv() {
  return QAbstractAnimationPrivate::_qt_property_direction_offset();
}

//  void QAbstractAnimationPrivate::setCurrentTime(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate14setCurrentTimeEi(
    QAbstractAnimationPrivate *self,
    int msecs) {
  self->setCurrentTime(msecs);
}

//  size_t QAbstractAnimationPrivate::_qt_property_totalCurrentTime_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QAbstractAnimationPrivate36_qt_property_totalCurrentTime_offsetEv() {
  return QAbstractAnimationPrivate::_qt_property_totalCurrentTime_offset();
}

//  size_t QAbstractAnimationPrivate::_qt_property_loopCount_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QAbstractAnimationPrivate29_qt_property_loopCount_offsetEv() {
  return QAbstractAnimationPrivate::_qt_property_loopCount_offset();
}

//  void QAbstractAnimationPrivate::emitCurrentLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractAnimationPrivate22emitCurrentLoopChangedEv(
    QAbstractAnimationPrivate *self) {
  self->emitCurrentLoopChanged();
}

//  size_t QAbstractAnimationPrivate::_qt_property_currentLoop_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QAbstractAnimationPrivate31_qt_property_currentLoop_offsetEv() {
  return QAbstractAnimationPrivate::_qt_property_currentLoop_offset();
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
#endif  // QT_CONFIG(animation)
