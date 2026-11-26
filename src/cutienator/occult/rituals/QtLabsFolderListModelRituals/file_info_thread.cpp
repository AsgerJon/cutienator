//  Written by dev_tooling.RitualGenerator from the records of QtLabsFolderLi
//  stModel/6.12.0/QtLabsFolderListModel/private/fileinfothread_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodelglobal_p.h>
#include <QtLabsFolderListModel/QtLabsFolderListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/fileinfothread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/fileproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsFolderListModel/private/fileinfothread_p.h>
#include <qdiriterator.h>
#include <qpointer.h>
#include <qtimer.h>
#include <QDebug>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/folderlistmodel/fileinfothread.cpp, line 225, as _ZN14FileInfoThread3runEv
inline void FileInfoThread::run()
{
    forever {
        bool updateFiles = false;
        QMutexLocker locker(&mutex);
        if (abort) {
            return;
        }
        if (currentPath.isEmpty() || !needUpdate) {
            emit statusChanged(currentPath.isEmpty() ? QQuickFolderListModel::Null : QQuickFolderListModel::Ready);
            condition.wait(&mutex);
        }

        if (abort) {
            return;
        }

        if (!currentPath.isEmpty()) {
            updateFiles = true;
            emit statusChanged(QQuickFolderListModel::Loading);
        }
        if (updateFiles)
            getFileInfos(currentPath);
        locker.unlock();
    }
}

//  from ../qtdeclarative/src/labs/folderlistmodel/fileinfothread.cpp, line 44, as _ZN14FileInfoThreadD1Ev
inline FileInfoThread::~FileInfoThread()
{
    QMutexLocker locker(&mutex);
    abort = true;
    condition.wakeOne();
    locker.unlock();
    wait();
}

//  from ../qtdeclarative/src/labs/folderlistmodel/fileinfothread.cpp, line 53, as _ZN14FileInfoThread5clearEv
inline void FileInfoThread::clear()
{
    QMutexLocker locker(&mutex);
#if QT_CONFIG(filesystemwatcher)
    watcher->removePaths(watcher->files());
    watcher->removePaths(watcher->directories());
#endif
}

//  from ../qtdeclarative/src/labs/folderlistmodel/fileinfothread.cpp, line 62, as _ZN14FileInfoThread10removePathERK7QString
inline void FileInfoThread::removePath(const QString &path)
{
    QMutexLocker locker(&mutex);
#if QT_CONFIG(filesystemwatcher)
    if (!path.startsWith(QLatin1Char(':')))
        watcher->removePath(path);
#else
    Q_UNUSED(path);
#endif
    currentPath.clear();
}

//  from ../qtdeclarative/src/labs/folderlistmodel/fileinfothread.cpp, line 364, as _ZN14FileInfoThread15findChangeRangeERK5QListI12FilePropertyERiS5_
inline void FileInfoThread::findChangeRange(const QList<FileProperty> &list, int &fromIndex, int &toIndex)
{
    if (currentFileList.size() == 0) {
        fromIndex = 0;
        toIndex = list.size();
        return;
    }

    int i;
    int listSize = list.size() < currentFileList.size() ? list.size() : currentFileList.size();
    bool changeFound = false;

    for (i=0; i < listSize; i++) {
        if (list.at(i) != currentFileList.at(i)) {
            changeFound = true;
            break;
        }
    }

    if (changeFound)
        fromIndex = i;
    else
        fromIndex = i-1;

    // For now I let the rest of the list be updated..
    toIndex = list.size() > currentFileList.size() ? list.size() - 1 : currentFileList.size() - 1;
}
//  -----------------------------------------------------------------------

//  A FileInfoThread that Python can take functions over in. Every FileInfoThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteFileInfoThreadCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteFileInfoThreadCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteFileInfoThreadCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteFileInfoThreadCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteFileInfoThreadCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteFileInfoThreadCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteFileInfoThreadCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteFileInfoThreadCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteFileInfoThread : public FileInfoThread {
public:
  using FileInfoThread::FileInfoThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void FileInfoThread::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteFileInfoThreadCall0 call = reinterpret_cast<CuteFileInfoThreadCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    FileInfoThread::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteFileInfoThreadCall1 call = reinterpret_cast<CuteFileInfoThreadCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteFileInfoThreadCall2 call = reinterpret_cast<CuteFileInfoThreadCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteFileInfoThreadCall3 call = reinterpret_cast<CuteFileInfoThreadCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteFileInfoThreadCall4 call = reinterpret_cast<CuteFileInfoThreadCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteFileInfoThreadCall5 call = reinterpret_cast<CuteFileInfoThreadCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteFileInfoThreadCall6 call = reinterpret_cast<CuteFileInfoThreadCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteFileInfoThreadCall7 call = reinterpret_cast<CuteFileInfoThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *FileInfoThread::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14FileInfoThread10metaObjectEv(
    const FileInfoThread *self) {
  return self->metaObject();
}

//  void *FileInfoThread::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14FileInfoThread11qt_metacastEPKc(
    FileInfoThread *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int FileInfoThread::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14FileInfoThread11qt_metacallEN11QMetaObject4CallEiPPv(
    FileInfoThread *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  FileInfoThread::~FileInfoThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThreadD1Ev(FileInfoThread *self) {
  delete self;
}

//  void FileInfoThread::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread5clearEv(FileInfoThread *self) {
  self->clear();
}

//  void FileInfoThread::removePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread10removePathERK7QString(
    FileInfoThread *self,
    const QString *path) {
  self->removePath(*path);
}

#if QT_CONFIG(filesystemwatcher)
//  void FileInfoThread::dirChanged(const QString &directoryPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread10dirChangedERK7QString(
    FileInfoThread *self,
    const QString *directoryPath) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "FileInfoThread")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dirChanged(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dirChanged(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(directoryPath)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(filesystemwatcher)

#if QT_CONFIG(filesystemwatcher)
//  void FileInfoThread::updateFile(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread10updateFileERK7QString(
    FileInfoThread *self,
    const QString *path) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "FileInfoThread")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateFile(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateFile(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(path)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(filesystemwatcher)

//  void FileInfoThread::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread3runEv(FileInfoThread *self) {
  self->run();
}

//  void FileInfoThread::findChangeRange(const QList<FileProperty> &list, int
//      &fromIndex, int &toIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN14FileInfoThread15findChangeRangeERK5QListI12FilePropertyERiS5_(
    FileInfoThread *self,
    const QList<FileProperty> *list,
    int *fromIndex,
    int *toIndex) {
  self->findChangeRange(*list, *fromIndex, *toIndex);
}

//  a Python function taken by a CuteFileInfoThread, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_FileInfoThread(
    FileInfoThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteFileInfoThread *>(self)->take(key, call);
}
