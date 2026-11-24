//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qeventpoint.h>
#include <cstring>

//  A QQuickPointerHandlerPrivate that Python can take functions over in. Every QQuickPointerHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPointerHandlerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPointerHandlerPrivateCall1)(const void *, int *);
class CuteQQuickPointerHandlerPrivate : public QQuickPointerHandlerPrivate {
public:
  using QQuickPointerHandlerPrivate::QQuickPointerHandlerPrivate;
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
      CuteQQuickPointerHandlerPrivateCall0 call = reinterpret_cast<CuteQQuickPointerHandlerPrivateCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
  }

  //  void QQuickPointerHandlerPrivate::onEnabledChanged()
  void onEnabledChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPointerHandlerPrivateCall1 call = reinterpret_cast<CuteQQuickPointerHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onEnabledChanged();
  }
};

//  QQuickPointerHandler *QQuickPointerHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPointerHandler *ritual_ZN27QQuickPointerHandlerPrivate6q_funcEv(
    QQuickPointerHandlerPrivate *self) {
  return self->q_func();
}

//  const QQuickPointerHandler *QQuickPointerHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPointerHandler *ritual_ZNK27QQuickPointerHandlerPrivate6q_funcEv(
    const QQuickPointerHandlerPrivate *self) {
  return self->q_func();
}

//  QQuickPointerHandlerPrivate
//      *QQuickPointerHandlerPrivate::get(QQuickPointerHandler *q)
extern "C" Q_DECL_EXPORT
QQuickPointerHandlerPrivate *ritual_ZN27QQuickPointerHandlerPrivate3getEP20QQuickPointerHandler(
    QQuickPointerHandler *q) {
  return QQuickPointerHandlerPrivate::get(q);
}

//  const QQuickPointerHandlerPrivate *QQuickPointerHandlerPrivate::get(const
//      QQuickPointerHandler *q)
extern "C" Q_DECL_EXPORT
const QQuickPointerHandlerPrivate *ritual_ZN27QQuickPointerHandlerPrivate3getEPK20QQuickPointerHandler(
    const QQuickPointerHandler *q) {
  return QQuickPointerHandlerPrivate::get(q);
}

//  QQuickPointerHandlerPrivate::QQuickPointerHandlerPrivate()
extern "C" Q_DECL_EXPORT
QQuickPointerHandlerPrivate *ritual_ZN27QQuickPointerHandlerPrivateC1Ev() {
  return new CuteQQuickPointerHandlerPrivate();
}

//  bool QQuickPointerHandlerPrivate::dragOverThreshold(QVector2D delta)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickPointerHandlerPrivate17dragOverThresholdE9QVector2D(
    const QQuickPointerHandlerPrivate *self,
    const QVector2D *delta) {
  return self->dragOverThreshold(*delta);
}

//  bool QQuickPointerHandlerPrivate::dragOverThreshold(const QEventPoint
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickPointerHandlerPrivate17dragOverThresholdERK11QEventPoint(
    const QQuickPointerHandlerPrivate *self,
    const QEventPoint *point) {
  return self->dragOverThreshold(*point);
}

//  void QQuickPointerHandlerPrivate::onParentChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10QQuickItemS1_(
    QQuickPointerHandlerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->onParentChanged(a0, a1);
}

//  void QQuickPointerHandlerPrivate::onEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv(
    QQuickPointerHandlerPrivate *self) {
  self->onEnabledChanged();
}

//  a Python function taken by a CuteQQuickPointerHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPointerHandlerPrivate(
    QQuickPointerHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPointerHandlerPrivate *>(self)->take(key, call);
}

//  void QQuickPointerHandlerPrivate::onParentChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickPointerHandlerPrivate15onParentChangedEP10QQuickItemS1_(
    QQuickPointerHandlerPrivate *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
}

//  void QQuickPointerHandlerPrivate::onEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickPointerHandlerPrivate16onEnabledChangedEv(
    QQuickPointerHandlerPrivate *self) {
  self->QQuickPointerHandlerPrivate::onEnabledChanged();
}
