//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h>

//  QFseventsFileSystemWatcherEngine::DirInfo::~DirInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QFseventsFileSystemWatcherEngine7DirInfoD1Ev(
    QFseventsFileSystemWatcherEngine::DirInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
