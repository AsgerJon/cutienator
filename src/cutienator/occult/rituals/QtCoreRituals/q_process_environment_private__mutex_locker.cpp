//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#if !(defined(Q_OS_WIN))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QProcessEnvironmentPrivate::MutexLocker::MutexLocker(const
//      QProcessEnvironmentPrivate *d)
extern "C" Q_DECL_EXPORT
QProcessEnvironmentPrivate::MutexLocker *ritual_ZN26QProcessEnvironmentPrivate11MutexLockerC1EPKS_(
    const QProcessEnvironmentPrivate *d) {
  return new QProcessEnvironmentPrivate::MutexLocker(d);
}

#endif  // !(defined(Q_OS_WIN))
#endif  // QT_CONFIG(processenvironment)
