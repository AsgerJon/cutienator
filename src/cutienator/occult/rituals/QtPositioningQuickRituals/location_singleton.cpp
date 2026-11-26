//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/locationsingleton_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/locationsingleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qvariant.h>
#include <QtPositioning/qgeocircle.h>
#include <QtPositioning/qgeopath.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtPositioning/qgeopolygon.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A LocationSingleton that Python can take functions over in. Every LocationSingleton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocationSingletonCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocationSingletonCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocationSingletonCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocationSingletonCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocationSingletonCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocationSingletonCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocationSingletonCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLocationSingleton : public LocationSingleton {
public:
  using LocationSingleton::LocationSingleton;
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
      CuteLocationSingletonCall0 call = reinterpret_cast<CuteLocationSingletonCall0>(taken[0]);
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
      CuteLocationSingletonCall1 call = reinterpret_cast<CuteLocationSingletonCall1>(taken[1]);
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
      CuteLocationSingletonCall2 call = reinterpret_cast<CuteLocationSingletonCall2>(taken[2]);
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
      CuteLocationSingletonCall3 call = reinterpret_cast<CuteLocationSingletonCall3>(taken[3]);
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
      CuteLocationSingletonCall4 call = reinterpret_cast<CuteLocationSingletonCall4>(taken[4]);
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
      CuteLocationSingletonCall5 call = reinterpret_cast<CuteLocationSingletonCall5>(taken[5]);
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
      CuteLocationSingletonCall6 call = reinterpret_cast<CuteLocationSingletonCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LocationSingleton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17LocationSingleton10metaObjectEv(
    const LocationSingleton *self) {
  return self->metaObject();
}

//  void *LocationSingleton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17LocationSingleton11qt_metacastEPKc(
    LocationSingleton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LocationSingleton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17LocationSingleton11qt_metacallEN11QMetaObject4CallEiPPv(
    LocationSingleton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LocationSingleton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17LocationSingleton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LocationSingleton::tr(s, c, n));
}

//  void LocationSingleton::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN17LocationSingleton22qt_qmlMarker_singletonEv(
    LocationSingleton *self) {
  self->qt_qmlMarker_singleton();
}

//  LocationSingleton::LocationSingleton(QObject *parent)
extern "C" Q_DECL_EXPORT
LocationSingleton *ritual_ZN17LocationSingletonC1EP7QObject(
    QObject *parent) {
  return new CuteLocationSingleton(parent);
}

//  QGeoCoordinate LocationSingleton::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK17LocationSingleton10coordinateEv(
    const LocationSingleton *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  QGeoCoordinate LocationSingleton::coordinate(double latitude, double
//      longitude, double altitude) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK17LocationSingleton10coordinateEddd(
    const LocationSingleton *self,
    double latitude,
    double longitude,
    double altitude) {
  return new QGeoCoordinate(self->coordinate(latitude, longitude, altitude));
}

//  QGeoShape LocationSingleton::shape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK17LocationSingleton5shapeEv(
    const LocationSingleton *self) {
  return new QGeoShape(self->shape());
}

//  QGeoRectangle LocationSingleton::rectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17LocationSingleton9rectangleEv(
    const LocationSingleton *self) {
  return new QGeoRectangle(self->rectangle());
}

//  QGeoRectangle LocationSingleton::rectangle(const QGeoCoordinate &center,
//      double width, double height) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17LocationSingleton9rectangleERK14QGeoCoordinatedd(
    const LocationSingleton *self,
    const QGeoCoordinate *center,
    double width,
    double height) {
  return new QGeoRectangle(self->rectangle(*center, width, height));
}

//  QGeoRectangle LocationSingleton::rectangle(const QGeoCoordinate &topLeft,
//      const QGeoCoordinate &bottomRight) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17LocationSingleton9rectangleERK14QGeoCoordinateS2_(
    const LocationSingleton *self,
    const QGeoCoordinate *topLeft,
    const QGeoCoordinate *bottomRight) {
  return new QGeoRectangle(self->rectangle(*topLeft, *bottomRight));
}

//  QGeoRectangle LocationSingleton::rectangle(const QVariantList
//      &coordinates) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17LocationSingleton9rectangleERK5QListI8QVariantE(
    const LocationSingleton *self,
    const QList<QVariant> *coordinates) {
  return new QGeoRectangle(self->rectangle(*coordinates));
}

//  QGeoCircle LocationSingleton::circle() const
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZNK17LocationSingleton6circleEv(
    const LocationSingleton *self) {
  return new QGeoCircle(self->circle());
}

//  QGeoCircle LocationSingleton::circle(const QGeoCoordinate &center, qreal
//      radius) const
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZNK17LocationSingleton6circleERK14QGeoCoordinated(
    const LocationSingleton *self,
    const QGeoCoordinate *center,
    qreal radius) {
  return new QGeoCircle(self->circle(*center, radius));
}

//  QGeoPath LocationSingleton::path() const
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZNK17LocationSingleton4pathEv(
    const LocationSingleton *self) {
  return new QGeoPath(self->path());
}

//  QGeoPath LocationSingleton::path(const QJSValue &value, qreal width)
//      const
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZNK17LocationSingleton4pathERK8QJSValued(
    const LocationSingleton *self,
    const QJSValue *value,
    qreal width) {
  return new QGeoPath(self->path(*value, width));
}

//  QGeoPolygon LocationSingleton::polygon() const
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZNK17LocationSingleton7polygonEv(
    const LocationSingleton *self) {
  return new QGeoPolygon(self->polygon());
}

//  QGeoPolygon LocationSingleton::polygon(const QVariantList &value) const
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZNK17LocationSingleton7polygonERK5QListI8QVariantE(
    const LocationSingleton *self,
    const QList<QVariant> *value) {
  return new QGeoPolygon(self->polygon(*value));
}

//  QGeoPolygon LocationSingleton::polygon(const QVariantList &perimeter,
//      const QVariantList &holes) const
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZNK17LocationSingleton7polygonERK5QListI8QVariantES4_(
    const LocationSingleton *self,
    const QList<QVariant> *perimeter,
    const QList<QVariant> *holes) {
  return new QGeoPolygon(self->polygon(*perimeter, *holes));
}

//  QGeoCircle LocationSingleton::shapeToCircle(const QGeoShape &shape) const
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZNK17LocationSingleton13shapeToCircleERK9QGeoShape(
    const LocationSingleton *self,
    const QGeoShape *shape) {
  return new QGeoCircle(self->shapeToCircle(*shape));
}

//  QGeoRectangle LocationSingleton::shapeToRectangle(const QGeoShape &shape)
//      const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17LocationSingleton16shapeToRectangleERK9QGeoShape(
    const LocationSingleton *self,
    const QGeoShape *shape) {
  return new QGeoRectangle(self->shapeToRectangle(*shape));
}

//  QGeoPath LocationSingleton::shapeToPath(const QGeoShape &shape) const
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZNK17LocationSingleton11shapeToPathERK9QGeoShape(
    const LocationSingleton *self,
    const QGeoShape *shape) {
  return new QGeoPath(self->shapeToPath(*shape));
}

//  QGeoPolygon LocationSingleton::shapeToPolygon(const QGeoShape &shape)
//      const
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZNK17LocationSingleton14shapeToPolygonERK9QGeoShape(
    const LocationSingleton *self,
    const QGeoShape *shape) {
  return new QGeoPolygon(self->shapeToPolygon(*shape));
}

//  QGeoCoordinate LocationSingleton::mercatorToCoord(const QPointF
//      &mercator) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK17LocationSingleton15mercatorToCoordERK7QPointF(
    const LocationSingleton *self,
    const QPointF *mercator) {
  return new QGeoCoordinate(self->mercatorToCoord(*mercator));
}

//  QPointF LocationSingleton::coordToMercator(const QGeoCoordinate &coord)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17LocationSingleton15coordToMercatorERK14QGeoCoordinate(
    const LocationSingleton *self,
    const QGeoCoordinate *coord) {
  return new QPointF(self->coordToMercator(*coord));
}

//  a Python function taken by a CuteLocationSingleton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LocationSingleton(
    LocationSingleton *self,
    const char *key,
    void *call) {
  return static_cast<CuteLocationSingleton *>(self)->take(key, call);
}
