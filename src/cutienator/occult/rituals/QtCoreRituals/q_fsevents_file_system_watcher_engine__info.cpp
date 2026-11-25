//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
//  A 'timespec' is passed as an address.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h>
#include <QtCore/qstring.h>

//  QFseventsFileSystemWatcherEngine::Info::Info()
extern "C" Q_DECL_EXPORT
QFseventsFileSystemWatcherEngine::Info *ritual_ZN32QFseventsFileSystemWatcherEngine4InfoC1Ev() {
  return new QFseventsFileSystemWatcherEngine::Info();
}

//  QFseventsFileSystemWatcherEngine::Info::Info(const QString &origPath,
//      const timespec &ctime, mode_t mode, const QString &watchedPath)
extern "C" Q_DECL_EXPORT
QFseventsFileSystemWatcherEngine::Info *ritual_ZN32QFseventsFileSystemWatcherEngine4InfoC1ERK7QStringRK8timespectS3_(
    const QString *origPath,
    const timespec *ctime,
    mode_t mode,
    const QString *watchedPath) {
  return new QFseventsFileSystemWatcherEngine::Info(*origPath, *ctime, mode, *watchedPath);
}

//  QFseventsFileSystemWatcherEngine::Info::~Info()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QFseventsFileSystemWatcherEngine4InfoD1Ev(
    QFseventsFileSystemWatcherEngine::Info *self) {
  delete self;
}

#endif  // defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
