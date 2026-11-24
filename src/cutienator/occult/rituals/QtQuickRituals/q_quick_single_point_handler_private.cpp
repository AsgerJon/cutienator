//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickSinglePointHandlerPrivate that Python can take functions over in. Every QQuickSinglePointHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSinglePointHandlerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSinglePointHandlerPrivateCall1)(const void *, int *);
class CuteQQuickSinglePointHandlerPrivate : public QQuickSinglePointHandlerPrivate {
public:
  using QQuickSinglePointHandlerPrivate::QQuickSinglePointHandlerPrivate;
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
      CuteQQuickSinglePointHandlerPrivateCall0 call = reinterpret_cast<CuteQQuickSinglePointHandlerPrivateCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
  }

  //  void QQuickPointerHandlerPrivate::onEnabledChanged()
  void onEnabledChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerPrivateCall1 call = reinterpret_cast<CuteQQuickSinglePointHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onEnabledChanged();
  }
};

//  QQuickSinglePointHandler *QQuickSinglePointHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSinglePointHandler *ritual_ZN31QQuickSinglePointHandlerPrivate6q_funcEv(
    QQuickSinglePointHandlerPrivate *self) {
  return self->q_func();
}

//  const QQuickSinglePointHandler *QQuickSinglePointHandlerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSinglePointHandler *ritual_ZNK31QQuickSinglePointHandlerPrivate6q_funcEv(
    const QQuickSinglePointHandlerPrivate *self) {
  return self->q_func();
}

//  QQuickSinglePointHandlerPrivate
//      *QQuickSinglePointHandlerPrivate::get(QQuickSinglePointHandler *q)
extern "C" Q_DECL_EXPORT
QQuickSinglePointHandlerPrivate *ritual_ZN31QQuickSinglePointHandlerPrivate3getEP24QQuickSinglePointHandler(
    QQuickSinglePointHandler *q) {
  return QQuickSinglePointHandlerPrivate::get(q);
}

//  const QQuickSinglePointHandlerPrivate
//      *QQuickSinglePointHandlerPrivate::get(const QQuickSinglePointHandler
//      *q)
extern "C" Q_DECL_EXPORT
const QQuickSinglePointHandlerPrivate *ritual_ZN31QQuickSinglePointHandlerPrivate3getEPK24QQuickSinglePointHandler(
    const QQuickSinglePointHandler *q) {
  return QQuickSinglePointHandlerPrivate::get(q);
}

//  QQuickSinglePointHandlerPrivate::QQuickSinglePointHandlerPrivate()
extern "C" Q_DECL_EXPORT
QQuickSinglePointHandlerPrivate *ritual_ZN31QQuickSinglePointHandlerPrivateC1Ev() {
  return new CuteQQuickSinglePointHandlerPrivate();
}

//  void QQuickSinglePointHandlerPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSinglePointHandlerPrivate5resetEv(
    QQuickSinglePointHandlerPrivate *self) {
  self->reset();
}

//  a Python function taken by a CuteQQuickSinglePointHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSinglePointHandlerPrivate(
    QQuickSinglePointHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSinglePointHandlerPrivate *>(self)->take(key, call);
}
