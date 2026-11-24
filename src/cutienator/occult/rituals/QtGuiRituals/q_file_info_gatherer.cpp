//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(filesystemmodel)
#if QT_CONFIG(filesystemmodel)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfileinfogatherer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFileInfoGatherer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileInfoGatherer : QFileInfoGatherer {
  using QFileInfoGatherer::event;
};

//  A QFileInfoGatherer that Python can take functions over in. Every QFileInfoGatherer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
typedef bool (*CuteQFileInfoGathererCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
typedef void (*CuteQFileInfoGathererCall1)(const void *, int *);
#endif  // QT_CONFIG(filesystemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileInfoGathererCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileInfoGathererCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileInfoGathererCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileInfoGathererCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileInfoGathererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileInfoGathererCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileInfoGatherer : public QFileInfoGatherer {
public:
  using QFileInfoGatherer::QFileInfoGatherer;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filesystemmodel)
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(filesystemmodel)
  //  bool QFileInfoGatherer::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileInfoGathererCall0 call = reinterpret_cast<CuteQFileInfoGathererCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QFileInfoGatherer::event(event);
  }
#endif  // QT_CONFIG(filesystemmodel)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(filesystemmodel)
  //  void QFileInfoGatherer::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileInfoGathererCall1 call = reinterpret_cast<CuteQFileInfoGathererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QFileInfoGatherer::run();
  }
#endif  // QT_CONFIG(filesystemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileInfoGathererCall2 call = reinterpret_cast<CuteQFileInfoGathererCall2>(taken[2]);
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
      CuteQFileInfoGathererCall3 call = reinterpret_cast<CuteQFileInfoGathererCall3>(taken[3]);
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
      CuteQFileInfoGathererCall4 call = reinterpret_cast<CuteQFileInfoGathererCall4>(taken[4]);
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
      CuteQFileInfoGathererCall5 call = reinterpret_cast<CuteQFileInfoGathererCall5>(taken[5]);
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
      CuteQFileInfoGathererCall6 call = reinterpret_cast<CuteQFileInfoGathererCall6>(taken[6]);
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
      CuteQFileInfoGathererCall7 call = reinterpret_cast<CuteQFileInfoGathererCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileInfoGatherer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QFileInfoGatherer10metaObjectEv(
    const QFileInfoGatherer *self) {
  return self->metaObject();
}

//  QString QFileInfoGatherer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFileInfoGatherer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileInfoGatherer::tr(s, c, n));
}

//  QFileInfoGatherer::QFileInfoGatherer(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileInfoGatherer *ritual_ZN17QFileInfoGathererC1EP7QObject(
    QObject *parent) {
  return new CuteQFileInfoGatherer(parent);
}

//  QFileInfoGatherer::~QFileInfoGatherer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGathererD1Ev(QFileInfoGatherer *self) {
  delete self;
}

//  QStringList QFileInfoGatherer::watchedFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QFileInfoGatherer12watchedFilesEv(
    const QFileInfoGatherer *self) {
  return new QList<QString>(self->watchedFiles());
}

//  QStringList QFileInfoGatherer::watchedDirectories() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QFileInfoGatherer18watchedDirectoriesEv(
    const QFileInfoGatherer *self) {
  return new QList<QString>(self->watchedDirectories());
}

//  void QFileInfoGatherer::watchPaths(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer10watchPathsERK5QListI7QStringE(
    QFileInfoGatherer *self,
    const QList<QString> *paths) {
  self->watchPaths(*paths);
}

//  void QFileInfoGatherer::unwatchPaths(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer12unwatchPathsERK5QListI7QStringE(
    QFileInfoGatherer *self,
    const QList<QString> *paths) {
  self->unwatchPaths(*paths);
}

//  bool QFileInfoGatherer::isWatching() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QFileInfoGatherer10isWatchingEv(
    const QFileInfoGatherer *self) {
  return self->isWatching();
}

//  void QFileInfoGatherer::setWatching(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer11setWatchingEb(
    QFileInfoGatherer *self,
    bool v) {
  self->setWatching(v);
}

//  void QFileInfoGatherer::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer5clearEv(QFileInfoGatherer *self) {
  self->clear();
}

//  void QFileInfoGatherer::removePath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer10removePathERK7QString(
    QFileInfoGatherer *self,
    const QString *path) {
  self->removePath(*path);
}

//  QExtendedInformation QFileInfoGatherer::getInfo(const QFileInfo &info)
//      const
extern "C" Q_DECL_EXPORT
QExtendedInformation *ritual_ZNK17QFileInfoGatherer7getInfoERK9QFileInfo(
    const QFileInfoGatherer *self,
    const QFileInfo *info) {
  return new QExtendedInformation(self->getInfo(*info));
}

//  QAbstractFileIconProvider *QFileInfoGatherer::iconProvider() const
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZNK17QFileInfoGatherer12iconProviderEv(
    const QFileInfoGatherer *self) {
  return self->iconProvider();
}

//  bool QFileInfoGatherer::resolveSymlinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QFileInfoGatherer15resolveSymlinksEv(
    const QFileInfoGatherer *self) {
  return self->resolveSymlinks();
}

//  void QFileInfoGatherer::requestAbort()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer12requestAbortEv(QFileInfoGatherer *self) {
  self->requestAbort();
}

//  void QFileInfoGatherer::list(const QString &directoryPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer4listERK7QString(
    QFileInfoGatherer *self,
    const QString *directoryPath) {
  self->list(*directoryPath);
}

//  void QFileInfoGatherer::fetchExtendedInformation(const QString &path,
//      const QStringList &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer24fetchExtendedInformationERK7QStringRK5QListIS0_E(
    QFileInfoGatherer *self,
    const QString *path,
    const QList<QString> *files) {
  self->fetchExtendedInformation(*path, *files);
}

//  void QFileInfoGatherer::updateFile(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer10updateFileERK7QString(
    QFileInfoGatherer *self,
    const QString *path) {
  self->updateFile(*path);
}

//  void QFileInfoGatherer::setResolveSymlinks(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer18setResolveSymlinksEb(
    QFileInfoGatherer *self,
    bool enable) {
  self->setResolveSymlinks(enable);
}

//  void QFileInfoGatherer::setIconProvider(QAbstractFileIconProvider
//      *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer15setIconProviderEP25QAbstractFileIconProvider(
    QFileInfoGatherer *self,
    QAbstractFileIconProvider *provider) {
  self->setIconProvider(provider);
}

//  void QFileInfoGatherer::driveAdded()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer10driveAddedEv(QFileInfoGatherer *self) {
  self->driveAdded();
}

//  void QFileInfoGatherer::driveRemoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer12driveRemovedEv(QFileInfoGatherer *self) {
  self->driveRemoved();
}

//  bool QFileInfoGatherer::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QFileInfoGatherer5eventEP6QEvent(
    QFileInfoGatherer *self,
    QEvent *event) {
  return self->event(event);
}

//  void QFileInfoGatherer::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer3runEv(QFileInfoGatherer *self) {
  self->run();
}

//  void QFileInfoGatherer::getFileInfos(const QString &path, const
//      QStringList &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer12getFileInfosERK7QStringRK5QListIS0_E(
    QFileInfoGatherer *self,
    const QString *path,
    const QList<QString> *files) {
  self->getFileInfos(*path, *files);
}

//  void QFileInfoGatherer::createWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileInfoGatherer13createWatcherEv(QFileInfoGatherer *self) {
  self->createWatcher();
}

//  a Python function taken by a CuteQFileInfoGatherer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileInfoGatherer(
    QFileInfoGatherer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileInfoGatherer *>(self)->take(key, call);
}

//  bool QFileInfoGatherer::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QFileInfoGatherer5eventEP6QEvent(
    QFileInfoGatherer *self,
    QEvent *event) {
  return static_cast<OwnQFileInfoGatherer *>(self)->OwnQFileInfoGatherer::event(
      event);
}

//  void QFileInfoGatherer::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QFileInfoGatherer3runEv(QFileInfoGatherer *self) {
  self->QFileInfoGatherer::run();
}

#endif  // QT_CONFIG(filesystemmodel)
#endif  // QT_CONFIG(filesystemmodel)
