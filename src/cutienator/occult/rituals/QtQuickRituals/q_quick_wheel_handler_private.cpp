//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(wheelevent)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(wheelevent)
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickWheelHandlerPrivate that Python can take functions over in. Every QQuickWheelHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWheelHandlerPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickWheelHandlerPrivateCall1)(const void *, int *);
class CuteQQuickWheelHandlerPrivate : public QQuickWheelHandlerPrivate {
public:
  using QQuickWheelHandlerPrivate::QQuickWheelHandlerPrivate;
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
      CuteQQuickWheelHandlerPrivateCall0 call = reinterpret_cast<CuteQQuickWheelHandlerPrivateCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onParentChanged(a0, a1);
  }

  //  void QQuickPointerHandlerPrivate::onEnabledChanged()
  void onEnabledChanged() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWheelHandlerPrivateCall1 call = reinterpret_cast<CuteQQuickWheelHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandlerPrivate::onEnabledChanged();
  }
};

//  QQuickWheelHandler *QQuickWheelHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickWheelHandler *ritual_ZN25QQuickWheelHandlerPrivate6q_funcEv(
    QQuickWheelHandlerPrivate *self) {
  return self->q_func();
}

//  const QQuickWheelHandler *QQuickWheelHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickWheelHandler *ritual_ZNK25QQuickWheelHandlerPrivate6q_funcEv(
    const QQuickWheelHandlerPrivate *self) {
  return self->q_func();
}

//  QQuickWheelHandlerPrivate
//      *QQuickWheelHandlerPrivate::get(QQuickWheelHandler *q)
extern "C" Q_DECL_EXPORT
QQuickWheelHandlerPrivate *ritual_ZN25QQuickWheelHandlerPrivate3getEP18QQuickWheelHandler(
    QQuickWheelHandler *q) {
  return QQuickWheelHandlerPrivate::get(q);
}

//  const QQuickWheelHandlerPrivate *QQuickWheelHandlerPrivate::get(const
//      QQuickWheelHandler *q)
extern "C" Q_DECL_EXPORT
const QQuickWheelHandlerPrivate *ritual_ZN25QQuickWheelHandlerPrivate3getEPK18QQuickWheelHandler(
    const QQuickWheelHandler *q) {
  return QQuickWheelHandlerPrivate::get(q);
}

//  QQuickWheelHandlerPrivate::QQuickWheelHandlerPrivate()
extern "C" Q_DECL_EXPORT
QQuickWheelHandlerPrivate *ritual_ZN25QQuickWheelHandlerPrivateC1Ev() {
  return new CuteQQuickWheelHandlerPrivate();
}

//  QMetaProperty &QQuickWheelHandlerPrivate::targetMetaProperty() const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK25QQuickWheelHandlerPrivate18targetMetaPropertyEv(
    const QQuickWheelHandlerPrivate *self) {
  return &(self->targetMetaProperty());
}

//  a Python function taken by a CuteQQuickWheelHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWheelHandlerPrivate(
    QQuickWheelHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWheelHandlerPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wheelevent)
