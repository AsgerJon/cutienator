//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinateobject_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeocoordinateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoCoordinateObject that Python can take functions over in. Every QGeoCoordinateObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCoordinateObjectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCoordinateObjectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCoordinateObjectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCoordinateObjectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCoordinateObjectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCoordinateObjectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCoordinateObjectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoCoordinateObject : public QGeoCoordinateObject {
public:
  using QGeoCoordinateObject::QGeoCoordinateObject;
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
      CuteQGeoCoordinateObjectCall0 call = reinterpret_cast<CuteQGeoCoordinateObjectCall0>(taken[0]);
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
      CuteQGeoCoordinateObjectCall1 call = reinterpret_cast<CuteQGeoCoordinateObjectCall1>(taken[1]);
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
      CuteQGeoCoordinateObjectCall2 call = reinterpret_cast<CuteQGeoCoordinateObjectCall2>(taken[2]);
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
      CuteQGeoCoordinateObjectCall3 call = reinterpret_cast<CuteQGeoCoordinateObjectCall3>(taken[3]);
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
      CuteQGeoCoordinateObjectCall4 call = reinterpret_cast<CuteQGeoCoordinateObjectCall4>(taken[4]);
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
      CuteQGeoCoordinateObjectCall5 call = reinterpret_cast<CuteQGeoCoordinateObjectCall5>(taken[5]);
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
      CuteQGeoCoordinateObjectCall6 call = reinterpret_cast<CuteQGeoCoordinateObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoCoordinateObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QGeoCoordinateObject10metaObjectEv(
    const QGeoCoordinateObject *self) {
  return self->metaObject();
}

//  QString QGeoCoordinateObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QGeoCoordinateObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoCoordinateObject::tr(s, c, n));
}

//  QGeoCoordinateObject::QGeoCoordinateObject(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCoordinateObject *ritual_ZN20QGeoCoordinateObjectC1EP7QObject(
    QObject *parent) {
  return new CuteQGeoCoordinateObject(parent);
}

//  QGeoCoordinateObject::QGeoCoordinateObject(const QGeoCoordinate &c,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCoordinateObject *ritual_ZN20QGeoCoordinateObjectC1ERK14QGeoCoordinateP7QObject(
    const QGeoCoordinate *c,
    QObject *parent) {
  return new CuteQGeoCoordinateObject(*c, parent);
}

//  QGeoCoordinateObject::~QGeoCoordinateObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoCoordinateObjectD1Ev(QGeoCoordinateObject *self) {
  delete self;
}

//  bool QGeoCoordinateObject::operator==(const QGeoCoordinate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoCoordinateObjecteqERK14QGeoCoordinate(
    const QGeoCoordinateObject *self,
    const QGeoCoordinate *other) {
  return self->operator==(*other);
}

//  bool QGeoCoordinateObject::operator!=(const QGeoCoordinate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoCoordinateObjectneERK14QGeoCoordinate(
    const QGeoCoordinateObject *self,
    const QGeoCoordinate *other) {
  return self->operator!=(*other);
}

//  QGeoCoordinate QGeoCoordinateObject::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK20QGeoCoordinateObject10coordinateEv(
    const QGeoCoordinateObject *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  void QGeoCoordinateObject::setCoordinate(const QGeoCoordinate &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoCoordinateObject13setCoordinateERK14QGeoCoordinate(
    QGeoCoordinateObject *self,
    const QGeoCoordinate *c) {
  self->setCoordinate(*c);
}

//  a Python function taken by a CuteQGeoCoordinateObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoCoordinateObject(
    QGeoCoordinateObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoCoordinateObject *>(self)->take(key, call);
}
