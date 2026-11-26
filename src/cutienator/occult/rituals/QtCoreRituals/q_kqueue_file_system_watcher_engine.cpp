//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_kqueue_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && defined(Q_OS_UNIX) && !defined(Q_OS_MACOS) && !QT_CONFIG(inotify) && (defined(Q_OS_DARWIN) || defined(Q_OS_FREEBSD) || defined(Q_OS_NETBSD) || defined(Q_OS_OPENBSD))
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_kqueue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/private/qfilesystemwatcher_kqueue_p.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qvarlengtharray.h>
#include <sys/types.h>
#include <sys/event.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <fcntl.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemwatcher_kqueue.cpp, line 50, as _ZN30QKqueueFileSystemWatcherEngineD1Ev
inline QKqueueFileSystemWatcherEngine::~QKqueueFileSystemWatcherEngine()
{
    notifier.setEnabled(false);
    close(kqfd);

    for (int id : std::as_const(pathToID))
        ::close(id < 0 ? -id : id);
}

//  from src/corelib/io/qfilesystemwatcher_kqueue.cpp, line 32, as _ZN30QKqueueFileSystemWatcherEngine6createEP7QObject
inline QKqueueFileSystemWatcherEngine *QKqueueFileSystemWatcherEngine::create(QObject *parent)
{
    int kqfd = kqueue();
    if (kqfd == -1)
        return 0;
    return new QKqueueFileSystemWatcherEngine(kqfd, parent);
}

//  from src/corelib/io/qfilesystemwatcher_kqueue.cpp, line 59, as _ZN30QKqueueFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_
inline QStringList QKqueueFileSystemWatcherEngine::addPaths(const QStringList &paths,
                                                     QStringList *files,
                                                     QStringList *directories)
{
    QStringList unhandled;
    for (const QString &path : paths) {
        auto sg = qScopeGuard([&]{unhandled.push_back(path);});
        int fd;
#if defined(O_EVTONLY)
        fd = qt_safe_open(QFile::encodeName(path), O_EVTONLY);
#else
        fd = qt_safe_open(QFile::encodeName(path), O_RDONLY);
#endif
        if (fd == -1) {
            perror("QKqueueFileSystemWatcherEngine::addPaths: open");
            continue;
        }
        if (fd >= (int)FD_SETSIZE / 2 && fd < (int)FD_SETSIZE) {
            int fddup = qt_safe_dup(fd, FD_SETSIZE);
            if (fddup != -1) {
                ::close(fd);
                fd = fddup;
            }
        }

        QT_STATBUF st;
        if (QT_FSTAT(fd, &st) == -1) {
            perror("QKqueueFileSystemWatcherEngine::addPaths: fstat");
            ::close(fd);
            continue;
        }
        int id = (S_ISDIR(st.st_mode)) ? -fd : fd;
        if (id < 0) {
            if (directories->contains(path)) {
                ::close(fd);
                continue;
            }
        } else {
            if (files->contains(path)) {
                ::close(fd);
                continue;
            }
        }

        struct kevent kev;
        EV_SET(&kev,
               fd,
               EVFILT_VNODE,
               EV_ADD | EV_ENABLE | EV_CLEAR,
               NOTE_DELETE | NOTE_WRITE | NOTE_EXTEND | NOTE_ATTRIB | NOTE_RENAME | NOTE_REVOKE,
               0,
               0);
        if (kevent(kqfd, &kev, 1, 0, 0, 0) == -1) {
            perror("QKqueueFileSystemWatcherEngine::addPaths: kevent");
            ::close(fd);
            continue;
        }

        sg.dismiss();

        if (id < 0) {
            DEBUG() << "QKqueueFileSystemWatcherEngine: added directory path" << path;
            directories->append(path);
        } else {
            DEBUG() << "QKqueueFileSystemWatcherEngine: added file path" << path;
            files->append(path);
        }

        pathToID.insert(path, id);
        idToPath.insert(id, path);
    }

    return unhandled;
}

//  from src/corelib/io/qfilesystemwatcher_kqueue.cpp, line 134, as _ZN30QKqueueFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_
inline QStringList QKqueueFileSystemWatcherEngine::removePaths(const QStringList &paths,
                                                        QStringList *files,
                                                        QStringList *directories)
{
    if (pathToID.isEmpty())
        return paths;

    QStringList unhandled;
    for (const QString &path : paths) {
        auto sg = qScopeGuard([&]{unhandled.push_back(path);});
        int id = pathToID.take(path);
        QString x = idToPath.take(id);
        if (x.isEmpty() || x != path)
            continue;

        ::close(id < 0 ? -id : id);

        sg.dismiss();

        if (id < 0)
            directories->removeAll(path);
        else
            files->removeAll(path);
    }

    return unhandled;
}

//  from src/corelib/io/qfilesystemwatcher_kqueue.cpp, line 40, as _ZN30QKqueueFileSystemWatcherEngineC1EiP7QObject
inline QKqueueFileSystemWatcherEngine::QKqueueFileSystemWatcherEngine(int kqfd, QObject *parent)
    : QFileSystemWatcherEngine(parent),
      kqfd(kqfd),
      notifier(kqfd, QSocketNotifier::Read, this)
{
    connect(&notifier, SIGNAL(activated(QSocketDescriptor)), SLOT(readFromKqueue()));

    fcntl(kqfd, F_SETFD, FD_CLOEXEC);
}
//  -----------------------------------------------------------------------

//  A QKqueueFileSystemWatcherEngine that Python can take functions over in. Every QKqueueFileSystemWatcherEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQKqueueFileSystemWatcherEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQKqueueFileSystemWatcherEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKqueueFileSystemWatcherEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKqueueFileSystemWatcherEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKqueueFileSystemWatcherEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKqueueFileSystemWatcherEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKqueueFileSystemWatcherEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQKqueueFileSystemWatcherEngine : public QKqueueFileSystemWatcherEngine {
public:
  using QKqueueFileSystemWatcherEngine::QKqueueFileSystemWatcherEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall0 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall1 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall2 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall3 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall4 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall5 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQKqueueFileSystemWatcherEngineCall6 call = reinterpret_cast<CuteQKqueueFileSystemWatcherEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QKqueueFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QKqueueFileSystemWatcherEngine10metaObjectEv(
    const QKqueueFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  void *QKqueueFileSystemWatcherEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QKqueueFileSystemWatcherEngine11qt_metacastEPKc(
    QKqueueFileSystemWatcherEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QKqueueFileSystemWatcherEngine::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QKqueueFileSystemWatcherEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QKqueueFileSystemWatcherEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QKqueueFileSystemWatcherEngine::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QKqueueFileSystemWatcherEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QKqueueFileSystemWatcherEngine::tr(s, c, n));
}

//  QKqueueFileSystemWatcherEngine::~QKqueueFileSystemWatcherEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QKqueueFileSystemWatcherEngineD1Ev(
    QKqueueFileSystemWatcherEngine *self) {
  delete self;
}

//  QKqueueFileSystemWatcherEngine
//      *QKqueueFileSystemWatcherEngine::create(QObject *parent)
extern "C" Q_DECL_EXPORT
QKqueueFileSystemWatcherEngine *ritual_ZN30QKqueueFileSystemWatcherEngine6createEP7QObject(
    QObject *parent) {
  return QKqueueFileSystemWatcherEngine::create(parent);
}

//  QStringList QKqueueFileSystemWatcherEngine::addPaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN30QKqueueFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_(
    QKqueueFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->addPaths(*paths, files, directories));
}

//  QStringList QKqueueFileSystemWatcherEngine::removePaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN30QKqueueFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_(
    QKqueueFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->removePaths(*paths, files, directories));
}

//  void QKqueueFileSystemWatcherEngine::readFromKqueue()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QKqueueFileSystemWatcherEngine14readFromKqueueEv(
    QKqueueFileSystemWatcherEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QKqueueFileSystemWatcherEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readFromKqueue()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readFromKqueue()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QKqueueFileSystemWatcherEngine::QKqueueFileSystemWatcherEngine(int kqfd,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QKqueueFileSystemWatcherEngine *ritual_ZN30QKqueueFileSystemWatcherEngineC1EiP7QObject(
    int kqfd,
    QObject *parent) {
  return new CuteQKqueueFileSystemWatcherEngine(kqfd, parent);
}

//  a Python function taken by a CuteQKqueueFileSystemWatcherEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKqueueFileSystemWatcherEngine(
    QKqueueFileSystemWatcherEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQKqueueFileSystemWatcherEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher)
#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_UNIX) && !defined(Q_OS_MACOS) && !QT_CONFIG(inotify) && (defined(Q_OS_DARWIN) || defined(Q_OS_FREEBSD) || defined(Q_OS_NETBSD) || defined(Q_OS_OPENBSD))
