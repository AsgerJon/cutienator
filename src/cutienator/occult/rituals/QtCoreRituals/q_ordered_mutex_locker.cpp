//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qorderedmutexlocker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qorderedmutexlocker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOrderedMutexLocker::QOrderedMutexLocker(QBasicMutex *m1, QBasicMutex
//      *m2)
extern "C" Q_DECL_EXPORT
QOrderedMutexLocker *ritual_ZN19QOrderedMutexLockerC1EP11QBasicMutexS1_(
    QBasicMutex *m1,
    QBasicMutex *m2) {
  return new QOrderedMutexLocker(m1, m2);
}

//  void QOrderedMutexLocker::swap(QOrderedMutexLocker &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrderedMutexLocker4swapERS_(
    QOrderedMutexLocker *self,
    QOrderedMutexLocker *other) {
  self->swap(*other);
}

//  QOrderedMutexLocker &QOrderedMutexLocker::operator=(QOrderedMutexLocker
//      &&other)
extern "C" Q_DECL_EXPORT
QOrderedMutexLocker *ritual_ZN19QOrderedMutexLockeraSEOS_(
    QOrderedMutexLocker *self,
    QOrderedMutexLocker *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOrderedMutexLocker::QOrderedMutexLocker(QOrderedMutexLocker &&other)
extern "C" Q_DECL_EXPORT
QOrderedMutexLocker *ritual_ZN19QOrderedMutexLockerC1EOS_(
    QOrderedMutexLocker *other) {
  return new QOrderedMutexLocker(std::move(*other));
}

//  QOrderedMutexLocker::~QOrderedMutexLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrderedMutexLockerD1Ev(QOrderedMutexLocker *self) {
  delete self;
}

//  void QOrderedMutexLocker::relock()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrderedMutexLocker6relockEv(QOrderedMutexLocker *self) {
  self->relock();
}

//  void QOrderedMutexLocker::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrderedMutexLocker7dismissEv(QOrderedMutexLocker *self) {
  self->dismiss();
}

//  void QOrderedMutexLocker::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrderedMutexLocker6unlockEv(QOrderedMutexLocker *self) {
  self->unlock();
}

//  bool QOrderedMutexLocker::relock(QBasicMutex *mtx1, QBasicMutex *mtx2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QOrderedMutexLocker6relockEP11QBasicMutexS1_(
    QBasicMutex *mtx1,
    QBasicMutex *mtx2) {
  return QOrderedMutexLocker::relock(mtx1, mtx2);
}

#endif  // QT_CONFIG(thread)
