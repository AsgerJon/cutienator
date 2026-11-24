//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QQuickUniformAnimatorJob::QQuickUniformAnimatorJob()
extern "C" Q_DECL_EXPORT
QQuickUniformAnimatorJob *ritual_ZN24QQuickUniformAnimatorJobC1Ev() {
  return new QQuickUniformAnimatorJob();
}

//  void QQuickUniformAnimatorJob::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob9setTargetEP10QQuickItem(
    QQuickUniformAnimatorJob *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  void QQuickUniformAnimatorJob::setUniform(const QByteArray &uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob10setUniformERK10QByteArray(
    QQuickUniformAnimatorJob *self,
    const QByteArray *uniform) {
  self->setUniform(*uniform);
}

//  QByteArray QQuickUniformAnimatorJob::uniform() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QQuickUniformAnimatorJob7uniformEv(
    const QQuickUniformAnimatorJob *self) {
  return new QByteArray(self->uniform());
}

//  void QQuickUniformAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob17updateCurrentTimeEi(
    QQuickUniformAnimatorJob *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QQuickUniformAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob9writeBackEv(
    QQuickUniformAnimatorJob *self) {
  self->writeBack();
}

//  void QQuickUniformAnimatorJob::postSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob8postSyncEv(
    QQuickUniformAnimatorJob *self) {
  self->postSync();
}

//  void QQuickUniformAnimatorJob::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickUniformAnimatorJob10invalidateEv(
    QQuickUniformAnimatorJob *self) {
  self->invalidate();
}

//  void QQuickUniformAnimatorJob::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickUniformAnimatorJob9setTargetEP10QQuickItem(
    QQuickUniformAnimatorJob *self,
    QQuickItem *target) {
  self->QQuickUniformAnimatorJob::setTarget(target);
}

//  void QQuickUniformAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickUniformAnimatorJob17updateCurrentTimeEi(
    QQuickUniformAnimatorJob *self,
    int time) {
  self->QQuickUniformAnimatorJob::updateCurrentTime(time);
}

//  void QQuickUniformAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickUniformAnimatorJob9writeBackEv(
    QQuickUniformAnimatorJob *self) {
  self->QQuickUniformAnimatorJob::writeBack();
}

//  void QQuickUniformAnimatorJob::postSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickUniformAnimatorJob8postSyncEv(
    QQuickUniformAnimatorJob *self) {
  self->QQuickUniformAnimatorJob::postSync();
}

//  void QQuickUniformAnimatorJob::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickUniformAnimatorJob10invalidateEv(
    QQuickUniformAnimatorJob *self) {
  self->QQuickUniformAnimatorJob::invalidate();
}

#endif  // QT_CONFIG(quick_shadereffect)
