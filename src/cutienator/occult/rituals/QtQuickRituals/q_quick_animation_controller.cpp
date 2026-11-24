//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimationcontroller_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimationcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickAnimationController that Python can take functions over in. Every QQuickAnimationController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnimationControllerCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimationControllerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimationControllerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimationControllerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimationControllerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimationControllerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimationControllerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimationControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnimationController : public QQuickAnimationController {
public:
  using QQuickAnimationController::QQuickAnimationController;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQmlFinalizerHook18componentFinalizedEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAnimationController::componentFinalized()
  void componentFinalized() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall0 call = reinterpret_cast<CuteQQuickAnimationControllerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimationController::componentFinalized();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall1 call = reinterpret_cast<CuteQQuickAnimationControllerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall2 call = reinterpret_cast<CuteQQuickAnimationControllerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall3 call = reinterpret_cast<CuteQQuickAnimationControllerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall4 call = reinterpret_cast<CuteQQuickAnimationControllerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall5 call = reinterpret_cast<CuteQQuickAnimationControllerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall6 call = reinterpret_cast<CuteQQuickAnimationControllerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimationControllerCall7 call = reinterpret_cast<CuteQQuickAnimationControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnimationController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickAnimationController10metaObjectEv(
    const QQuickAnimationController *self) {
  return self->metaObject();
}

//  QString QQuickAnimationController::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickAnimationController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimationController::tr(s, c, n));
}

//  QQuickAnimationController::QQuickAnimationController(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAnimationController *ritual_ZN25QQuickAnimationControllerC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickAnimationController(parent);
}

//  QQuickAnimationController::~QQuickAnimationController()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationControllerD1Ev(
    QQuickAnimationController *self) {
  delete self;
}

//  qreal QQuickAnimationController::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickAnimationController8progressEv(
    const QQuickAnimationController *self) {
  return self->progress();
}

//  void QQuickAnimationController::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController11setProgressEd(
    QQuickAnimationController *self,
    qreal progress) {
  self->setProgress(progress);
}

//  QQuickAbstractAnimation *QQuickAnimationController::animation() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation *ritual_ZNK25QQuickAnimationController9animationEv(
    const QQuickAnimationController *self) {
  return self->animation();
}

//  void QQuickAnimationController::setAnimation(QQuickAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController12setAnimationEP23QQuickAbstractAnimation(
    QQuickAnimationController *self,
    QQuickAbstractAnimation *animation) {
  self->setAnimation(animation);
}

//  void QQuickAnimationController::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController18componentFinalizedEv(
    QQuickAnimationController *self) {
  self->componentFinalized();
}

//  void QQuickAnimationController::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController6reloadEv(
    QQuickAnimationController *self) {
  self->reload();
}

//  void QQuickAnimationController::completeToBeginning()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController19completeToBeginningEv(
    QQuickAnimationController *self) {
  self->completeToBeginning();
}

//  void QQuickAnimationController::completeToEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController13completeToEndEv(
    QQuickAnimationController *self) {
  self->completeToEnd();
}

//  void QQuickAnimationController::updateProgress()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickAnimationController14updateProgressEv(
    QQuickAnimationController *self) {
  self->updateProgress();
}

//  QQuickAnimationController as the QQmlFinalizerHook it is built on
extern "C" Q_DECL_EXPORT
QQmlFinalizerHook *ritual_cast_QQuickAnimationController_QQmlFinalizerHook(
    QQuickAnimationController *self) {
  return static_cast<QQmlFinalizerHook *>(self);
}

//  a Python function taken by a CuteQQuickAnimationController, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimationController(
    QQuickAnimationController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimationController *>(self)->take(key, call);
}

//  void QQuickAnimationController::componentFinalized()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickAnimationController18componentFinalizedEv(
    QQuickAnimationController *self) {
  self->QQuickAnimationController::componentFinalized();
}
