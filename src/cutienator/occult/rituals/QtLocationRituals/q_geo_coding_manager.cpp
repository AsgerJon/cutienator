//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeocodingmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeocodingmanager.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeoaddress.h>
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoCodingManager that Python can take functions over in. Every QGeoCodingManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodingManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodingManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoCodingManager : public QGeoCodingManager {
public:
  using QGeoCodingManager::QGeoCodingManager;
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
      CuteQGeoCodingManagerCall0 call = reinterpret_cast<CuteQGeoCodingManagerCall0>(taken[0]);
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
      CuteQGeoCodingManagerCall1 call = reinterpret_cast<CuteQGeoCodingManagerCall1>(taken[1]);
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
      CuteQGeoCodingManagerCall2 call = reinterpret_cast<CuteQGeoCodingManagerCall2>(taken[2]);
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
      CuteQGeoCodingManagerCall3 call = reinterpret_cast<CuteQGeoCodingManagerCall3>(taken[3]);
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
      CuteQGeoCodingManagerCall4 call = reinterpret_cast<CuteQGeoCodingManagerCall4>(taken[4]);
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
      CuteQGeoCodingManagerCall5 call = reinterpret_cast<CuteQGeoCodingManagerCall5>(taken[5]);
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
      CuteQGeoCodingManagerCall6 call = reinterpret_cast<CuteQGeoCodingManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoCodingManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGeoCodingManager10metaObjectEv(
    const QGeoCodingManager *self) {
  return self->metaObject();
}

//  QString QGeoCodingManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGeoCodingManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoCodingManager::tr(s, c, n));
}

//  QGeoCodingManager::~QGeoCodingManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCodingManagerD1Ev(QGeoCodingManager *self) {
  delete self;
}

//  QString QGeoCodingManager::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGeoCodingManager11managerNameEv(
    const QGeoCodingManager *self) {
  return new QString(self->managerName());
}

//  int QGeoCodingManager::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoCodingManager14managerVersionEv(
    const QGeoCodingManager *self) {
  return self->managerVersion();
}

//  QGeoCodeReply *QGeoCodingManager::geocode(const QGeoAddress &address,
//      const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN17QGeoCodingManager7geocodeERK11QGeoAddressRK9QGeoShape(
    QGeoCodingManager *self,
    const QGeoAddress *address,
    const QGeoShape *bounds) {
  return self->geocode(*address, *bounds);
}

//  QGeoCodeReply *QGeoCodingManager::geocode(const QString &searchString,
//      int limit, int offset, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN17QGeoCodingManager7geocodeERK7QStringiiRK9QGeoShape(
    QGeoCodingManager *self,
    const QString *searchString,
    int limit,
    int offset,
    const QGeoShape *bounds) {
  return self->geocode(*searchString, limit, offset, *bounds);
}

//  QGeoCodeReply *QGeoCodingManager::reverseGeocode(const QGeoCoordinate
//      &coordinate, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN17QGeoCodingManager14reverseGeocodeERK14QGeoCoordinateRK9QGeoShape(
    QGeoCodingManager *self,
    const QGeoCoordinate *coordinate,
    const QGeoShape *bounds) {
  return self->reverseGeocode(*coordinate, *bounds);
}

//  void QGeoCodingManager::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCodingManager9setLocaleERK7QLocale(
    QGeoCodingManager *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoCodingManager::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK17QGeoCodingManager6localeEv(
    const QGeoCodingManager *self) {
  return new QLocale(self->locale());
}

//  QGeoCodingManager::QGeoCodingManager(QGeoCodingManagerEngine *engine,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCodingManager *ritual_ZN17QGeoCodingManagerC1EP23QGeoCodingManagerEngineP7QObject(
    QGeoCodingManagerEngine *engine,
    QObject *parent) {
  return new CuteQGeoCodingManager(engine, parent);
}

//  a Python function taken by a CuteQGeoCodingManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoCodingManager(
    QGeoCodingManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoCodingManager *>(self)->take(key, call);
}
