//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
#if !(defined(Q_OS_WIN))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QProcessPrivate::UnixExtras::~UnixExtras()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate10UnixExtrasD1Ev(
    QProcessPrivate::UnixExtras *self) {
  delete self;
}

#endif  // !(defined(Q_OS_WIN))
#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
#endif  // QT_CONFIG(processenvironment)
