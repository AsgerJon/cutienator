//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions are called, through the object. Not written: 'tr',
//  'create', 'processEvent', the signals and the slots.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_fsevents_p.h>
#include <QtCore/qstringlist.h>

//  const QMetaObject *QFseventsFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QFseventsFileSystemWatcherEngine10metaObjectEv(
    const QFseventsFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  QFseventsFileSystemWatcherEngine::~QFseventsFileSystemWatcherEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QFseventsFileSystemWatcherEngineD1Ev(
    QFseventsFileSystemWatcherEngine *self) {
  delete self;
}

//  QStringList QFseventsFileSystemWatcherEngine::addPaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN32QFseventsFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_(
    QFseventsFileSystemWatcherEngine *self,
    const QStringList *paths,
    QStringList *files,
    QStringList *directories) {
  return new QStringList(self->addPaths(*paths, files, directories));
}

//  QStringList QFseventsFileSystemWatcherEngine::removePaths(const
//      QStringList &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QStringList *ritual_ZN32QFseventsFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_(
    QFseventsFileSystemWatcherEngine *self,
    const QStringList *paths,
    QStringList *files,
    QStringList *directories) {
  return new QStringList(self->removePaths(*paths, files, directories));
}

#endif  // defined(Q_OS_MACOS) && QT_CONFIG(filesystemwatcher)
