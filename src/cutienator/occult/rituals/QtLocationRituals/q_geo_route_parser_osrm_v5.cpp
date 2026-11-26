//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoRouteParserOsrmV5 that Python can take functions over in. Every QGeoRouteParserOsrmV5
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteParserOsrmV5Call0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteParserOsrmV5Call1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserOsrmV5Call2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserOsrmV5Call3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserOsrmV5Call4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserOsrmV5Call5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserOsrmV5Call6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoRouteParserOsrmV5 : public QGeoRouteParserOsrmV5 {
public:
  using QGeoRouteParserOsrmV5::QGeoRouteParserOsrmV5;
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
      CuteQGeoRouteParserOsrmV5Call0 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call0>(taken[0]);
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
      CuteQGeoRouteParserOsrmV5Call1 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call1>(taken[1]);
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
      CuteQGeoRouteParserOsrmV5Call2 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call2>(taken[2]);
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
      CuteQGeoRouteParserOsrmV5Call3 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call3>(taken[3]);
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
      CuteQGeoRouteParserOsrmV5Call4 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call4>(taken[4]);
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
      CuteQGeoRouteParserOsrmV5Call5 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call5>(taken[5]);
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
      CuteQGeoRouteParserOsrmV5Call6 call = reinterpret_cast<CuteQGeoRouteParserOsrmV5Call6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoRouteParserOsrmV5::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGeoRouteParserOsrmV510metaObjectEv(
    const QGeoRouteParserOsrmV5 *self) {
  return self->metaObject();
}

//  void *QGeoRouteParserOsrmV5::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QGeoRouteParserOsrmV511qt_metacastEPKc(
    QGeoRouteParserOsrmV5 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoRouteParserOsrmV5::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QGeoRouteParserOsrmV511qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoRouteParserOsrmV5 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoRouteParserOsrmV5::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGeoRouteParserOsrmV52trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoRouteParserOsrmV5::tr(s, c, n));
}

//  QGeoRouteParserOsrmV5Private *QGeoRouteParserOsrmV5::d_func()
extern "C" Q_DECL_EXPORT
QGeoRouteParserOsrmV5Private *ritual_ZN21QGeoRouteParserOsrmV56d_funcEv(
    QGeoRouteParserOsrmV5 *self) {
  return self->d_func();
}

//  const QGeoRouteParserOsrmV5Private *QGeoRouteParserOsrmV5::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoRouteParserOsrmV5Private *ritual_ZNK21QGeoRouteParserOsrmV56d_funcEv(
    const QGeoRouteParserOsrmV5 *self) {
  return self->d_func();
}

//  QGeoRouteParserOsrmV5::QGeoRouteParserOsrmV5(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoRouteParserOsrmV5 *ritual_ZN21QGeoRouteParserOsrmV5C1EP7QObject(
    QObject *parent) {
  return new CuteQGeoRouteParserOsrmV5(parent);
}

//  QGeoRouteParserOsrmV5::~QGeoRouteParserOsrmV5()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoRouteParserOsrmV5D1Ev(QGeoRouteParserOsrmV5 *self) {
  delete self;
}

//  void QGeoRouteParserOsrmV5::setExtension(const
//      QGeoRouteParserOsrmV5Extension *extension)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoRouteParserOsrmV512setExtensionEPK30QGeoRouteParserOsrmV5Extension(
    QGeoRouteParserOsrmV5 *self,
    const QGeoRouteParserOsrmV5Extension *extension) {
  self->setExtension(extension);
}

//  a Python function taken by a CuteQGeoRouteParserOsrmV5, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRouteParserOsrmV5(
    QGeoRouteParserOsrmV5 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRouteParserOsrmV5 *>(self)->take(key, call);
}
