//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtUiPlugin/customwidget.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerPluginManager that Python can take functions over in. Every QDesignerPluginManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPluginManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPluginManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPluginManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPluginManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPluginManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPluginManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPluginManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerPluginManager : public QDesignerPluginManager {
public:
  using QDesignerPluginManager::QDesignerPluginManager;
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
      CuteQDesignerPluginManagerCall0 call = reinterpret_cast<CuteQDesignerPluginManagerCall0>(taken[0]);
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
      CuteQDesignerPluginManagerCall1 call = reinterpret_cast<CuteQDesignerPluginManagerCall1>(taken[1]);
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
      CuteQDesignerPluginManagerCall2 call = reinterpret_cast<CuteQDesignerPluginManagerCall2>(taken[2]);
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
      CuteQDesignerPluginManagerCall3 call = reinterpret_cast<CuteQDesignerPluginManagerCall3>(taken[3]);
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
      CuteQDesignerPluginManagerCall4 call = reinterpret_cast<CuteQDesignerPluginManagerCall4>(taken[4]);
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
      CuteQDesignerPluginManagerCall5 call = reinterpret_cast<CuteQDesignerPluginManagerCall5>(taken[5]);
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
      CuteQDesignerPluginManagerCall6 call = reinterpret_cast<CuteQDesignerPluginManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerPluginManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDesignerPluginManager10metaObjectEv(
    const QDesignerPluginManager *self) {
  return self->metaObject();
}

//  void *QDesignerPluginManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QDesignerPluginManager11qt_metacastEPKc(
    QDesignerPluginManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerPluginManager::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDesignerPluginManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerPluginManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerPluginManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QDesignerPluginManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerPluginManager::tr(s, c, n));
}

//  QDesignerPluginManager::QDesignerPluginManager(QDesignerFormEditorInterfa
//      ce *core)
extern "C" Q_DECL_EXPORT
QDesignerPluginManager *ritual_ZN22QDesignerPluginManagerC1EP28QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *core) {
  return new CuteQDesignerPluginManager(core);
}

//  QDesignerPluginManager::QDesignerPluginManager(const QStringList
//      &pluginPaths, QDesignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
QDesignerPluginManager *ritual_ZN22QDesignerPluginManagerC1ERK5QListI7QStringEP28QDesignerFormEditorInterface(
    const QList<QString> *pluginPaths,
    QDesignerFormEditorInterface *core) {
  return new CuteQDesignerPluginManager(*pluginPaths, core);
}

//  QDesignerPluginManager::~QDesignerPluginManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManagerD1Ev(QDesignerPluginManager *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerPluginManager::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK22QDesignerPluginManager4coreEv(
    const QDesignerPluginManager *self) {
  return self->core();
}

//  QObject *QDesignerPluginManager::instance(const QString &plugin) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QDesignerPluginManager8instanceERK7QString(
    const QDesignerPluginManager *self,
    const QString *plugin) {
  return self->instance(*plugin);
}

//  QStringList QDesignerPluginManager::registeredPlugins() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QDesignerPluginManager17registeredPluginsEv(
    const QDesignerPluginManager *self) {
  return new QList<QString>(self->registeredPlugins());
}

//  QStringList QDesignerPluginManager::findPlugins(const QString &path)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN22QDesignerPluginManager11findPluginsERK7QString(
    QDesignerPluginManager *self,
    const QString *path) {
  return new QList<QString>(self->findPlugins(*path));
}

//  QStringList QDesignerPluginManager::pluginPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QDesignerPluginManager11pluginPathsEv(
    const QDesignerPluginManager *self) {
  return new QList<QString>(self->pluginPaths());
}

//  void QDesignerPluginManager::setPluginPaths(const QStringList
//      &plugin_paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager14setPluginPathsERK5QListI7QStringE(
    QDesignerPluginManager *self,
    const QList<QString> *plugin_paths) {
  self->setPluginPaths(*plugin_paths);
}

//  QStringList QDesignerPluginManager::disabledPlugins() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QDesignerPluginManager15disabledPluginsEv(
    const QDesignerPluginManager *self) {
  return new QList<QString>(self->disabledPlugins());
}

//  void QDesignerPluginManager::setDisabledPlugins(const QStringList
//      &disabled_plugins)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager18setDisabledPluginsERK5QListI7QStringE(
    QDesignerPluginManager *self,
    const QList<QString> *disabled_plugins) {
  self->setDisabledPlugins(*disabled_plugins);
}

//  QStringList QDesignerPluginManager::failedPlugins() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QDesignerPluginManager13failedPluginsEv(
    const QDesignerPluginManager *self) {
  return new QList<QString>(self->failedPlugins());
}

//  QString QDesignerPluginManager::failureReason(const QString &pluginName)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDesignerPluginManager13failureReasonERK7QString(
    const QDesignerPluginManager *self,
    const QString *pluginName) {
  return new QString(self->failureReason(*pluginName));
}

//  QObjectList QDesignerPluginManager::instances() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK22QDesignerPluginManager9instancesEv(
    const QDesignerPluginManager *self) {
  return new QList<QObject *>(self->instances());
}

//  CustomWidgetList QDesignerPluginManager::registeredCustomWidgets() const
extern "C" Q_DECL_EXPORT
QList<QDesignerCustomWidgetInterface *> *ritual_ZNK22QDesignerPluginManager23registeredCustomWidgetsEv(
    const QDesignerPluginManager *self) {
  return new QList<QDesignerCustomWidgetInterface *>(
      self->registeredCustomWidgets());
}

//  QDesignerCustomWidgetData
//      QDesignerPluginManager::customWidgetData(QDesignerCustomWidgetInterfa
//      ce *w) const
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData *ritual_ZNK22QDesignerPluginManager16customWidgetDataEP30QDesignerCustomWidgetInterface(
    const QDesignerPluginManager *self,
    QDesignerCustomWidgetInterface *w) {
  return new QDesignerCustomWidgetData(self->customWidgetData(w));
}

//  QDesignerCustomWidgetData QDesignerPluginManager::customWidgetData(const
//      QString &className) const
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetData *ritual_ZNK22QDesignerPluginManager16customWidgetDataERK7QString(
    const QDesignerPluginManager *self,
    const QString *className) {
  return new QDesignerCustomWidgetData(self->customWidgetData(*className));
}

//  bool QDesignerPluginManager::registerNewPlugins()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDesignerPluginManager18registerNewPluginsEv(
    QDesignerPluginManager *self) {
  return self->registerNewPlugins();
}

//  QStringList QDesignerPluginManager::defaultPluginPaths()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN22QDesignerPluginManager18defaultPluginPathsEv() {
  return new QList<QString>(QDesignerPluginManager::defaultPluginPaths());
}

//  bool QDesignerPluginManager::syncSettings()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDesignerPluginManager12syncSettingsEv(
    QDesignerPluginManager *self) {
  return self->syncSettings();
}

//  void QDesignerPluginManager::ensureInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager17ensureInitializedEv(
    QDesignerPluginManager *self) {
  self->ensureInitialized();
}

//  void QDesignerPluginManager::updateRegisteredPlugins()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager23updateRegisteredPluginsEv(
    QDesignerPluginManager *self) {
  self->updateRegisteredPlugins();
}

//  void QDesignerPluginManager::registerPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager12registerPathERK7QString(
    QDesignerPluginManager *self,
    const QString *path) {
  self->registerPath(*path);
}

//  void QDesignerPluginManager::registerPlugin(const QString &plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPluginManager14registerPluginERK7QString(
    QDesignerPluginManager *self,
    const QString *plugin) {
  self->registerPlugin(*plugin);
}

//  a Python function taken by a CuteQDesignerPluginManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerPluginManager(
    QDesignerPluginManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerPluginManager *>(self)->take(key, call);
}
