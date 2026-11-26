//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher)
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QFileSystemWatcherEngine that Python can take functions over in. Every QFileSystemWatcherEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSystemWatcherEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileSystemWatcherEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileSystemWatcherEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileSystemWatcherEngine : public QFileSystemWatcherEngine {
public:
  using QFileSystemWatcherEngine::QFileSystemWatcherEngine;
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
      CuteQFileSystemWatcherEngineCall0 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall0>(taken[0]);
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
      CuteQFileSystemWatcherEngineCall1 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall1>(taken[1]);
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
      CuteQFileSystemWatcherEngineCall2 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall2>(taken[2]);
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
      CuteQFileSystemWatcherEngineCall3 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall3>(taken[3]);
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
      CuteQFileSystemWatcherEngineCall4 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall4>(taken[4]);
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
      CuteQFileSystemWatcherEngineCall5 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall5>(taken[5]);
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
      CuteQFileSystemWatcherEngineCall6 call = reinterpret_cast<CuteQFileSystemWatcherEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QFileSystemWatcherEngine10metaObjectEv(
    const QFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  void *QFileSystemWatcherEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QFileSystemWatcherEngine11qt_metacastEPKc(
    QFileSystemWatcherEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QFileSystemWatcherEngine::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QFileSystemWatcherEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QFileSystemWatcherEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QStringList QFileSystemWatcherEngine::addPaths(const QStringList &paths,
//      QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN24QFileSystemWatcherEngine8addPathsERK5QListI7QStringEPS2_S5_(
    QFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->addPaths(*paths, files, directories));
}

//  QStringList QFileSystemWatcherEngine::removePaths(const QStringList
//      &paths, QStringList *files, QStringList *directories)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN24QFileSystemWatcherEngine11removePathsERK5QListI7QStringEPS2_S5_(
    QFileSystemWatcherEngine *self,
    const QList<QString> *paths,
    QStringList *files,
    QStringList *directories) {
  return new QList<QString>(self->removePaths(*paths, files, directories));
}

//  void QFileSystemWatcherEngine::fileChanged(const QString &path, bool
//      removed)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QFileSystemWatcherEngine11fileChangedERK7QStringb(
    QFileSystemWatcherEngine *self,
    const QString *path,
    bool removed) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QFileSystemWatcherEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fileChanged(const QString &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fileChanged(const QString &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(path)),
      const_cast<void *>(static_cast<const void *>(&removed)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QFileSystemWatcherEngine::directoryChanged(const QString &path, bool
//      removed)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QFileSystemWatcherEngine16directoryChangedERK7QStringb(
    QFileSystemWatcherEngine *self,
    const QString *path,
    bool removed) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QFileSystemWatcherEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "directoryChanged(const QString &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "directoryChanged(const QString &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(path)),
      const_cast<void *>(static_cast<const void *>(&removed)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQFileSystemWatcherEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileSystemWatcherEngine(
    QFileSystemWatcherEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileSystemWatcherEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher)
#endif  // QT_CONFIG(filesystemwatcher)
