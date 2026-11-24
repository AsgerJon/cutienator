//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativegeolocation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativegeolocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeolocation.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QDeclarativeGeoLocation that Python can take functions over in. Every QDeclarativeGeoLocation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoLocationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoLocationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoLocationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoLocationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoLocationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoLocationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoLocationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoLocation : public QDeclarativeGeoLocation {
public:
  using QDeclarativeGeoLocation::QDeclarativeGeoLocation;
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
      CuteQDeclarativeGeoLocationCall0 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall0>(taken[0]);
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
      CuteQDeclarativeGeoLocationCall1 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall1>(taken[1]);
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
      CuteQDeclarativeGeoLocationCall2 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall2>(taken[2]);
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
      CuteQDeclarativeGeoLocationCall3 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall3>(taken[3]);
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
      CuteQDeclarativeGeoLocationCall4 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall4>(taken[4]);
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
      CuteQDeclarativeGeoLocationCall5 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall5>(taken[5]);
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
      CuteQDeclarativeGeoLocationCall6 call = reinterpret_cast<CuteQDeclarativeGeoLocationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoLocation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QDeclarativeGeoLocation10metaObjectEv(
    const QDeclarativeGeoLocation *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoLocation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QDeclarativeGeoLocation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoLocation::tr(s, c, n));
}

//  QDeclarativeGeoLocation::QDeclarativeGeoLocation(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoLocation *ritual_ZN23QDeclarativeGeoLocationC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeoLocation(parent);
}

//  QDeclarativeGeoLocation::QDeclarativeGeoLocation(const QGeoLocation &src,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoLocation *ritual_ZN23QDeclarativeGeoLocationC1ERK12QGeoLocationP7QObject(
    const QGeoLocation *src,
    QObject *parent) {
  return new CuteQDeclarativeGeoLocation(*src, parent);
}

//  QDeclarativeGeoLocation::~QDeclarativeGeoLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocationD1Ev(QDeclarativeGeoLocation *self) {
  delete self;
}

//  QGeoLocation QDeclarativeGeoLocation::location() const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZNK23QDeclarativeGeoLocation8locationEv(
    const QDeclarativeGeoLocation *self) {
  return new QGeoLocation(self->location());
}

//  void QDeclarativeGeoLocation::setLocation(const QGeoLocation &src)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation11setLocationERK12QGeoLocation(
    QDeclarativeGeoLocation *self,
    const QGeoLocation *src) {
  self->setLocation(*src);
}

//  QDeclarativeGeoAddress *QDeclarativeGeoLocation::address() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoAddress *ritual_ZNK23QDeclarativeGeoLocation7addressEv(
    const QDeclarativeGeoLocation *self) {
  return self->address();
}

//  void QDeclarativeGeoLocation::setAddress(QDeclarativeGeoAddress *address)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation10setAddressEP22QDeclarativeGeoAddress(
    QDeclarativeGeoLocation *self,
    QDeclarativeGeoAddress *address) {
  self->setAddress(address);
}

//  QGeoCoordinate QDeclarativeGeoLocation::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK23QDeclarativeGeoLocation10coordinateEv(
    const QDeclarativeGeoLocation *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  void QDeclarativeGeoLocation::setCoordinate(const QGeoCoordinate
//      coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation13setCoordinateE14QGeoCoordinate(
    QDeclarativeGeoLocation *self,
    const QGeoCoordinate *coordinate) {
  self->setCoordinate(*coordinate);
}

//  QGeoShape QDeclarativeGeoLocation::boundingShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK23QDeclarativeGeoLocation13boundingShapeEv(
    const QDeclarativeGeoLocation *self) {
  return new QGeoShape(self->boundingShape());
}

//  void QDeclarativeGeoLocation::setBoundingShape(const QGeoShape
//      &boundingShape)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation16setBoundingShapeERK9QGeoShape(
    QDeclarativeGeoLocation *self,
    const QGeoShape *boundingShape) {
  self->setBoundingShape(*boundingShape);
}

//  QVariantMap QDeclarativeGeoLocation::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK23QDeclarativeGeoLocation18extendedAttributesEv(
    const QDeclarativeGeoLocation *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  void QDeclarativeGeoLocation::setExtendedAttributes(const QVariantMap
//      &attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QDeclarativeGeoLocation *self,
    const QMap<QString, QVariant> *attributes) {
  self->setExtendedAttributes(*attributes);
}

//  void QDeclarativeGeoLocation::setLocationInternal(const QGeoLocation
//      &src)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDeclarativeGeoLocation19setLocationInternalERK12QGeoLocation(
    QDeclarativeGeoLocation *self,
    const QGeoLocation *src) {
  self->setLocationInternal(*src);
}

//  a Python function taken by a CuteQDeclarativeGeoLocation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoLocation(
    QDeclarativeGeoLocation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoLocation *>(self)->take(key, call);
}
