//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomappingmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomappingmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoMappingManager that Python can take functions over in. Every QGeoMappingManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMappingManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoMappingManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoMappingManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoMappingManager : public QGeoMappingManager {
public:
  using QGeoMappingManager::QGeoMappingManager;
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
      CuteQGeoMappingManagerCall0 call = reinterpret_cast<CuteQGeoMappingManagerCall0>(taken[0]);
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
      CuteQGeoMappingManagerCall1 call = reinterpret_cast<CuteQGeoMappingManagerCall1>(taken[1]);
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
      CuteQGeoMappingManagerCall2 call = reinterpret_cast<CuteQGeoMappingManagerCall2>(taken[2]);
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
      CuteQGeoMappingManagerCall3 call = reinterpret_cast<CuteQGeoMappingManagerCall3>(taken[3]);
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
      CuteQGeoMappingManagerCall4 call = reinterpret_cast<CuteQGeoMappingManagerCall4>(taken[4]);
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
      CuteQGeoMappingManagerCall5 call = reinterpret_cast<CuteQGeoMappingManagerCall5>(taken[5]);
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
      CuteQGeoMappingManagerCall6 call = reinterpret_cast<CuteQGeoMappingManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoMappingManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QGeoMappingManager10metaObjectEv(
    const QGeoMappingManager *self) {
  return self->metaObject();
}

//  void *QGeoMappingManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QGeoMappingManager11qt_metacastEPKc(
    QGeoMappingManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoMappingManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGeoMappingManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoMappingManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoMappingManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QGeoMappingManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoMappingManager::tr(s, c, n));
}

//  QGeoMappingManager::~QGeoMappingManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoMappingManagerD1Ev(QGeoMappingManager *self) {
  delete self;
}

//  QString QGeoMappingManager::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QGeoMappingManager11managerNameEv(
    const QGeoMappingManager *self) {
  return new QString(self->managerName());
}

//  int QGeoMappingManager::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoMappingManager14managerVersionEv(
    const QGeoMappingManager *self) {
  return self->managerVersion();
}

//  QGeoMap *QGeoMappingManager::createMap(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZN18QGeoMappingManager9createMapEP7QObject(
    QGeoMappingManager *self,
    QObject *parent) {
  return self->createMap(parent);
}

//  QList<QGeoMapType> QGeoMappingManager::supportedMapTypes() const
extern "C" Q_DECL_EXPORT
QList<QGeoMapType> *ritual_ZNK18QGeoMappingManager17supportedMapTypesEv(
    const QGeoMappingManager *self) {
  return new QList<QGeoMapType>(self->supportedMapTypes());
}

//  bool QGeoMappingManager::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGeoMappingManager13isInitializedEv(
    const QGeoMappingManager *self) {
  return self->isInitialized();
}

//  void QGeoMappingManager::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoMappingManager9setLocaleERK7QLocale(
    QGeoMappingManager *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoMappingManager::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK18QGeoMappingManager6localeEv(
    const QGeoMappingManager *self) {
  return new QLocale(self->locale());
}

//  void QGeoMappingManager::initialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoMappingManager11initializedEv(QGeoMappingManager *self) {
  self->initialized();
}

//  void QGeoMappingManager::supportedMapTypesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoMappingManager24supportedMapTypesChangedEv(
    QGeoMappingManager *self) {
  self->supportedMapTypesChanged();
}

//  QGeoMappingManager::QGeoMappingManager(QGeoMappingManagerEngine *engine,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoMappingManager *ritual_ZN18QGeoMappingManagerC1EP24QGeoMappingManagerEngineP7QObject(
    QGeoMappingManagerEngine *engine,
    QObject *parent) {
  return new CuteQGeoMappingManager(engine, parent);
}

//  a Python function taken by a CuteQGeoMappingManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoMappingManager(
    QGeoMappingManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoMappingManager *>(self)->take(key, call);
}
