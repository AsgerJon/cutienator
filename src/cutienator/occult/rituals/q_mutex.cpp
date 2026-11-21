//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmutex.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmutex.h>

//  QMutex::QMutex()
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZN6QMutexC1Ev() {
  return new QMutex();
}

//  QMutex::~QMutex()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMutexD1Ev(QMutex *self) {
  delete self;
}

//  bool QMutex::try_lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMutex8try_lockEv(QMutex *self) {
  return self->try_lock();
}
