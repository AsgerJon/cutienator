//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorglobal_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QmlSensorGlobal that Python can take functions over in. Every QmlSensorGlobal
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorGlobalCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorGlobalCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorGlobalCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorGlobalCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorGlobalCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorGlobalCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorGlobalCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlSensorGlobal : public QmlSensorGlobal {
public:
  using QmlSensorGlobal::QmlSensorGlobal;
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
      CuteQmlSensorGlobalCall0 call = reinterpret_cast<CuteQmlSensorGlobalCall0>(taken[0]);
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
      CuteQmlSensorGlobalCall1 call = reinterpret_cast<CuteQmlSensorGlobalCall1>(taken[1]);
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
      CuteQmlSensorGlobalCall2 call = reinterpret_cast<CuteQmlSensorGlobalCall2>(taken[2]);
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
      CuteQmlSensorGlobalCall3 call = reinterpret_cast<CuteQmlSensorGlobalCall3>(taken[3]);
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
      CuteQmlSensorGlobalCall4 call = reinterpret_cast<CuteQmlSensorGlobalCall4>(taken[4]);
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
      CuteQmlSensorGlobalCall5 call = reinterpret_cast<CuteQmlSensorGlobalCall5>(taken[5]);
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
      CuteQmlSensorGlobalCall6 call = reinterpret_cast<CuteQmlSensorGlobalCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlSensorGlobal::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QmlSensorGlobal10metaObjectEv(
    const QmlSensorGlobal *self) {
  return self->metaObject();
}

//  QString QmlSensorGlobal::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QmlSensorGlobal2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlSensorGlobal::tr(s, c, n));
}

//  QmlSensorGlobal::QmlSensorGlobal(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlSensorGlobal *ritual_ZN15QmlSensorGlobalC1EP7QObject(QObject *parent) {
  return new CuteQmlSensorGlobal(parent);
}

//  QmlSensorGlobal::~QmlSensorGlobal()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QmlSensorGlobalD1Ev(QmlSensorGlobal *self) {
  delete self;
}

//  QStringList QmlSensorGlobal::sensorTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QmlSensorGlobal11sensorTypesEv(
    const QmlSensorGlobal *self) {
  return new QList<QString>(self->sensorTypes());
}

//  QStringList QmlSensorGlobal::sensorsForType(const QString &type) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QmlSensorGlobal14sensorsForTypeERK7QString(
    const QmlSensorGlobal *self,
    const QString *type) {
  return new QList<QString>(self->sensorsForType(*type));
}

//  QString QmlSensorGlobal::defaultSensorForType(const QString &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QmlSensorGlobal20defaultSensorForTypeERK7QString(
    const QmlSensorGlobal *self,
    const QString *type) {
  return new QString(self->defaultSensorForType(*type));
}

//  void QmlSensorGlobal::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QmlSensorGlobal22qt_qmlMarker_singletonEv(
    QmlSensorGlobal *self) {
  self->qt_qmlMarker_singleton();
}

//  a Python function taken by a CuteQmlSensorGlobal, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlSensorGlobal(
    QmlSensorGlobal *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlSensorGlobal *>(self)->take(key, call);
}
