//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsharedmemory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSharedMemoryWin32::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSharedMemoryWin3219runtimeSupportCheckEv() {
  return QSharedMemoryWin32::runtimeSupportCheck();
}

//  bool QSharedMemoryWin32::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSharedMemoryWin328supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSharedMemoryWin32::supports(type);
}

//  QSharedMemoryWin32::~QSharedMemoryWin32()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSharedMemoryWin32D1Ev(QSharedMemoryWin32 *self) {
  delete self;
}

#endif  // QT_CONFIG(sharedmemory)
