//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>
#include <QtCore/qdebug.h>

//  QMacAutoReleasePool::QMacAutoReleasePool()
extern "C" Q_DECL_EXPORT
QMacAutoReleasePool *ritual_ZN19QMacAutoReleasePoolC1Ev() {
  return new QMacAutoReleasePool();
}

//  QMacAutoReleasePool::~QMacAutoReleasePool()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMacAutoReleasePoolD1Ev(QMacAutoReleasePool *self) {
  delete self;
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QMacAutoReleasePool *pool)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK19QMacAutoReleasePool(
    const QDebug *debug,
    const QMacAutoReleasePool *pool) {
  return new QDebug(operator<<(*debug, pool));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#endif  // defined(Q_OS_DARWIN)
