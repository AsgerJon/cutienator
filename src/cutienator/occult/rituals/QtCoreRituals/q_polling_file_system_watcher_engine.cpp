//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_polling_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher)
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_polling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QPollingFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QPollingFileSystemWatcherEngine10metaObjectEv(
    const QPollingFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  void *QPollingFileSystemWatcherEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QPollingFileSystemWatcherEngine11qt_metacastEPKc(
    QPollingFileSystemWatcherEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPollingFileSystemWatcherEngine::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QPollingFileSystemWatcherEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QPollingFileSystemWatcherEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QStringList QPollingFileSystemWatcherEngine::addPaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN31QPollingFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_(
    QPollingFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->addPaths(*paths, files, directories));
}

//  QStringList QPollingFileSystemWatcherEngine::removePaths(const
//      QStringList &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN31QPollingFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_(
    QPollingFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->removePaths(*paths, files, directories));
}

#endif  // QT_CONFIG(filesystemwatcher)
#endif  // QT_CONFIG(filesystemwatcher)
