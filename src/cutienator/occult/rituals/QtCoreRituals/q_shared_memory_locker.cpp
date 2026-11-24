//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsharedmemory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSharedMemoryLocker::QSharedMemoryLocker(QSharedMemory *sharedMemory)
extern "C" Q_DECL_EXPORT
QSharedMemoryLocker *ritual_ZN19QSharedMemoryLockerC1EP13QSharedMemory(
    QSharedMemory *sharedMemory) {
  return new QSharedMemoryLocker(sharedMemory);
}

//  QSharedMemoryLocker::~QSharedMemoryLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSharedMemoryLockerD1Ev(QSharedMemoryLocker *self) {
  delete self;
}

//  bool QSharedMemoryLocker::lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSharedMemoryLocker4lockEv(QSharedMemoryLocker *self) {
  return self->lock();
}

#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(sharedmemory)
