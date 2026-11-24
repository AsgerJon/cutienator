//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCore/6.12.0/QtQmlCore/private/qqmlstandardpaths_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#include <QtQmlCore/QtQmlCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlstandardpaths_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlStandardPaths that Python can take functions over in. Every QQmlStandardPaths
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlStandardPathsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlStandardPathsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStandardPathsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStandardPathsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStandardPathsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStandardPathsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlStandardPathsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlStandardPaths : public QQmlStandardPaths {
public:
  using QQmlStandardPaths::QQmlStandardPaths;
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
      CuteQQmlStandardPathsCall0 call = reinterpret_cast<CuteQQmlStandardPathsCall0>(taken[0]);
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
      CuteQQmlStandardPathsCall1 call = reinterpret_cast<CuteQQmlStandardPathsCall1>(taken[1]);
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
      CuteQQmlStandardPathsCall2 call = reinterpret_cast<CuteQQmlStandardPathsCall2>(taken[2]);
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
      CuteQQmlStandardPathsCall3 call = reinterpret_cast<CuteQQmlStandardPathsCall3>(taken[3]);
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
      CuteQQmlStandardPathsCall4 call = reinterpret_cast<CuteQQmlStandardPathsCall4>(taken[4]);
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
      CuteQQmlStandardPathsCall5 call = reinterpret_cast<CuteQQmlStandardPathsCall5>(taken[5]);
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
      CuteQQmlStandardPathsCall6 call = reinterpret_cast<CuteQQmlStandardPathsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlStandardPaths::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlStandardPaths10metaObjectEv(
    const QQmlStandardPaths *self) {
  return self->metaObject();
}

//  QString QQmlStandardPaths::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlStandardPaths2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlStandardPaths::tr(s, c, n));
}

//  void QQmlStandardPaths::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlStandardPaths22qt_qmlMarker_singletonEv(
    QQmlStandardPaths *self) {
  self->qt_qmlMarker_singleton();
}

//  const QMetaObject *QQmlStandardPaths::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN17QQmlStandardPaths20qmlExtendedNamespaceEv() {
  return QQmlStandardPaths::qmlExtendedNamespace();
}

//  void QQmlStandardPaths::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlStandardPaths30qt_qmlMarker_extendedNamespaceEv(
    QQmlStandardPaths *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQmlStandardPaths::QQmlStandardPaths(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlStandardPaths *ritual_ZN17QQmlStandardPathsC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlStandardPaths(parent);
}

//  QString QQmlStandardPaths::displayName(QStandardPaths::StandardLocation
//      type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlStandardPaths11displayNameEN14QStandardPaths16StandardLocationE(
    const QQmlStandardPaths *self,
    QStandardPaths::StandardLocation type) {
  return new QString(self->displayName(type));
}

//  QUrl QQmlStandardPaths::findExecutable(const QString &executableName,
//      const QStringList &paths) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QQmlStandardPaths14findExecutableERK7QStringRK5QListIS0_E(
    const QQmlStandardPaths *self,
    const QString *executableName,
    const QList<QString> *paths) {
  return new QUrl(self->findExecutable(*executableName, *paths));
}

//  QUrl QQmlStandardPaths::locate(QStandardPaths::StandardLocation type,
//      const QString &fileName, QStandardPaths::LocateOptions options) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QQmlStandardPaths6locateEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE(
    const QQmlStandardPaths *self,
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QUrl(
      self->locate(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}

//  QList<QUrl> QQmlStandardPaths::locateAll(QStandardPaths::StandardLocation
//      type, const QString &fileName, QStandardPaths::LocateOptions options)
//      const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK17QQmlStandardPaths9locateAllEN14QStandardPaths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE(
    const QQmlStandardPaths *self,
    QStandardPaths::StandardLocation type,
    const QString *fileName,
    int options) {
  return new QList<QUrl>(
      self->locateAll(
          type,
          *fileName,
          QFlags<QStandardPaths::LocateOption>::fromInt(options)));
}

//  QList<QUrl>
//      QQmlStandardPaths::standardLocations(QStandardPaths::StandardLocation
//      type) const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK17QQmlStandardPaths17standardLocationsEN14QStandardPaths16StandardLocationE(
    const QQmlStandardPaths *self,
    QStandardPaths::StandardLocation type) {
  return new QList<QUrl>(self->standardLocations(type));
}

//  QUrl QQmlStandardPaths::writableLocation(QStandardPaths::StandardLocation
//      type) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QQmlStandardPaths16writableLocationEN14QStandardPaths16StandardLocationE(
    const QQmlStandardPaths *self,
    QStandardPaths::StandardLocation type) {
  return new QUrl(self->writableLocation(type));
}

//  a Python function taken by a CuteQQmlStandardPaths, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlStandardPaths(
    QQmlStandardPaths *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlStandardPaths *>(self)->take(key, call);
}
