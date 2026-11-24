//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>

//  bool QWindowsFileSystemWatcherEngine::PathInfo::operator!=(const
//      QFileInfo &fileInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QWindowsFileSystemWatcherEngine8PathInfoneERK9QFileInfo(
    const QWindowsFileSystemWatcherEngine::PathInfo *self,
    const QFileInfo *fileInfo) {
  return self->operator!=(*fileInfo);
}

//  QWindowsFileSystemWatcherEngine::PathInfo::~PathInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsFileSystemWatcherEngine8PathInfoD1Ev(
    QWindowsFileSystemWatcherEngine::PathInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
