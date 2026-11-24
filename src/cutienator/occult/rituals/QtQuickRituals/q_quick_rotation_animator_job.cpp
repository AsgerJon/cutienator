//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickRotationAnimatorJob::QQuickRotationAnimatorJob()
extern "C" Q_DECL_EXPORT
QQuickRotationAnimatorJob *ritual_ZN25QQuickRotationAnimatorJobC1Ev() {
  return new QQuickRotationAnimatorJob();
}

//  void QQuickRotationAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRotationAnimatorJob17updateCurrentTimeEi(
    QQuickRotationAnimatorJob *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QQuickRotationAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRotationAnimatorJob9writeBackEv(
    QQuickRotationAnimatorJob *self) {
  self->writeBack();
}

//  void QQuickRotationAnimatorJob::setDirection(QQuickRotationAnimator::Rota
//      tionDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickRotationAnimatorJob12setDirectionEN22QQuickRotationAnimator17RotationDirectionE(
    QQuickRotationAnimatorJob *self,
    QQuickRotationAnimator::RotationDirection direction) {
  self->setDirection(direction);
}

//  QQuickRotationAnimator::RotationDirection
//      QQuickRotationAnimatorJob::direction() const
extern "C" Q_DECL_EXPORT
QQuickRotationAnimator::RotationDirection ritual_ZNK25QQuickRotationAnimatorJob9directionEv(
    const QQuickRotationAnimatorJob *self) {
  return self->direction();
}

//  void QQuickRotationAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickRotationAnimatorJob17updateCurrentTimeEi(
    QQuickRotationAnimatorJob *self,
    int time) {
  self->QQuickRotationAnimatorJob::updateCurrentTime(time);
}

//  void QQuickRotationAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickRotationAnimatorJob9writeBackEv(
    QQuickRotationAnimatorJob *self) {
  self->QQuickRotationAnimatorJob::writeBack();
}
