//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgAnimationController that Python can take functions over in. Every QSvgAnimationController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAnimationControllerCall0)(const void *, int *);
typedef qint64 (*CuteQSvgAnimationControllerCall1)(const void *, int *);
typedef void (*CuteQSvgAnimationControllerCall2)(const void *, qint64, int *);
class CuteQSvgAnimationController : public QSvgAnimationController {
public:
  using QSvgAnimationController::QSvgAnimationController;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QSvgAbstractAnimator16restartAnimationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSvgAbstractAnimator14currentElapsedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSvgAbstractAnimator15setAnimatorTimeEx")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QSvgAnimationController::restartAnimation()
  void restartAnimation() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimationControllerCall0 call = reinterpret_cast<CuteQSvgAnimationControllerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSvgAnimationController::restartAnimation();
  }

  //  qint64 QSvgAnimationController::currentElapsed()
  qint64 currentElapsed() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAnimationControllerCall1 call = reinterpret_cast<CuteQSvgAnimationControllerCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAnimationController::currentElapsed();
  }

  //  void QSvgAnimationController::setAnimatorTime(qint64 time)
  void setAnimatorTime(qint64 time) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAnimationControllerCall2 call = reinterpret_cast<CuteQSvgAnimationControllerCall2>(taken[2]);
      call(this, time, &handled);
      if (handled) return;
    }
    QSvgAnimationController::setAnimatorTime(time);
  }
};

//  QSvgAnimationController::QSvgAnimationController()
extern "C" Q_DECL_EXPORT
QSvgAnimationController *ritual_ZN23QSvgAnimationControllerC1Ev() {
  return new CuteQSvgAnimationController();
}

//  QSvgAnimationController::~QSvgAnimationController()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSvgAnimationControllerD1Ev(QSvgAnimationController *self) {
  delete self;
}

//  void QSvgAnimationController::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSvgAnimationController16restartAnimationEv(
    QSvgAnimationController *self) {
  self->restartAnimation();
}

//  qint64 QSvgAnimationController::currentElapsed()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN23QSvgAnimationController14currentElapsedEv(
    QSvgAnimationController *self) {
  return self->currentElapsed();
}

//  void QSvgAnimationController::setAnimatorTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSvgAnimationController15setAnimatorTimeEx(
    QSvgAnimationController *self,
    qint64 time) {
  self->setAnimatorTime(time);
}

//  a Python function taken by a CuteQSvgAnimationController, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimationController(
    QSvgAnimationController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimationController *>(self)->take(key, call);
}

//  void QSvgAnimationController::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSvgAnimationController16restartAnimationEv(
    QSvgAnimationController *self) {
  self->QSvgAnimationController::restartAnimation();
}

//  qint64 QSvgAnimationController::currentElapsed()
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN23QSvgAnimationController14currentElapsedEv(
    QSvgAnimationController *self) {
  return self->QSvgAnimationController::currentElapsed();
}

//  void QSvgAnimationController::setAnimatorTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSvgAnimationController15setAnimatorTimeEx(
    QSvgAnimationController *self,
    qint64 time) {
  self->QSvgAnimationController::setAnimatorTime(time);
}
