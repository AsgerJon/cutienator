//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickMultiPointHandlerPrivate that Python can take functions over in. Every QQuickMultiPointHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMultiPointHandlerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickMultiPointHandlerPrivateCall1)(const void *, int *);
class CuteQQuickMultiPointHandlerPrivate : public QQuickMultiPointHandlerPrivate {
public:
  using QQuickMultiPointHandlerPrivate::QQuickMultiPointHandlerPrivate;
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
      CuteQQuickMultiPointHandlerPrivateCall0 call = reinterpret_cast<CuteQQuickMultiPointHandlerPrivateCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
  }

  //  void QQuickPointerHandlerPrivate::onEnabledChanged()
  void onEnabledChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerPrivateCall1 call = reinterpret_cast<CuteQQuickMultiPointHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onEnabledChanged();
  }
};

//  QQuickMultiPointHandler *QQuickMultiPointHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMultiPointHandler *ritual_ZN30QQuickMultiPointHandlerPrivate6q_funcEv(
    QQuickMultiPointHandlerPrivate *self) {
  return self->q_func();
}

//  const QQuickMultiPointHandler *QQuickMultiPointHandlerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMultiPointHandler *ritual_ZNK30QQuickMultiPointHandlerPrivate6q_funcEv(
    const QQuickMultiPointHandlerPrivate *self) {
  return self->q_func();
}

//  QQuickMultiPointHandlerPrivate
//      *QQuickMultiPointHandlerPrivate::get(QQuickMultiPointHandler *q)
extern "C" Q_DECL_EXPORT
QQuickMultiPointHandlerPrivate *ritual_ZN30QQuickMultiPointHandlerPrivate3getEP23QQuickMultiPointHandler(
    QQuickMultiPointHandler *q) {
  return QQuickMultiPointHandlerPrivate::get(q);
}

//  const QQuickMultiPointHandlerPrivate
//      *QQuickMultiPointHandlerPrivate::get(const QQuickMultiPointHandler
//      *q)
extern "C" Q_DECL_EXPORT
const QQuickMultiPointHandlerPrivate *ritual_ZN30QQuickMultiPointHandlerPrivate3getEPK23QQuickMultiPointHandler(
    const QQuickMultiPointHandler *q) {
  return QQuickMultiPointHandlerPrivate::get(q);
}

//  QQuickMultiPointHandlerPrivate::QQuickMultiPointHandlerPrivate(int
//      minPointCount, int maxPointCount)
extern "C" Q_DECL_EXPORT
QQuickMultiPointHandlerPrivate *ritual_ZN30QQuickMultiPointHandlerPrivateC1Eii(
    int minPointCount,
    int maxPointCount) {
  return new CuteQQuickMultiPointHandlerPrivate(
      minPointCount,
      maxPointCount);
}

//  a Python function taken by a CuteQQuickMultiPointHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMultiPointHandlerPrivate(
    QQuickMultiPointHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMultiPointHandlerPrivate *>(self)->take(key, call);
}
