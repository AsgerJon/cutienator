//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlhardwarelayerintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlhardwarelayerintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtWayland::HardwareLayerIntegration that Python can take functions over in. Every QtWayland::HardwareLayerIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall0)(const void *, QWaylandQuickHardwareLayer *, int *);
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall1)(const void *, QWaylandQuickHardwareLayer *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_HardwareLayerIntegrationCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_HardwareLayerIntegrationCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_HardwareLayerIntegrationCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_HardwareLayerIntegration : public QtWayland::HardwareLayerIntegration {
public:
  using QtWayland::HardwareLayerIntegration::HardwareLayerIntegration;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtWayland24HardwareLayerIntegration3addEP26QWaylandQuickHardwareLayer")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland24HardwareLayerIntegration6removeEP26QWaylandQuickHardwareLayer")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void
  //      QtWayland::HardwareLayerIntegration::add(QWaylandQuickHardwareLay
  //      er *a0)
  void add(QWaylandQuickHardwareLayer *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall0 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QtWayland::HardwareLayerIntegration::add(a0);
  }

  //  void QtWayland::HardwareLayerIntegration::remove(QWaylandQuickHardwar
  //      eLayer *a0)
  void remove(QWaylandQuickHardwareLayer *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall1 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QtWayland::HardwareLayerIntegration::remove(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall2 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall3 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall4 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall5 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall6 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall7 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtWayland_HardwareLayerIntegrationCall8 call = reinterpret_cast<CuteQtWayland_HardwareLayerIntegrationCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::HardwareLayerIntegration::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland24HardwareLayerIntegration10metaObjectEv(
    const QtWayland::HardwareLayerIntegration *self) {
  return self->metaObject();
}

//  QString QtWayland::HardwareLayerIntegration::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland24HardwareLayerIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::HardwareLayerIntegration::tr(s, c, n));
}

//  QtWayland::HardwareLayerIntegration::HardwareLayerIntegration(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtWayland::HardwareLayerIntegration *ritual_ZN9QtWayland24HardwareLayerIntegrationC1EP7QObject(
    QObject *parent) {
  return new CuteQtWayland_HardwareLayerIntegration(parent);
}

//  QtWayland::HardwareLayerIntegration::~HardwareLayerIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24HardwareLayerIntegrationD1Ev(
    QtWayland::HardwareLayerIntegration *self) {
  delete self;
}

//  void QtWayland::HardwareLayerIntegration::add(QWaylandQuickHardwareLayer
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24HardwareLayerIntegration3addEP26QWaylandQuickHardwareLayer(
    QtWayland::HardwareLayerIntegration *self,
    QWaylandQuickHardwareLayer *a0) {
  self->add(a0);
}

//  void
//      QtWayland::HardwareLayerIntegration::remove(QWaylandQuickHardwareLaye
//      r *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland24HardwareLayerIntegration6removeEP26QWaylandQuickHardwareLayer(
    QtWayland::HardwareLayerIntegration *self,
    QWaylandQuickHardwareLayer *a0) {
  self->remove(a0);
}

//  a Python function taken by a CuteQtWayland_HardwareLayerIntegration, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_HardwareLayerIntegration(
    QtWayland::HardwareLayerIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_HardwareLayerIntegration *>(self)->take(key, call);
}

//  void QtWayland::HardwareLayerIntegration::add(QWaylandQuickHardwareLayer
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtWayland24HardwareLayerIntegration3addEP26QWaylandQuickHardwareLayer(
    QtWayland::HardwareLayerIntegration *self,
    QWaylandQuickHardwareLayer *a0) {
  self->QtWayland::HardwareLayerIntegration::add(a0);
}

//  void
//      QtWayland::HardwareLayerIntegration::remove(QWaylandQuickHardwareLaye
//      r *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtWayland24HardwareLayerIntegration6removeEP26QWaylandQuickHardwareLayer(
    QtWayland::HardwareLayerIntegration *self,
    QWaylandQuickHardwareLayer *a0) {
  self->QtWayland::HardwareLayerIntegration::remove(a0);
}

#endif  // QT_CONFIG(opengl)
