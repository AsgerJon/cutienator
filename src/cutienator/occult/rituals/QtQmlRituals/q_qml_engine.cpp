//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlengine.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlabstracturlinterceptor.h>
#include <QtCore/qurl.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlEngine : QQmlEngine {
  using QQmlEngine::event;
};

//  A QQmlEngine that Python can take functions over in. Every QQmlEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlEngine : public QQmlEngine {
public:
  using QQmlEngine::QQmlEngine;
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
  //  bool QQmlEngine::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlEngineCall0 call = reinterpret_cast<CuteQQmlEngineCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlEngine::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlEngineCall1 call = reinterpret_cast<CuteQQmlEngineCall1>(taken[1]);
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
      CuteQQmlEngineCall2 call = reinterpret_cast<CuteQQmlEngineCall2>(taken[2]);
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
      CuteQQmlEngineCall3 call = reinterpret_cast<CuteQQmlEngineCall3>(taken[3]);
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
      CuteQQmlEngineCall4 call = reinterpret_cast<CuteQQmlEngineCall4>(taken[4]);
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
      CuteQQmlEngineCall5 call = reinterpret_cast<CuteQQmlEngineCall5>(taken[5]);
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
      CuteQQmlEngineCall6 call = reinterpret_cast<CuteQQmlEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQmlEngine10metaObjectEv(
    const QQmlEngine *self) {
  return self->metaObject();
}

//  QString QQmlEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQmlEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlEngine::tr(s, c, n));
}

//  QQmlEngine::QQmlEngine(QObject *p)
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZN10QQmlEngineC1EP7QObject(QObject *p) {
  return new CuteQQmlEngine(p);
}

//  QQmlEngine::~QQmlEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngineD1Ev(QQmlEngine *self) {
  delete self;
}

//  QQmlContext *QQmlEngine::rootContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK10QQmlEngine11rootContextEv(const QQmlEngine *self) {
  return self->rootContext();
}

//  void QQmlEngine::clearComponentCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine19clearComponentCacheEv(QQmlEngine *self) {
  self->clearComponentCache();
}

//  void QQmlEngine::trimComponentCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine18trimComponentCacheEv(QQmlEngine *self) {
  self->trimComponentCache();
}

//  void QQmlEngine::clearSingletons()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine15clearSingletonsEv(QQmlEngine *self) {
  self->clearSingletons();
}

//  QStringList QQmlEngine::importPathList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QQmlEngine14importPathListEv(
    const QQmlEngine *self) {
  return new QList<QString>(self->importPathList());
}

//  void QQmlEngine::setImportPathList(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine17setImportPathListERK5QListI7QStringE(
    QQmlEngine *self,
    const QList<QString> *paths) {
  self->setImportPathList(*paths);
}

//  void QQmlEngine::addImportPath(const QString &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine13addImportPathERK7QString(
    QQmlEngine *self,
    const QString *dir) {
  self->addImportPath(*dir);
}

//  QStringList QQmlEngine::pluginPathList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QQmlEngine14pluginPathListEv(
    const QQmlEngine *self) {
  return new QList<QString>(self->pluginPathList());
}

//  void QQmlEngine::setPluginPathList(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine17setPluginPathListERK5QListI7QStringE(
    QQmlEngine *self,
    const QList<QString> *paths) {
  self->setPluginPathList(*paths);
}

//  void QQmlEngine::addPluginPath(const QString &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine13addPluginPathERK7QString(
    QQmlEngine *self,
    const QString *dir) {
  self->addPluginPath(*dir);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QQmlEngine::addNamedBundle(const QString &a0, const QString &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQmlEngine14addNamedBundleERK7QStringS2_(
    QQmlEngine *self,
    const QString *a0,
    const QString *a1) {
  return self->addNamedBundle(*a0, *a1);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_CONFIG(qml_network)
//  void QQmlEngine::setNetworkAccessManagerFactory(QQmlNetworkAccessManagerF
//      actory *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine30setNetworkAccessManagerFactoryEP31QQmlNetworkAccessManagerFactory(
    QQmlEngine *self,
    QQmlNetworkAccessManagerFactory *a0) {
  self->setNetworkAccessManagerFactory(a0);
}
#endif  // QT_CONFIG(qml_network)

#if QT_CONFIG(qml_network)
//  QQmlNetworkAccessManagerFactory
//      *QQmlEngine::networkAccessManagerFactory() const
extern "C" Q_DECL_EXPORT
QQmlNetworkAccessManagerFactory *ritual_ZNK10QQmlEngine27networkAccessManagerFactoryEv(
    const QQmlEngine *self) {
  return self->networkAccessManagerFactory();
}
#endif  // QT_CONFIG(qml_network)

#if QT_CONFIG(qml_network)
//  QNetworkAccessManager *QQmlEngine::networkAccessManager() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZNK10QQmlEngine20networkAccessManagerEv(
    const QQmlEngine *self) {
  return self->networkAccessManager();
}
#endif  // QT_CONFIG(qml_network)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QQmlEngine::setUrlInterceptor(QQmlAbstractUrlInterceptor
//      *urlInterceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine17setUrlInterceptorEP26QQmlAbstractUrlInterceptor(
    QQmlEngine *self,
    QQmlAbstractUrlInterceptor *urlInterceptor) {
  self->setUrlInterceptor(urlInterceptor);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QQmlAbstractUrlInterceptor *QQmlEngine::urlInterceptor() const
extern "C" Q_DECL_EXPORT
QQmlAbstractUrlInterceptor *ritual_ZNK10QQmlEngine14urlInterceptorEv(
    const QQmlEngine *self) {
  return self->urlInterceptor();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  void QQmlEngine::addUrlInterceptor(QQmlAbstractUrlInterceptor
//      *urlInterceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine17addUrlInterceptorEP26QQmlAbstractUrlInterceptor(
    QQmlEngine *self,
    QQmlAbstractUrlInterceptor *urlInterceptor) {
  self->addUrlInterceptor(urlInterceptor);
}

//  void QQmlEngine::removeUrlInterceptor(QQmlAbstractUrlInterceptor
//      *urlInterceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine20removeUrlInterceptorEP26QQmlAbstractUrlInterceptor(
    QQmlEngine *self,
    QQmlAbstractUrlInterceptor *urlInterceptor) {
  self->removeUrlInterceptor(urlInterceptor);
}

//  QList<QQmlAbstractUrlInterceptor *> QQmlEngine::urlInterceptors() const
extern "C" Q_DECL_EXPORT
QList<QQmlAbstractUrlInterceptor *> *ritual_ZNK10QQmlEngine15urlInterceptorsEv(
    const QQmlEngine *self) {
  return new QList<QQmlAbstractUrlInterceptor *>(self->urlInterceptors());
}

//  QUrl QQmlEngine::interceptUrl(const QUrl &url,
//      QQmlAbstractUrlInterceptor::DataType type) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQmlEngine12interceptUrlERK4QUrlN26QQmlAbstractUrlInterceptor8DataTypeE(
    const QQmlEngine *self,
    const QUrl *url,
    QQmlAbstractUrlInterceptor::DataType type) {
  return new QUrl(self->interceptUrl(*url, type));
}

//  void QQmlEngine::addImageProvider(const QString &id,
//      QQmlImageProviderBase *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine16addImageProviderERK7QStringP21QQmlImageProviderBase(
    QQmlEngine *self,
    const QString *id,
    QQmlImageProviderBase *a1) {
  self->addImageProvider(*id, a1);
}

//  QQmlImageProviderBase *QQmlEngine::imageProvider(const QString &id) const
extern "C" Q_DECL_EXPORT
QQmlImageProviderBase *ritual_ZNK10QQmlEngine13imageProviderERK7QString(
    const QQmlEngine *self,
    const QString *id) {
  return self->imageProvider(*id);
}

//  void QQmlEngine::removeImageProvider(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine19removeImageProviderERK7QString(
    QQmlEngine *self,
    const QString *id) {
  self->removeImageProvider(*id);
}

//  void QQmlEngine::setIncubationController(QQmlIncubationController *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine23setIncubationControllerEP24QQmlIncubationController(
    QQmlEngine *self,
    QQmlIncubationController *a0) {
  self->setIncubationController(a0);
}

//  QQmlIncubationController *QQmlEngine::incubationController() const
extern "C" Q_DECL_EXPORT
QQmlIncubationController *ritual_ZNK10QQmlEngine20incubationControllerEv(
    const QQmlEngine *self) {
  return self->incubationController();
}

//  void QQmlEngine::setOfflineStoragePath(const QString &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine21setOfflineStoragePathERK7QString(
    QQmlEngine *self,
    const QString *dir) {
  self->setOfflineStoragePath(*dir);
}

//  QString QQmlEngine::offlineStoragePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQmlEngine18offlineStoragePathEv(
    const QQmlEngine *self) {
  return new QString(self->offlineStoragePath());
}

//  QString QQmlEngine::offlineStorageDatabaseFilePath(const QString
//      &databaseName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQmlEngine30offlineStorageDatabaseFilePathERK7QString(
    const QQmlEngine *self,
    const QString *databaseName) {
  return new QString(self->offlineStorageDatabaseFilePath(*databaseName));
}

//  QUrl QQmlEngine::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QQmlEngine7baseUrlEv(const QQmlEngine *self) {
  return new QUrl(self->baseUrl());
}

//  void QQmlEngine::setBaseUrl(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine10setBaseUrlERK4QUrl(
    QQmlEngine *self,
    const QUrl *a0) {
  self->setBaseUrl(*a0);
}

//  bool QQmlEngine::outputWarningsToStandardError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQmlEngine29outputWarningsToStandardErrorEv(
    const QQmlEngine *self) {
  return self->outputWarningsToStandardError();
}

//  void QQmlEngine::setOutputWarningsToStandardError(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine32setOutputWarningsToStandardErrorEb(
    QQmlEngine *self,
    bool a0) {
  self->setOutputWarningsToStandardError(a0);
}

//  void QQmlEngine::markCurrentFunctionAsTranslationBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine39markCurrentFunctionAsTranslationBindingEv(
    QQmlEngine *self) {
  self->markCurrentFunctionAsTranslationBinding();
}

//  bool QQmlEngine::setExternalSingletonInstance(QAnyStringView moduleName,
//      QAnyStringView typeName, QObject *instance)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQmlEngine28setExternalSingletonInstanceE14QAnyStringViewS0_P7QObject(
    QQmlEngine *self,
    const QString *moduleName,
    const QString *typeName,
    QObject *instance) {
  return self->setExternalSingletonInstance(
      QAnyStringView(*moduleName),
      QAnyStringView(*typeName),
      instance);
}

//  void QQmlEngine::captureProperty(QObject *object, const QMetaProperty
//      &property) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQmlEngine15capturePropertyEP7QObjectRK13QMetaProperty(
    const QQmlEngine *self,
    QObject *object,
    const QMetaProperty *property) {
  self->captureProperty(object, *property);
}

//  void QQmlEngine::retranslate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine11retranslateEv(QQmlEngine *self) {
  self->retranslate();
}

//  QQmlContext *QQmlEngine::contextForObject(const QObject *a0)
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN10QQmlEngine16contextForObjectEPK7QObject(
    const QObject *a0) {
  return QQmlEngine::contextForObject(a0);
}

//  void QQmlEngine::setContextForObject(QObject *a0, QQmlContext *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlEngine19setContextForObjectEP7QObjectP11QQmlContext(
    QObject *a0,
    QQmlContext *a1) {
  QQmlEngine::setContextForObject(a0, a1);
}

//  bool QQmlEngine::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QQmlEngine5eventEP6QEvent(QQmlEngine *self, QEvent *a0) {
  return self->event(a0);
}

//  QQmlEnginePrivate *QQmlEngine::d_func()
extern "C" Q_DECL_EXPORT
QQmlEnginePrivate *ritual_ZN10QQmlEngine6d_funcEv(QQmlEngine *self) {
  return self->d_func();
}

//  const QQmlEnginePrivate *QQmlEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlEnginePrivate *ritual_ZNK10QQmlEngine6d_funcEv(
    const QQmlEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlEngine(QQmlEngine *self, const char *key, void *call) {
  return static_cast<CuteQQmlEngine *>(self)->take(key, call);
}

//  bool QQmlEngine::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QQmlEngine5eventEP6QEvent(QQmlEngine *self, QEvent *a0) {
  return static_cast<OwnQQmlEngine *>(self)->OwnQQmlEngine::event(a0);
}
