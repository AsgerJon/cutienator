//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcore_unix_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcore_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qt_semun::~qt_semun()
extern "C" Q_DECL_EXPORT
void ritual_ZN8qt_semunD1Ev(qt_semun *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX)
