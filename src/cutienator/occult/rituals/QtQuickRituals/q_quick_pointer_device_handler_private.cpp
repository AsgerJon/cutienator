//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerdevicehandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickPointerDeviceHandlerPrivate that Python can take functions over in. Every QQuickPointerDeviceHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPointerDeviceHandlerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPointerDeviceHandlerPrivateCall1)(const void *, int *);
class CuteQQuickPointerDeviceHandlerPrivate : public QQuickPointerDeviceHandlerPrivate {
public:
  using QQuickPointerDeviceHandlerPrivate::QQuickPointerDeviceHandlerPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickPointerHandlerPrivate::onParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void onParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerPrivateCall0 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerPrivateCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
  }

  //  void QQuickPointerHandlerPrivate::onEnabledChanged()
  void onEnabledChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPointerDeviceHandlerPrivateCall1 call = reinterpret_cast<CuteQQuickPointerDeviceHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onEnabledChanged();
  }
};

//  QQuickPointerDeviceHandler *QQuickPointerDeviceHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPointerDeviceHandler *ritual_ZN33QQuickPointerDeviceHandlerPrivate6q_funcEv(
    QQuickPointerDeviceHandlerPrivate *self) {
  return self->q_func();
}

//  const QQuickPointerDeviceHandler
//      *QQuickPointerDeviceHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPointerDeviceHandler *ritual_ZNK33QQuickPointerDeviceHandlerPrivate6q_funcEv(
    const QQuickPointerDeviceHandlerPrivate *self) {
  return self->q_func();
}

//  QQuickPointerDeviceHandlerPrivate
//      *QQuickPointerDeviceHandlerPrivate::get(QQuickPointerDeviceHandler
//      *q)
extern "C" Q_DECL_EXPORT
QQuickPointerDeviceHandlerPrivate *ritual_ZN33QQuickPointerDeviceHandlerPrivate3getEP26QQuickPointerDeviceHandler(
    QQuickPointerDeviceHandler *q) {
  return QQuickPointerDeviceHandlerPrivate::get(q);
}

//  const QQuickPointerDeviceHandlerPrivate
//      *QQuickPointerDeviceHandlerPrivate::get(const
//      QQuickPointerDeviceHandler *q)
extern "C" Q_DECL_EXPORT
const QQuickPointerDeviceHandlerPrivate *ritual_ZN33QQuickPointerDeviceHandlerPrivate3getEPK26QQuickPointerDeviceHandler(
    const QQuickPointerDeviceHandler *q) {
  return QQuickPointerDeviceHandlerPrivate::get(q);
}

//  a Python function taken by a CuteQQuickPointerDeviceHandlerPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPointerDeviceHandlerPrivate(
    QQuickPointerDeviceHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPointerDeviceHandlerPrivate *>(self)->take(key, call);
}
