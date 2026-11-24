//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomappingmanagerengine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomappingmanagerengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoMappingManagerEngine that Python can take functions over in. Every QGeoMappingManagerEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoMappingManagerEngineCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMappingManagerEngineCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMappingManagerEngineCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerEngineCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerEngineCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerEngineCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerEngineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoMappingManagerEngine : public QGeoMappingManagerEngine {
public:
  using QGeoMappingManagerEngine::QGeoMappingManagerEngine;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QGeoMappingManagerEngine9createMapEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  QGeoMap *QGeoMappingManagerEngine::createMap()
  QGeoMap *createMap() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoMappingManagerEngineCall0 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoMap *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoMappingManagerEngineCall1 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoMappingManagerEngineCall2 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall2>(taken[2]);
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
      CuteQGeoMappingManagerEngineCall3 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall3>(taken[3]);
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
      CuteQGeoMappingManagerEngineCall4 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall4>(taken[4]);
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
      CuteQGeoMappingManagerEngineCall5 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall5>(taken[5]);
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
      CuteQGeoMappingManagerEngineCall6 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall6>(taken[6]);
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
      CuteQGeoMappingManagerEngineCall7 call = reinterpret_cast<CuteQGeoMappingManagerEngineCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoMappingManagerEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QGeoMappingManagerEngine10metaObjectEv(
    const QGeoMappingManagerEngine *self) {
  return self->metaObject();
}

//  QString QGeoMappingManagerEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QGeoMappingManagerEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoMappingManagerEngine::tr(s, c, n));
}

//  QGeoMappingManagerEngine::~QGeoMappingManagerEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngineD1Ev(
    QGeoMappingManagerEngine *self) {
  delete self;
}

//  QGeoMap *QGeoMappingManagerEngine::createMap()
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZN24QGeoMappingManagerEngine9createMapEv(
    QGeoMappingManagerEngine *self) {
  return self->createMap();
}

//  QString QGeoMappingManagerEngine::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QGeoMappingManagerEngine11managerNameEv(
    const QGeoMappingManagerEngine *self) {
  return new QString(self->managerName());
}

//  int QGeoMappingManagerEngine::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoMappingManagerEngine14managerVersionEv(
    const QGeoMappingManagerEngine *self) {
  return self->managerVersion();
}

//  QList<QGeoMapType> QGeoMappingManagerEngine::supportedMapTypes() const
extern "C" Q_DECL_EXPORT
QList<QGeoMapType> *ritual_ZNK24QGeoMappingManagerEngine17supportedMapTypesEv(
    const QGeoMappingManagerEngine *self) {
  return new QList<QGeoMapType>(self->supportedMapTypes());
}

//  QGeoCameraCapabilities QGeoMappingManagerEngine::cameraCapabilities(int
//      mapId) const
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZNK24QGeoMappingManagerEngine18cameraCapabilitiesEi(
    const QGeoMappingManagerEngine *self,
    int mapId) {
  return new QGeoCameraCapabilities(self->cameraCapabilities(mapId));
}

//  void QGeoMappingManagerEngine::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine9setLocaleERK7QLocale(
    QGeoMappingManagerEngine *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoMappingManagerEngine::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK24QGeoMappingManagerEngine6localeEv(
    const QGeoMappingManagerEngine *self) {
  return new QLocale(self->locale());
}

//  bool QGeoMappingManagerEngine::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QGeoMappingManagerEngine13isInitializedEv(
    const QGeoMappingManagerEngine *self) {
  return self->isInitialized();
}

//  void QGeoMappingManagerEngine::setSupportedMapTypes(const
//      QList<QGeoMapType> &supportedMapTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine20setSupportedMapTypesERK5QListI11QGeoMapTypeE(
    QGeoMappingManagerEngine *self,
    const QList<QGeoMapType> *supportedMapTypes) {
  self->setSupportedMapTypes(*supportedMapTypes);
}

//  void QGeoMappingManagerEngine::setCameraCapabilities(const
//      QGeoCameraCapabilities &capabilities)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine21setCameraCapabilitiesERK22QGeoCameraCapabilities(
    QGeoMappingManagerEngine *self,
    const QGeoCameraCapabilities *capabilities) {
  self->setCameraCapabilities(*capabilities);
}

//  void QGeoMappingManagerEngine::engineInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine17engineInitializedEv(
    QGeoMappingManagerEngine *self) {
  self->engineInitialized();
}

//  void QGeoMappingManagerEngine::setManagerName(const QString &managerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine14setManagerNameERK7QString(
    QGeoMappingManagerEngine *self,
    const QString *managerName) {
  self->setManagerName(*managerName);
}

//  void QGeoMappingManagerEngine::setManagerVersion(int managerVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoMappingManagerEngine17setManagerVersionEi(
    QGeoMappingManagerEngine *self,
    int managerVersion) {
  self->setManagerVersion(managerVersion);
}

//  QGeoMappingManagerEnginePrivate *QGeoMappingManagerEngine::d_func()
extern "C" Q_DECL_EXPORT
QGeoMappingManagerEnginePrivate *ritual_ZN24QGeoMappingManagerEngine6d_funcEv(
    QGeoMappingManagerEngine *self) {
  return self->d_func();
}

//  const QGeoMappingManagerEnginePrivate *QGeoMappingManagerEngine::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGeoMappingManagerEnginePrivate *ritual_ZNK24QGeoMappingManagerEngine6d_funcEv(
    const QGeoMappingManagerEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGeoMappingManagerEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMappingManagerEngine(
    QGeoMappingManagerEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMappingManagerEngine *>(self)->take(key, call);
}
