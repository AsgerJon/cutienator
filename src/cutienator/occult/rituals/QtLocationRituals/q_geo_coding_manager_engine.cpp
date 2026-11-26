//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeocodingmanagerengine.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtLocation/qgeocodingmanagerengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtPositioning/qgeoaddress.h>
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QGeoCodingManagerEngine that Python can take functions over in. Every QGeoCodingManagerEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoCodingManagerEngineCall0)(const void *, const QGeoAddress *, const QGeoShape *, int *);
typedef void * (*CuteQGeoCodingManagerEngineCall1)(const void *, const QString *, int, int, const QGeoShape *, int *);
typedef void * (*CuteQGeoCodingManagerEngineCall2)(const void *, const QGeoCoordinate *, const QGeoShape *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodingManagerEngineCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodingManagerEngineCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerEngineCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerEngineCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerEngineCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerEngineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodingManagerEngineCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoCodingManagerEngine : public QGeoCodingManagerEngine {
public:
  using QGeoCodingManagerEngine::QGeoCodingManagerEngine;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK9QGeoShape")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QGeoShape")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoCoordinateRK9QGeoShape")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QGeoAddress
  //      &address, const QGeoShape &bounds)
  QGeoCodeReply *geocode(
      const QGeoAddress &address,
      const QGeoShape &bounds) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall0 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall0>(taken[0]);
      void * given = call(this, &address, &bounds, &handled);
      if (handled) return static_cast<QGeoCodeReply *>(given);
    }
    return QGeoCodingManagerEngine::geocode(address, bounds);
  }

  //  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QString
  //      &address, int limit, int offset, const QGeoShape &bounds)
  QGeoCodeReply *geocode(
      const QString &address,
      int limit,
      int offset,
      const QGeoShape &bounds) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall1 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall1>(taken[1]);
      void * given = call(this, &address, limit, offset, &bounds, &handled);
      if (handled) return static_cast<QGeoCodeReply *>(given);
    }
    return QGeoCodingManagerEngine::geocode(address, limit, offset, bounds);
  }

  //  QGeoCodeReply *QGeoCodingManagerEngine::reverseGeocode(const
  //      QGeoCoordinate &coordinate, const QGeoShape &bounds)
  QGeoCodeReply *reverseGeocode(
      const QGeoCoordinate &coordinate,
      const QGeoShape &bounds) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall2 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall2>(taken[2]);
      void * given = call(this, &coordinate, &bounds, &handled);
      if (handled) return static_cast<QGeoCodeReply *>(given);
    }
    return QGeoCodingManagerEngine::reverseGeocode(coordinate, bounds);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall3 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall4 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall5 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall6 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall7 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall8 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoCodingManagerEngineCall9 call = reinterpret_cast<CuteQGeoCodingManagerEngineCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoCodingManagerEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QGeoCodingManagerEngine10metaObjectEv(
    const QGeoCodingManagerEngine *self) {
  return self->metaObject();
}

//  void *QGeoCodingManagerEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QGeoCodingManagerEngine11qt_metacastEPKc(
    QGeoCodingManagerEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoCodingManagerEngine::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QGeoCodingManagerEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoCodingManagerEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoCodingManagerEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QGeoCodingManagerEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoCodingManagerEngine::tr(s, c, n));
}

//  QGeoCodingManagerEngine::QGeoCodingManagerEngine(const QVariantMap
//      &parameters, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCodingManagerEngine *ritual_ZN23QGeoCodingManagerEngineC1ERK4QMapI7QString8QVariantEP7QObject(
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return new CuteQGeoCodingManagerEngine(*parameters, parent);
}

//  QGeoCodingManagerEngine::~QGeoCodingManagerEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngineD1Ev(QGeoCodingManagerEngine *self) {
  delete self;
}

//  QString QGeoCodingManagerEngine::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QGeoCodingManagerEngine11managerNameEv(
    const QGeoCodingManagerEngine *self) {
  return new QString(self->managerName());
}

//  int QGeoCodingManagerEngine::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGeoCodingManagerEngine14managerVersionEv(
    const QGeoCodingManagerEngine *self) {
  return self->managerVersion();
}

//  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QGeoAddress
//      &address, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QGeoAddress *address,
    const QGeoShape *bounds) {
  return self->geocode(*address, *bounds);
}

//  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QString &address,
//      int limit, int offset, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QString *address,
    int limit,
    int offset,
    const QGeoShape *bounds) {
  return self->geocode(*address, limit, offset, *bounds);
}

//  QGeoCodeReply *QGeoCodingManagerEngine::reverseGeocode(const
//      QGeoCoordinate &coordinate, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoCoordinateRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QGeoCoordinate *coordinate,
    const QGeoShape *bounds) {
  return self->reverseGeocode(*coordinate, *bounds);
}

//  void QGeoCodingManagerEngine::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngine9setLocaleERK7QLocale(
    QGeoCodingManagerEngine *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoCodingManagerEngine::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK23QGeoCodingManagerEngine6localeEv(
    const QGeoCodingManagerEngine *self) {
  return new QLocale(self->locale());
}

//  void QGeoCodingManagerEngine::finished(QGeoCodeReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngine8finishedEP13QGeoCodeReply(
    QGeoCodingManagerEngine *self,
    QGeoCodeReply *reply) {
  self->finished(reply);
}

//  void QGeoCodingManagerEngine::errorOccurred(QGeoCodeReply *reply,
//      QGeoCodeReply::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngine13errorOccurredEP13QGeoCodeReplyNS0_5ErrorERK7QString(
    QGeoCodingManagerEngine *self,
    QGeoCodeReply *reply,
    QGeoCodeReply::Error error,
    const QString *errorString) {
  self->errorOccurred(reply, error, *errorString);
}

//  void QGeoCodingManagerEngine::setManagerName(const QString &managerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngine14setManagerNameERK7QString(
    QGeoCodingManagerEngine *self,
    const QString *managerName) {
  self->setManagerName(*managerName);
}

//  void QGeoCodingManagerEngine::setManagerVersion(int managerVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoCodingManagerEngine17setManagerVersionEi(
    QGeoCodingManagerEngine *self,
    int managerVersion) {
  self->setManagerVersion(managerVersion);
}

//  a Python function taken by a CuteQGeoCodingManagerEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoCodingManagerEngine(
    QGeoCodingManagerEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoCodingManagerEngine *>(self)->take(key, call);
}

//  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QGeoAddress
//      &address, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_own_ZN23QGeoCodingManagerEngine7geocodeERK11QGeoAddressRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QGeoAddress *address,
    const QGeoShape *bounds) {
  return self->QGeoCodingManagerEngine::geocode(*address, *bounds);
}

//  QGeoCodeReply *QGeoCodingManagerEngine::geocode(const QString &address,
//      int limit, int offset, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_own_ZN23QGeoCodingManagerEngine7geocodeERK7QStringiiRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QString *address,
    int limit,
    int offset,
    const QGeoShape *bounds) {
  return self->QGeoCodingManagerEngine::geocode(
      *address,
      limit,
      offset,
      *bounds);
}

//  QGeoCodeReply *QGeoCodingManagerEngine::reverseGeocode(const
//      QGeoCoordinate &coordinate, const QGeoShape &bounds)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_own_ZN23QGeoCodingManagerEngine14reverseGeocodeERK14QGeoCoordinateRK9QGeoShape(
    QGeoCodingManagerEngine *self,
    const QGeoCoordinate *coordinate,
    const QGeoShape *bounds) {
  return self->QGeoCodingManagerEngine::reverseGeocode(*coordinate, *bounds);
}
