//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSystemSemaphoreWin32::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphoreWin328supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSystemSemaphoreWin32::supports(type);
}

//  bool QSystemSemaphoreWin32::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphoreWin3219runtimeSupportCheckEv() {
  return QSystemSemaphoreWin32::runtimeSupportCheck();
}

//  QSystemSemaphoreWin32::~QSystemSemaphoreWin32()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSystemSemaphoreWin32D1Ev(QSystemSemaphoreWin32 *self) {
  delete self;
}

#endif  // QT_CONFIG(systemsemaphore)
