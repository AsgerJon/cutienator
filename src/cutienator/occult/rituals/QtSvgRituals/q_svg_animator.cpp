//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgAnimator that Python can take functions over in. Every QSvgAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAnimatorCall0)(const void *, int *);
typedef qint64 (*CuteQSvgAnimatorCall1)(const void *, int *);
typedef void (*CuteQSvgAnimatorCall2)(const void *, qint64, int *);
class CuteQSvgAnimator : public QSvgAnimator {
public:
  using QSvgAnimator::QSvgAnimator;
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

  //  void QSvgAnimator::restartAnimation()
  void restartAnimation() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAnimatorCall0 call = reinterpret_cast<CuteQSvgAnimatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSvgAnimator::restartAnimation();
  }

  //  qint64 QSvgAnimator::currentElapsed()
  qint64 currentElapsed() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAnimatorCall1 call = reinterpret_cast<CuteQSvgAnimatorCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAnimator::currentElapsed();
  }

  //  void QSvgAnimator::setAnimatorTime(qint64 time)
  void setAnimatorTime(qint64 time) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAnimatorCall2 call = reinterpret_cast<CuteQSvgAnimatorCall2>(taken[2]);
      call(this, time, &handled);
      if (handled) return;
    }
    QSvgAnimator::setAnimatorTime(time);
  }
};

//  QSvgAnimator::QSvgAnimator()
extern "C" Q_DECL_EXPORT
QSvgAnimator *ritual_ZN12QSvgAnimatorC1Ev() {
  return new CuteQSvgAnimator();
}

//  QSvgAnimator::~QSvgAnimator()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgAnimatorD1Ev(QSvgAnimator *self) {
  delete self;
}

//  void QSvgAnimator::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgAnimator16restartAnimationEv(QSvgAnimator *self) {
  self->restartAnimation();
}

//  qint64 QSvgAnimator::currentElapsed()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QSvgAnimator14currentElapsedEv(QSvgAnimator *self) {
  return self->currentElapsed();
}

//  void QSvgAnimator::setAnimatorTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgAnimator15setAnimatorTimeEx(
    QSvgAnimator *self,
    qint64 time) {
  self->setAnimatorTime(time);
}

//  a Python function taken by a CuteQSvgAnimator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAnimator(
    QSvgAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAnimator *>(self)->take(key, call);
}

//  void QSvgAnimator::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSvgAnimator16restartAnimationEv(QSvgAnimator *self) {
  self->QSvgAnimator::restartAnimation();
}

//  qint64 QSvgAnimator::currentElapsed()
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN12QSvgAnimator14currentElapsedEv(QSvgAnimator *self) {
  return self->QSvgAnimator::currentElapsed();
}

//  void QSvgAnimator::setAnimatorTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QSvgAnimator15setAnimatorTimeEx(
    QSvgAnimator *self,
    qint64 time) {
  self->QSvgAnimator::setAnimatorTime(time);
}
