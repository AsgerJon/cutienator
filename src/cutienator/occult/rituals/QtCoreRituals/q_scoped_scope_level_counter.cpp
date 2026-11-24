//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScopedScopeLevelCounter::QScopedScopeLevelCounter(QThreadData
//      *threadData)
extern "C" Q_DECL_EXPORT
QScopedScopeLevelCounter *ritual_ZN24QScopedScopeLevelCounterC1EP11QThreadData(
    QThreadData *threadData) {
  return new QScopedScopeLevelCounter(threadData);
}

//  QScopedScopeLevelCounter::~QScopedScopeLevelCounter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScopedScopeLevelCounterD1Ev(
    QScopedScopeLevelCounter *self) {
  delete self;
}
