//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Not written: 'versionsForImage', 'applicationVersion' and
//  'libraryVersion', which give a 'std::pair'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>
#include <QtCore/qoperatingsystemversion.h>

//  QOperatingSystemVersion QMacVersion::buildSDK(VersionTarget target)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN11QMacVersion8buildSDKENS_13VersionTargetE(
    QMacVersion::VersionTarget target) {
  return new QOperatingSystemVersion(QMacVersion::buildSDK(target));
}

//  QOperatingSystemVersion QMacVersion::deploymentTarget(VersionTarget
//      target)
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN11QMacVersion16deploymentTargetENS_13VersionTargetE(
    QMacVersion::VersionTarget target) {
  return new QOperatingSystemVersion(QMacVersion::deploymentTarget(target));
}

//  QOperatingSystemVersion QMacVersion::currentRuntime()
extern "C" Q_DECL_EXPORT
QOperatingSystemVersion *ritual_ZN11QMacVersion14currentRuntimeEv() {
  return new QOperatingSystemVersion(QMacVersion::currentRuntime());
}

//  QMacVersion::QMacVersion()
extern "C" Q_DECL_EXPORT
QMacVersion *ritual_ZN11QMacVersionC1Ev() {
  return new QMacVersion();
}

//  QMacVersion::~QMacVersion()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMacVersionD1Ev(QMacVersion *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
