//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineextensionmanager.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#if QT_CONFIG(webengine_extensions)
#include <QtWebEngineCore/qwebengineextensionmanager.h>
#include <QtCore/qstring.h>
#include <QtWebEngineCore/qwebengineextensioninfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWebEngineExtensionManager may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWebEngineExtensionManager : QWebEngineExtensionManager {
  using QWebEngineExtensionManager::event;
};

//  A QWebEngineExtensionManager that Python can take functions over in. Every QWebEngineExtensionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(webengine_extensions)
typedef bool (*CuteQWebEngineExtensionManagerCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(webengine_extensions)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineExtensionManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineExtensionManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineExtensionManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineExtensionManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineExtensionManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineExtensionManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineExtensionManager : public QWebEngineExtensionManager {
public:
  using QWebEngineExtensionManager::QWebEngineExtensionManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(webengine_extensions)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(webengine_extensions)
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
#if QT_CONFIG(webengine_extensions)
  //  bool QWebEngineExtensionManager::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineExtensionManagerCall0 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QWebEngineExtensionManager::event(e);
  }
#endif  // QT_CONFIG(webengine_extensions)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineExtensionManagerCall1 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall1>(taken[1]);
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
      CuteQWebEngineExtensionManagerCall2 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall2>(taken[2]);
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
      CuteQWebEngineExtensionManagerCall3 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall3>(taken[3]);
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
      CuteQWebEngineExtensionManagerCall4 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall4>(taken[4]);
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
      CuteQWebEngineExtensionManagerCall5 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall5>(taken[5]);
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
      CuteQWebEngineExtensionManagerCall6 call = reinterpret_cast<CuteQWebEngineExtensionManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineExtensionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWebEngineExtensionManager10metaObjectEv(
    const QWebEngineExtensionManager *self) {
  return self->metaObject();
}

//  void *QWebEngineExtensionManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWebEngineExtensionManager11qt_metacastEPKc(
    QWebEngineExtensionManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineExtensionManager::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWebEngineExtensionManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineExtensionManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineExtensionManager::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWebEngineExtensionManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineExtensionManager::tr(s, c, n));
}

//  QWebEngineExtensionManager::~QWebEngineExtensionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManagerD1Ev(
    QWebEngineExtensionManager *self) {
  delete self;
}

//  void QWebEngineExtensionManager::loadExtension(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager13loadExtensionERK7QString(
    QWebEngineExtensionManager *self,
    const QString *path) {
  self->loadExtension(*path);
}

//  void QWebEngineExtensionManager::installExtension(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager16installExtensionERK7QString(
    QWebEngineExtensionManager *self,
    const QString *path) {
  self->installExtension(*path);
}

//  void QWebEngineExtensionManager::unloadExtension(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager15unloadExtensionERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->unloadExtension(*extension);
}

//  void QWebEngineExtensionManager::uninstallExtension(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager18uninstallExtensionERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->uninstallExtension(*extension);
}

//  void QWebEngineExtensionManager::setExtensionEnabled(const
//      QWebEngineExtensionInfo &extension, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager19setExtensionEnabledERK23QWebEngineExtensionInfob(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension,
    bool enabled) {
  self->setExtensionEnabled(*extension, enabled);
}

//  QString QWebEngineExtensionManager::installPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebEngineExtensionManager11installPathEv(
    const QWebEngineExtensionManager *self) {
  return new QString(self->installPath());
}

//  QList<QWebEngineExtensionInfo> QWebEngineExtensionManager::extensions()
//      const
extern "C" Q_DECL_EXPORT
QList<QWebEngineExtensionInfo> *ritual_ZNK26QWebEngineExtensionManager10extensionsEv(
    const QWebEngineExtensionManager *self) {
  return new QList<QWebEngineExtensionInfo>(self->extensions());
}

//  void QWebEngineExtensionManager::loadFinished(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager12loadFinishedERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->loadFinished(*extension);
}

//  void QWebEngineExtensionManager::installFinished(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager15installFinishedERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->installFinished(*extension);
}

//  void QWebEngineExtensionManager::unloadFinished(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager14unloadFinishedERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->unloadFinished(*extension);
}

//  void QWebEngineExtensionManager::uninstallFinished(const
//      QWebEngineExtensionInfo &extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineExtensionManager17uninstallFinishedERK23QWebEngineExtensionInfo(
    QWebEngineExtensionManager *self,
    const QWebEngineExtensionInfo *extension) {
  self->uninstallFinished(*extension);
}

//  bool QWebEngineExtensionManager::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QWebEngineExtensionManager5eventEP6QEvent(
    QWebEngineExtensionManager *self,
    QEvent *e) {
  return self->event(e);
}

//  QWebEngineExtensionManager::QWebEngineExtensionManager(QtWebEngineCore::E
//      xtensionManager *d)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionManager *ritual_ZN26QWebEngineExtensionManagerC1EPN15QtWebEngineCore16ExtensionManagerE(
    QtWebEngineCore::ExtensionManager *d) {
  return new CuteQWebEngineExtensionManager(d);
}

//  a Python function taken by a CuteQWebEngineExtensionManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineExtensionManager(
    QWebEngineExtensionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineExtensionManager *>(self)->take(key, call);
}

//  bool QWebEngineExtensionManager::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QWebEngineExtensionManager5eventEP6QEvent(
    QWebEngineExtensionManager *self,
    QEvent *e) {
  return static_cast<OwnQWebEngineExtensionManager *>(self)->OwnQWebEngineExtensionManager::event(
      e);
}

#endif  // QT_CONFIG(webengine_extensions)
