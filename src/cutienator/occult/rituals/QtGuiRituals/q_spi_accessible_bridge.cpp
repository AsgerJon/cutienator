//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qspiaccessiblebridge_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qspiaccessiblebridge_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSpiAccessibleBridge that Python can take functions over in. Every QSpiAccessibleBridge
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void (*CuteQSpiAccessibleBridgeCall0)(const void *, QAccessibleEvent *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQSpiAccessibleBridgeCall1)(const void *, QObject *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQSpiAccessibleBridgeCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQSpiAccessibleBridgeCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpiAccessibleBridgeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpiAccessibleBridgeCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiAccessibleBridgeCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiAccessibleBridgeCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiAccessibleBridgeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiAccessibleBridgeCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpiAccessibleBridgeCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSpiAccessibleBridge : public QSpiAccessibleBridge {
public:
  using QSpiAccessibleBridge::QSpiAccessibleBridge;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility25notifyAccessibilityUpdateEP16QAccessibleEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility13setRootObjectEP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility10initializeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN22QPlatformAccessibility7cleanupEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  void QSpiAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
  //      *event)
  void notifyAccessibilityUpdate(QAccessibleEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall0 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSpiAccessibleBridge::notifyAccessibilityUpdate(event);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::setRootObject(QObject *o)
  void setRootObject(QObject *o) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall1 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall1>(taken[1]);
      call(this, o, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::setRootObject(o);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::initialize()
  void initialize() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall2 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::initialize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QPlatformAccessibility::cleanup()
  void cleanup() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall3 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformAccessibility::cleanup();
  }
#endif  // QT_CONFIG(accessibility)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall4 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall5 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall6 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall7 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall8 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall9 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSpiAccessibleBridgeCall10 call = reinterpret_cast<CuteQSpiAccessibleBridgeCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSpiAccessibleBridge::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QSpiAccessibleBridge10metaObjectEv(
    const QSpiAccessibleBridge *self) {
  return self->metaObject();
}

//  QString QSpiAccessibleBridge::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QSpiAccessibleBridge2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSpiAccessibleBridge::tr(s, c, n));
}

//  QSpiAccessibleBridge::QSpiAccessibleBridge()
extern "C" Q_DECL_EXPORT
QSpiAccessibleBridge *ritual_ZN20QSpiAccessibleBridgeC1Ev() {
  return new CuteQSpiAccessibleBridge();
}

//  QSpiAccessibleBridge::~QSpiAccessibleBridge()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpiAccessibleBridgeD1Ev(QSpiAccessibleBridge *self) {
  delete self;
}

//  void QSpiAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpiAccessibleBridge25notifyAccessibilityUpdateEP16QAccessibleEvent(
    QSpiAccessibleBridge *self,
    QAccessibleEvent *event) {
  self->notifyAccessibilityUpdate(event);
}

//  QDBusConnection QSpiAccessibleBridge::dBusConnection() const
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZNK20QSpiAccessibleBridge14dBusConnectionEv(
    const QSpiAccessibleBridge *self) {
  return new QDBusConnection(self->dBusConnection());
}

//  QSpiAccessibleBridge *QSpiAccessibleBridge::instance()
extern "C" Q_DECL_EXPORT
QSpiAccessibleBridge *ritual_ZN20QSpiAccessibleBridge8instanceEv() {
  return QSpiAccessibleBridge::instance();
}

//  void QSpiAccessibleBridge::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpiAccessibleBridge14enabledChangedEb(
    QSpiAccessibleBridge *self,
    bool enabled) {
  self->enabledChanged(enabled);
}

//  void QSpiAccessibleBridge::initializeConstantMappings()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpiAccessibleBridge26initializeConstantMappingsEv(
    QSpiAccessibleBridge *self) {
  self->initializeConstantMappings();
}

//  void QSpiAccessibleBridge::updateStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSpiAccessibleBridge12updateStatusEv(
    QSpiAccessibleBridge *self) {
  self->updateStatus();
}

//  QSpiAccessibleBridge as the QPlatformAccessibility it is built on
extern "C" Q_DECL_EXPORT
QPlatformAccessibility *ritual_cast_QSpiAccessibleBridge_QPlatformAccessibility(
    QSpiAccessibleBridge *self) {
  return static_cast<QPlatformAccessibility *>(self);
}

//  a Python function taken by a CuteQSpiAccessibleBridge, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpiAccessibleBridge(
    QSpiAccessibleBridge *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpiAccessibleBridge *>(self)->take(key, call);
}

//  void QSpiAccessibleBridge::notifyAccessibilityUpdate(QAccessibleEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSpiAccessibleBridge25notifyAccessibilityUpdateEP16QAccessibleEvent(
    QSpiAccessibleBridge *self,
    QAccessibleEvent *event) {
  self->QSpiAccessibleBridge::notifyAccessibilityUpdate(event);
}

#endif  // QT_CONFIG(accessibility)
