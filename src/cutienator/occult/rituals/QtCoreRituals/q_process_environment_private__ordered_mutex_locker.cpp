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

//  QProcessEnvironmentPrivate::OrderedMutexLocker::OrderedMutexLocker(const
//      QProcessEnvironmentPrivate *d1, const QProcessEnvironmentPrivate *d2)
extern "C" Q_DECL_EXPORT
QProcessEnvironmentPrivate::OrderedMutexLocker *ritual_ZN26QProcessEnvironmentPrivate18OrderedMutexLockerC1EPKS_S2_(
    const QProcessEnvironmentPrivate *d1,
    const QProcessEnvironmentPrivate *d2) {
  return new QProcessEnvironmentPrivate::OrderedMutexLocker(d1, d2);
}

#endif  // !(defined(Q_OS_WIN))
#endif  // QT_CONFIG(processenvironment)
