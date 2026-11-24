//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfilesystemwatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFileSystemWatcher that Python can take functions over in. Every QFileSystemWatcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSystemWatcherCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSystemWatcherCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileSystemWatcher : public QFileSystemWatcher {
public:
  using QFileSystemWatcher::QFileSystemWatcher;
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
      CuteQFileSystemWatcherCall0 call = reinterpret_cast<CuteQFileSystemWatcherCall0>(taken[0]);
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
      CuteQFileSystemWatcherCall1 call = reinterpret_cast<CuteQFileSystemWatcherCall1>(taken[1]);
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
      CuteQFileSystemWatcherCall2 call = reinterpret_cast<CuteQFileSystemWatcherCall2>(taken[2]);
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
      CuteQFileSystemWatcherCall3 call = reinterpret_cast<CuteQFileSystemWatcherCall3>(taken[3]);
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
      CuteQFileSystemWatcherCall4 call = reinterpret_cast<CuteQFileSystemWatcherCall4>(taken[4]);
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
      CuteQFileSystemWatcherCall5 call = reinterpret_cast<CuteQFileSystemWatcherCall5>(taken[5]);
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
      CuteQFileSystemWatcherCall6 call = reinterpret_cast<CuteQFileSystemWatcherCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileSystemWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QFileSystemWatcher10metaObjectEv(
    const QFileSystemWatcher *self) {
  return self->metaObject();
}

//  QString QFileSystemWatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFileSystemWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSystemWatcher::tr(s, c, n));
}

//  QFileSystemWatcherPrivate *QFileSystemWatcher::d_func()
extern "C" Q_DECL_EXPORT
QFileSystemWatcherPrivate *ritual_ZN18QFileSystemWatcher6d_funcEv(
    QFileSystemWatcher *self) {
  return self->d_func();
}

//  const QFileSystemWatcherPrivate *QFileSystemWatcher::d_func() const
extern "C" Q_DECL_EXPORT
const QFileSystemWatcherPrivate *ritual_ZNK18QFileSystemWatcher6d_funcEv(
    const QFileSystemWatcher *self) {
  return self->d_func();
}

//  QFileSystemWatcher::QFileSystemWatcher(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSystemWatcher *ritual_ZN18QFileSystemWatcherC1EP7QObject(
    QObject *parent) {
  return new CuteQFileSystemWatcher(parent);
}

//  QFileSystemWatcher::QFileSystemWatcher(const QStringList &paths, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QFileSystemWatcher *ritual_ZN18QFileSystemWatcherC1ERK5QListI7QStringEP7QObject(
    const QList<QString> *paths,
    QObject *parent) {
  return new CuteQFileSystemWatcher(*paths, parent);
}

//  QFileSystemWatcher::~QFileSystemWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileSystemWatcherD1Ev(QFileSystemWatcher *self) {
  delete self;
}

//  bool QFileSystemWatcher::addPath(const QString &file)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileSystemWatcher7addPathERK7QString(
    QFileSystemWatcher *self,
    const QString *file) {
  return self->addPath(*file);
}

//  QStringList QFileSystemWatcher::addPaths(const QStringList &files)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18QFileSystemWatcher8addPathsERK5QListI7QStringE(
    QFileSystemWatcher *self,
    const QList<QString> *files) {
  return new QList<QString>(self->addPaths(*files));
}

//  bool QFileSystemWatcher::removePath(const QString &file)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileSystemWatcher10removePathERK7QString(
    QFileSystemWatcher *self,
    const QString *file) {
  return self->removePath(*file);
}

//  QStringList QFileSystemWatcher::removePaths(const QStringList &files)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18QFileSystemWatcher11removePathsERK5QListI7QStringE(
    QFileSystemWatcher *self,
    const QList<QString> *files) {
  return new QList<QString>(self->removePaths(*files));
}

//  QStringList QFileSystemWatcher::files() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileSystemWatcher5filesEv(
    const QFileSystemWatcher *self) {
  return new QList<QString>(self->files());
}

//  QStringList QFileSystemWatcher::directories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileSystemWatcher11directoriesEv(
    const QFileSystemWatcher *self) {
  return new QList<QString>(self->directories());
}

//  a Python function taken by a CuteQFileSystemWatcher, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSystemWatcher(
    QFileSystemWatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSystemWatcher *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher)
