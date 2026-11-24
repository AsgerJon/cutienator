//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusservicewatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS) && !defined(QT_NO_QOBJECT)
#include <QtDBus/qdbusservicewatcher.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDBusServiceWatcher that Python can take functions over in. Every QDBusServiceWatcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusServiceWatcherCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusServiceWatcherCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServiceWatcherCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServiceWatcherCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServiceWatcherCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServiceWatcherCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServiceWatcherCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusServiceWatcher : public QDBusServiceWatcher {
public:
  using QDBusServiceWatcher::QDBusServiceWatcher;
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
      CuteQDBusServiceWatcherCall0 call = reinterpret_cast<CuteQDBusServiceWatcherCall0>(taken[0]);
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
      CuteQDBusServiceWatcherCall1 call = reinterpret_cast<CuteQDBusServiceWatcherCall1>(taken[1]);
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
      CuteQDBusServiceWatcherCall2 call = reinterpret_cast<CuteQDBusServiceWatcherCall2>(taken[2]);
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
      CuteQDBusServiceWatcherCall3 call = reinterpret_cast<CuteQDBusServiceWatcherCall3>(taken[3]);
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
      CuteQDBusServiceWatcherCall4 call = reinterpret_cast<CuteQDBusServiceWatcherCall4>(taken[4]);
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
      CuteQDBusServiceWatcherCall5 call = reinterpret_cast<CuteQDBusServiceWatcherCall5>(taken[5]);
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
      CuteQDBusServiceWatcherCall6 call = reinterpret_cast<CuteQDBusServiceWatcherCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusServiceWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QDBusServiceWatcher10metaObjectEv(
    const QDBusServiceWatcher *self) {
  return self->metaObject();
}

//  QString QDBusServiceWatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QDBusServiceWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusServiceWatcher::tr(s, c, n));
}

//  QDBusServiceWatcher::QDBusServiceWatcher(QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusServiceWatcher *ritual_ZN19QDBusServiceWatcherC1EP7QObject(
    QObject *parent) {
  return new CuteQDBusServiceWatcher(parent);
}

//  QDBusServiceWatcher::QDBusServiceWatcher(const QString &service, const
//      QDBusConnection &connection, WatchMode watchMode, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusServiceWatcher *ritual_ZN19QDBusServiceWatcherC1ERK7QStringRK15QDBusConnection6QFlagsINS_13WatchModeFlagEEP7QObject(
    const QString *service,
    const QDBusConnection *connection,
    int watchMode,
    QObject *parent) {
  return new CuteQDBusServiceWatcher(
      *service,
      *connection,
      QFlags<QDBusServiceWatcher::WatchModeFlag>::fromInt(watchMode),
      parent);
}

//  QDBusServiceWatcher::~QDBusServiceWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusServiceWatcherD1Ev(QDBusServiceWatcher *self) {
  delete self;
}

//  QStringList QDBusServiceWatcher::watchedServices() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QDBusServiceWatcher15watchedServicesEv(
    const QDBusServiceWatcher *self) {
  return new QList<QString>(self->watchedServices());
}

//  void QDBusServiceWatcher::setWatchedServices(const QStringList &services)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusServiceWatcher18setWatchedServicesERK5QListI7QStringE(
    QDBusServiceWatcher *self,
    const QList<QString> *services) {
  self->setWatchedServices(*services);
}

//  void QDBusServiceWatcher::addWatchedService(const QString &newService)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusServiceWatcher17addWatchedServiceERK7QString(
    QDBusServiceWatcher *self,
    const QString *newService) {
  self->addWatchedService(*newService);
}

//  bool QDBusServiceWatcher::removeWatchedService(const QString &service)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QDBusServiceWatcher20removeWatchedServiceERK7QString(
    QDBusServiceWatcher *self,
    const QString *service) {
  return self->removeWatchedService(*service);
}

//  WatchMode QDBusServiceWatcher::watchMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDBusServiceWatcher9watchModeEv(
    const QDBusServiceWatcher *self) {
  return static_cast<int>(self->watchMode().toInt());
}

//  void QDBusServiceWatcher::setWatchMode(WatchMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusServiceWatcher12setWatchModeE6QFlagsINS_13WatchModeFlagEE(
    QDBusServiceWatcher *self,
    int mode) {
  self->setWatchMode(
      QFlags<QDBusServiceWatcher::WatchModeFlag>::fromInt(mode));
}

//  QDBusConnection QDBusServiceWatcher::connection() const
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZNK19QDBusServiceWatcher10connectionEv(
    const QDBusServiceWatcher *self) {
  return new QDBusConnection(self->connection());
}

//  void QDBusServiceWatcher::setConnection(const QDBusConnection
//      &connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusServiceWatcher13setConnectionERK15QDBusConnection(
    QDBusServiceWatcher *self,
    const QDBusConnection *connection) {
  self->setConnection(*connection);
}

//  a Python function taken by a CuteQDBusServiceWatcher, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusServiceWatcher(
    QDBusServiceWatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusServiceWatcher *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS) && !defined(QT_NO_QOBJECT)
