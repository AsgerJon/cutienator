//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_polling_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfilesystemwatcher_polling_p.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qscopeguard.h>
#include <chrono>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystemwatcher_polling.cpp, line 67, as _ZN31QPollingFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_
inline QStringList QPollingFileSystemWatcherEngine::removePaths(const QStringList &paths,
                                                         QStringList *files,
                                                         QStringList *directories)
{
    QStringList unhandled;
    for (const QString &path : paths) {
        if (this->directories.remove(path)) {
            directories->removeAll(path);
        } else if (this->files.remove(path)) {
            files->removeAll(path);
        } else {
            unhandled.push_back(path);
        }
    }

    if (this->files.isEmpty() &&
        this->directories.isEmpty()) {
        timer.stop();
    }

    return unhandled;
}

//  from src/corelib/io/qfilesystemwatcher_polling.cpp, line 90, as _ZN31QPollingFileSystemWatcherEngine10timerEventEP11QTimerEvent
inline void QPollingFileSystemWatcherEngine::timerEvent(QTimerEvent *e)
{
    if (e->id() != timer.id())
        return QFileSystemWatcherEngine::timerEvent(e);

    for (auto it = files.begin(), end = files.end(); it != end; /*erasing*/) {
        QString path = it.key();
        QFileInfo fi(path);
        if (!fi.exists()) {
            it = files.erase(it);
            emit fileChanged(path, true);
            continue;
        } else if (it.value() != fi) {
            it.value() = fi;
            emit fileChanged(path, false);
        }
        ++it;
    }

    for (auto it = directories.begin(), end = directories.end(); it != end; /*erasing*/) {
        QString path = it.key();
        QFileInfo fi(path);
        if (!path.endsWith(u'/'))
            fi = QFileInfo(path + u'/');
        if (!fi.exists()) {
            it = directories.erase(it);
            emit directoryChanged(path, true);
            continue;
        } else if (it.value() != fi) {
            fi.refresh();
            if (!fi.exists()) {
                it = directories.erase(it);
                emit directoryChanged(path, true);
                continue;
            } else {
                it.value() = fi;
                emit directoryChanged(path, false);
            }
        }
        ++it;
    }
}
//  -----------------------------------------------------------------------

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

//  void QPollingFileSystemWatcherEngine::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QPollingFileSystemWatcherEngine10timerEventEP11QTimerEvent(
    QPollingFileSystemWatcherEngine *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

#endif  // QT_CONFIG(filesystemwatcher)
#endif  // QT_CONFIG(filesystemwatcher)
