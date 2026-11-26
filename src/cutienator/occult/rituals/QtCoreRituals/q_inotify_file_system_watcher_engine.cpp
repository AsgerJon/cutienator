//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_inotify_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QInotifyFileSystemWatcherEngine' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 3 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && QT_CONFIG(inotify) && defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_inotify_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/private/qfilesystemwatcher_inotify_p.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/private/qsystemerror_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qvarlengtharray.h>
#if defined(Q_OS_LINUX)
#include <sys/syscall.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <fcntl.h>
#endif
#if defined(QT_NO_INOTIFY)
#include <linux/types.h>
#else /* QT_NO_INOTIFY */
#include <sys/inotify.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 393, as local:qfilesystemwatcher_inotify.cpp:find_last_in_equal_range
inline template <typename Hash, typename Key>
typename Hash::const_iterator
find_last_in_equal_range(const Hash &c, const Key &key)
{
    // find c.equal_range(key).second - 1 without backwards iteration:
    auto i = c.find(key);
    const auto end = c.cend();
    if (i == end)
        return end;
    decltype(i) prev;
    do {
        prev = i;
        ++i;
    } while (i != end && i.key() == key);
    return prev;
}

//  from QtCore__QInotifyFileSystemWatcherEngine.cpp, line 1, as moc:QInotifyFileSystemWatcherEngine
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t {};
} // unnamed namespace

template <> constexpr inline auto QInotifyFileSystemWatcherEngine::qt_create_metaobjectdata<qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QInotifyFileSystemWatcherEngine",
        "readFromInotify",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'readFromInotify'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QInotifyFileSystemWatcherEngine, qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QInotifyFileSystemWatcherEngine::staticMetaObject = { {
    QMetaObject::SuperData::link<QFileSystemWatcherEngine::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>.metaTypes,
    nullptr
} };

void QInotifyFileSystemWatcherEngine::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QInotifyFileSystemWatcherEngine *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->readFromInotify(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QInotifyFileSystemWatcherEngine::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QInotifyFileSystemWatcherEngine::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QInotifyFileSystemWatcherEngineE_t>.strings))
        return static_cast<void*>(this);
    return QFileSystemWatcherEngine::qt_metacast(_clname);
}

int QInotifyFileSystemWatcherEngine::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QFileSystemWatcherEngine::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 290, as _ZN31QInotifyFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_
inline QStringList QInotifyFileSystemWatcherEngine::removePaths(const QStringList &paths,
                                                         QStringList *files,
                                                         QStringList *directories)
{
    QStringList unhandled;
    for (const QString &path : paths) {
        int id = pathToID.take(path);

        auto sg = qScopeGuard([&]{ unhandled.push_back(path); });

        // Multiple paths could be associated to the same watch descriptor
        // when a file is moved and added with the new name.
        // So we should find and delete the correct one by using
        // both id and path
        auto path_range = idToPath.equal_range(id);
        auto path_it = std::find(path_range.first, path_range.second, path);
        if (path_it == idToPath.end())
            continue;

        const ssize_t num_elements = std::distance(path_range.first, path_range.second);
        idToPath.erase(path_it);

        // If there was only one path associated to the given id we should remove the watch
        if (num_elements == 1) {
            int wd = id < 0 ? -id : id;
            inotify_rm_watch(inotifyFd, wd);
        }

        sg.dismiss();

        if (id < 0) {
            directories->removeAll(path);
        } else {
            files->removeAll(path);
        }
    }

    return unhandled;
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 330, as _ZN31QInotifyFileSystemWatcherEngine15readFromInotifyEv
inline void QInotifyFileSystemWatcherEngine::readFromInotify()
{
    // qDebug("QInotifyFileSystemWatcherEngine::readFromInotify");

    int buffSize = 0;
    if (ioctl(inotifyFd, FIONREAD, (char *) &buffSize) == -1 || buffSize == 0)
        return;

    QVarLengthArray<char, 4096> buffer(buffSize);
    buffSize = int(read(inotifyFd, buffer.data(), buffSize));
    char *at = buffer.data();
    char * const end = at + buffSize;

    QHash<int, inotify_event *> eventForId;
    while (at < end) {
        inotify_event *event = reinterpret_cast<inotify_event *>(at);

        if (eventForId.contains(event->wd))
            eventForId[event->wd]->mask |= event->mask;
        else
            eventForId.insert(event->wd, event);

        at += sizeof(inotify_event) + event->len;
    }

    QHash<int, inotify_event *>::const_iterator it = eventForId.constBegin();
    while (it != eventForId.constEnd()) {
        const inotify_event &event = **it;
        ++it;

        // qDebug() << "inotify event, wd" << event.wd << "mask" << Qt::hex << event.mask;

        int id = event.wd;
        QString path = getPathFromID(id);
        if (path.isEmpty()) {
            // perhaps a directory?
            id = -id;
            path = getPathFromID(id);
            if (path.isEmpty())
                continue;
        }

        // qDebug() << "event for path" << path;

        if ((event.mask & (IN_DELETE_SELF | IN_MOVE_SELF | IN_UNMOUNT)) != 0) {
            pathToID.remove(path);
            idToPath.remove(id, getPathFromID(id));
            if (!idToPath.contains(id))
                inotify_rm_watch(inotifyFd, event.wd);

            if (id < 0)
                emit directoryChanged(path, true);
            else
                emit fileChanged(path, true);
        } else {
            if (id < 0)
                emit directoryChanged(path, false);
            else
                emit fileChanged(path, false);
        }
    }
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 234, as _ZN31QInotifyFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_
inline QStringList QInotifyFileSystemWatcherEngine::addPaths(const QStringList &paths,
                                                      QStringList *files,
                                                      QStringList *directories)
{
    QStringList unhandled;
    for (const QString &path : paths) {
        QFileInfo fi(path);
        bool isDir = fi.isDir();
        auto sg = qScopeGuard([&]{ unhandled.push_back(path); });
        if (isDir) {
            if (directories->contains(path))
                continue;
        } else {
            if (files->contains(path))
                continue;
        }

        int wd = inotify_add_watch(inotifyFd,
                                   QFile::encodeName(path),
                                   (isDir
                                    ? (0
                                       | IN_ATTRIB
                                       | IN_MOVE
                                       | IN_CREATE
                                       | IN_DELETE
                                       | IN_DELETE_SELF
                                       )
                                    : (0
                                       | IN_ATTRIB
                                       | IN_MODIFY
                                       | IN_MOVE
                                       | IN_MOVE_SELF
                                       | IN_DELETE_SELF
                                       )));
        if (wd < 0) {
            if (errno != ENOENT)
                qErrnoWarning("inotify_add_watch(%ls) failed:", path.constData());
            continue;
        }

        sg.dismiss();

        int id = isDir ? -wd : wd;
        if (id < 0) {
            directories->append(path);
        } else {
            files->append(path);
        }

        pathToID.insert(path, id);
        idToPath.insert(id, path);
    }

    return unhandled;
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 225, as _ZN31QInotifyFileSystemWatcherEngineD1Ev
inline QInotifyFileSystemWatcherEngine::~QInotifyFileSystemWatcherEngine()
{
    notifier.setEnabled(false);
    for (int id : std::as_const(pathToID))
        inotify_rm_watch(inotifyFd, id < 0 ? -id : id);

    ::close(inotifyFd);
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 201, as _ZN31QInotifyFileSystemWatcherEngine6createEP7QObject
inline QInotifyFileSystemWatcherEngine *QInotifyFileSystemWatcherEngine::create(QObject *parent)
{
    int fd = -1;
#if defined(IN_CLOEXEC)
    fd = inotify_init1(IN_CLOEXEC);
#endif
    if (fd == -1) {
        fd = inotify_init();
        if (fd == -1)
            return nullptr;
    }
    return new QInotifyFileSystemWatcherEngine(fd, parent);
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 410, as _ZNK31QInotifyFileSystemWatcherEngine13getPathFromIDEi
inline QString QInotifyFileSystemWatcherEngine::getPathFromID(int id) const
{
    auto i = find_last_in_equal_range(idToPath, id);
    return i == idToPath.cend() ? QString() : i.value() ;
}

//  from src/corelib/io/qfilesystemwatcher_inotify.cpp, line 215, as _ZN31QInotifyFileSystemWatcherEngineC1EiP7QObject
inline QInotifyFileSystemWatcherEngine::QInotifyFileSystemWatcherEngine(int fd, QObject *parent)
    : QFileSystemWatcherEngine(parent),
      inotifyFd(fd),
      notifier(fd, QSocketNotifier::Read, this)
{
    fcntl(inotifyFd, F_SETFD, FD_CLOEXEC);
    QObject::connect(&notifier, &QSocketNotifier::activated,
                     this, &QInotifyFileSystemWatcherEngine::readFromInotify);
}
//  -----------------------------------------------------------------------

//  A QInotifyFileSystemWatcherEngine that Python can take functions over in. Every QInotifyFileSystemWatcherEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInotifyFileSystemWatcherEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQInotifyFileSystemWatcherEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInotifyFileSystemWatcherEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInotifyFileSystemWatcherEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInotifyFileSystemWatcherEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInotifyFileSystemWatcherEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQInotifyFileSystemWatcherEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQInotifyFileSystemWatcherEngine : public QInotifyFileSystemWatcherEngine {
public:
  using QInotifyFileSystemWatcherEngine::QInotifyFileSystemWatcherEngine;
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
      CuteQInotifyFileSystemWatcherEngineCall0 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall0>(taken[0]);
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
      CuteQInotifyFileSystemWatcherEngineCall1 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall1>(taken[1]);
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
      CuteQInotifyFileSystemWatcherEngineCall2 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall2>(taken[2]);
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
      CuteQInotifyFileSystemWatcherEngineCall3 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall3>(taken[3]);
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
      CuteQInotifyFileSystemWatcherEngineCall4 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall4>(taken[4]);
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
      CuteQInotifyFileSystemWatcherEngineCall5 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall5>(taken[5]);
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
      CuteQInotifyFileSystemWatcherEngineCall6 call = reinterpret_cast<CuteQInotifyFileSystemWatcherEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QInotifyFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QInotifyFileSystemWatcherEngine10metaObjectEv(
    const QInotifyFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  void *QInotifyFileSystemWatcherEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QInotifyFileSystemWatcherEngine11qt_metacastEPKc(
    QInotifyFileSystemWatcherEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QInotifyFileSystemWatcherEngine::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QInotifyFileSystemWatcherEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QInotifyFileSystemWatcherEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QInotifyFileSystemWatcherEngine::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QInotifyFileSystemWatcherEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInotifyFileSystemWatcherEngine::tr(s, c, n));
}

//  QInotifyFileSystemWatcherEngine::~QInotifyFileSystemWatcherEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QInotifyFileSystemWatcherEngineD1Ev(
    QInotifyFileSystemWatcherEngine *self) {
  delete self;
}

//  QInotifyFileSystemWatcherEngine
//      *QInotifyFileSystemWatcherEngine::create(QObject *parent)
extern "C" Q_DECL_EXPORT
QInotifyFileSystemWatcherEngine *ritual_ZN31QInotifyFileSystemWatcherEngine6createEP7QObject(
    QObject *parent) {
  return QInotifyFileSystemWatcherEngine::create(parent);
}

//  QStringList QInotifyFileSystemWatcherEngine::addPaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN31QInotifyFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_(
    QInotifyFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->addPaths(*paths, files, directories));
}

//  QStringList QInotifyFileSystemWatcherEngine::removePaths(const
//      QStringList &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN31QInotifyFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_(
    QInotifyFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->removePaths(*paths, files, directories));
}

//  void QInotifyFileSystemWatcherEngine::readFromInotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QInotifyFileSystemWatcherEngine15readFromInotifyEv(
    QInotifyFileSystemWatcherEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QInotifyFileSystemWatcherEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readFromInotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readFromInotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QString QInotifyFileSystemWatcherEngine::getPathFromID(int id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QInotifyFileSystemWatcherEngine13getPathFromIDEi(
    const QInotifyFileSystemWatcherEngine *self,
    int id) {
  return new QString(self->getPathFromID(id));
}

//  QInotifyFileSystemWatcherEngine::QInotifyFileSystemWatcherEngine(int fd,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QInotifyFileSystemWatcherEngine *ritual_ZN31QInotifyFileSystemWatcherEngineC1EiP7QObject(
    int fd,
    QObject *parent) {
  return new CuteQInotifyFileSystemWatcherEngine(fd, parent);
}

//  a Python function taken by a CuteQInotifyFileSystemWatcherEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInotifyFileSystemWatcherEngine(
    QInotifyFileSystemWatcherEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInotifyFileSystemWatcherEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher)
#endif  // QT_CONFIG(filesystemwatcher) && QT_CONFIG(inotify) && defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
