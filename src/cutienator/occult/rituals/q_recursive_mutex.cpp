//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmutex.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmutex.h>

//  QRecursiveMutex::QRecursiveMutex()
extern "C" Q_DECL_EXPORT
QRecursiveMutex *ritual_ZN15QRecursiveMutexC1Ev() {
  return new QRecursiveMutex();
}

//  QRecursiveMutex::~QRecursiveMutex()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRecursiveMutexD1Ev(QRecursiveMutex *self) {
  delete self;
}

//  void QRecursiveMutex::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRecursiveMutex6unlockEv(QRecursiveMutex *self) {
  self->unlock();
}
