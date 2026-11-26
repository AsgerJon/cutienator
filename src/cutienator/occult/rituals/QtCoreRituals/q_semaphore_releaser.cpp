//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsemaphore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsemaphore.h>

//  QSemaphoreReleaser::QSemaphoreReleaser()
extern "C" Q_DECL_EXPORT
QSemaphoreReleaser *ritual_ZN18QSemaphoreReleaserC1Ev() {
  return new QSemaphoreReleaser();
}

//  QSemaphoreReleaser::QSemaphoreReleaser(QSemaphore &sem, int n)
extern "C" Q_DECL_EXPORT
QSemaphoreReleaser *ritual_ZN18QSemaphoreReleaserC1ER10QSemaphorei(
    QSemaphore *sem,
    int n) {
  return new QSemaphoreReleaser(*sem, n);
}

//  QSemaphoreReleaser::QSemaphoreReleaser(QSemaphore *sem, int n)
extern "C" Q_DECL_EXPORT
QSemaphoreReleaser *ritual_ZN18QSemaphoreReleaserC1EP10QSemaphorei(
    QSemaphore *sem,
    int n) {
  return new QSemaphoreReleaser(sem, n);
}

//  QSemaphoreReleaser::QSemaphoreReleaser(QSemaphoreReleaser &&other)
extern "C" Q_DECL_EXPORT
QSemaphoreReleaser *ritual_ZN18QSemaphoreReleaserC1EOS_(
    QSemaphoreReleaser *other) {
  return new QSemaphoreReleaser(std::move(*other));
}

//  QSemaphoreReleaser &QSemaphoreReleaser::operator=(QSemaphoreReleaser
//      &&other)
extern "C" Q_DECL_EXPORT
QSemaphoreReleaser *ritual_ZN18QSemaphoreReleaseraSEOS_(
    QSemaphoreReleaser *self,
    QSemaphoreReleaser *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSemaphoreReleaser::~QSemaphoreReleaser()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSemaphoreReleaserD1Ev(QSemaphoreReleaser *self) {
  delete self;
}

//  void QSemaphoreReleaser::swap(QSemaphoreReleaser &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSemaphoreReleaser4swapERS_(
    QSemaphoreReleaser *self,
    QSemaphoreReleaser *other) {
  self->swap(*other);
}

//  QSemaphore *QSemaphoreReleaser::semaphore() const
extern "C" Q_DECL_EXPORT
QSemaphore *ritual_ZNK18QSemaphoreReleaser9semaphoreEv(
    const QSemaphoreReleaser *self) {
  return self->semaphore();
}

//  QSemaphore *QSemaphoreReleaser::cancel()
extern "C" Q_DECL_EXPORT
QSemaphore *ritual_ZN18QSemaphoreReleaser6cancelEv(
    QSemaphoreReleaser *self) {
  return self->cancel();
}
