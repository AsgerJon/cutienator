//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpluginloader.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpluginloader.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qplugin.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPluginLoader that Python can take functions over in. Every QPluginLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPluginLoaderCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQPluginLoaderCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQPluginLoaderCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQPluginLoaderCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQPluginLoaderCall4)(const void *, QEvent *, int *);
typedef void (*CuteQPluginLoaderCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQPluginLoaderCall6)(const void *, const QMetaMethod *, int *);
class CuteQPluginLoader : public QPluginLoader {
public:
  using QPluginLoader::QPluginLoader;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPluginLoaderCall0 call = reinterpret_cast<CuteQPluginLoaderCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPluginLoaderCall1 call = reinterpret_cast<CuteQPluginLoaderCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPluginLoaderCall2 call = reinterpret_cast<CuteQPluginLoaderCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPluginLoaderCall3 call = reinterpret_cast<CuteQPluginLoaderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPluginLoaderCall4 call = reinterpret_cast<CuteQPluginLoaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPluginLoaderCall5 call = reinterpret_cast<CuteQPluginLoaderCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPluginLoaderCall6 call = reinterpret_cast<CuteQPluginLoaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QPluginLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPluginLoader10metaObjectEv(
    const QPluginLoader *self) {
  return self->metaObject();
}

//  QString QPluginLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPluginLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPluginLoader::tr(s, c, n));
}

//  QPluginLoader::QPluginLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QPluginLoader *ritual_ZN13QPluginLoaderC1EP7QObject(QObject *parent) {
  return new CuteQPluginLoader(parent);
}

//  QPluginLoader::QPluginLoader(const QString &fileName, QObject *parent)
extern "C" Q_DECL_EXPORT
QPluginLoader *ritual_ZN13QPluginLoaderC1ERK7QStringP7QObject(
    const QString *fileName,
    QObject *parent) {
  return new CuteQPluginLoader(*fileName, parent);
}

//  QPluginLoader::~QPluginLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoaderD1Ev(QPluginLoader *self) {
  delete self;
}

//  QObject *QPluginLoader::instance()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN13QPluginLoader8instanceEv(QPluginLoader *self) {
  return self->instance();
}

//  QJsonObject QPluginLoader::metaData() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QPluginLoader8metaDataEv(
    const QPluginLoader *self) {
  return new QJsonObject(self->metaData());
}

//  QObjectList QPluginLoader::staticInstances()
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZN13QPluginLoader15staticInstancesEv() {
  return new QList<QObject *>(QPluginLoader::staticInstances());
}

//  QList<QStaticPlugin> QPluginLoader::staticPlugins()
extern "C" Q_DECL_EXPORT
QList<QStaticPlugin> *ritual_ZN13QPluginLoader13staticPluginsEv() {
  return new QList<QStaticPlugin>(QPluginLoader::staticPlugins());
}

//  bool QPluginLoader::load()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPluginLoader4loadEv(QPluginLoader *self) {
  return self->load();
}

//  bool QPluginLoader::unload()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPluginLoader6unloadEv(QPluginLoader *self) {
  return self->unload();
}

//  bool QPluginLoader::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPluginLoader8isLoadedEv(const QPluginLoader *self) {
  return self->isLoaded();
}

//  void QPluginLoader::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoader11setFileNameERK7QString(
    QPluginLoader *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QPluginLoader::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPluginLoader8fileNameEv(const QPluginLoader *self) {
  return new QString(self->fileName());
}

//  QString QPluginLoader::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPluginLoader11errorStringEv(
    const QPluginLoader *self) {
  return new QString(self->errorString());
}

//  void QPluginLoader::setLoadHints(QLibrary::LoadHints loadHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPluginLoader12setLoadHintsE6QFlagsIN8QLibrary8LoadHintEE(
    QPluginLoader *self,
    int loadHints) {
  self->setLoadHints(QFlags<QLibrary::LoadHint>::fromInt(loadHints));
}

//  QLibrary::LoadHints QPluginLoader::loadHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPluginLoader9loadHintsEv(const QPluginLoader *self) {
  return static_cast<int>(self->loadHints().toInt());
}

//  a Python function taken by a CuteQPluginLoader, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPluginLoader(
    QPluginLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPluginLoader *>(self)->take(key, call);
}
