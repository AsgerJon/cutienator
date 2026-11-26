//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgAbstractAnimator that Python can take functions over in. Every QSvgAbstractAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgAbstractAnimatorCall0)(const void *, int *);
typedef qint64 (*CuteQSvgAbstractAnimatorCall1)(const void *, int *);
typedef void (*CuteQSvgAbstractAnimatorCall2)(const void *, qint64, int *);
class CuteQSvgAbstractAnimator : public QSvgAbstractAnimator {
public:
  using QSvgAbstractAnimator::QSvgAbstractAnimator;
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

  //  void QSvgAbstractAnimator::restartAnimation()
  void restartAnimation() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAbstractAnimatorCall0 call = reinterpret_cast<CuteQSvgAbstractAnimatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qint64 QSvgAbstractAnimator::currentElapsed()
  qint64 currentElapsed() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAbstractAnimatorCall1 call = reinterpret_cast<CuteQSvgAbstractAnimatorCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSvgAbstractAnimator::setAnimatorTime(qint64 time)
  void setAnimatorTime(qint64 time) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAbstractAnimatorCall2 call = reinterpret_cast<CuteQSvgAbstractAnimatorCall2>(taken[2]);
      call(this, time, &handled);
      if (handled) return;
    }
  }
};

//  QSvgAbstractAnimator::QSvgAbstractAnimator()
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimator *ritual_ZN20QSvgAbstractAnimatorC1Ev() {
  return new CuteQSvgAbstractAnimator();
}

//  QSvgAbstractAnimator::~QSvgAbstractAnimator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimatorD1Ev(QSvgAbstractAnimator *self) {
  delete self;
}

//  void QSvgAbstractAnimator::appendAnimation(const QSvgNode *node,
//      QSvgAbstractAnimation *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimator15appendAnimationEPK8QSvgNodeP21QSvgAbstractAnimation(
    QSvgAbstractAnimator *self,
    const QSvgNode *node,
    QSvgAbstractAnimation *anim) {
  self->appendAnimation(node, anim);
}

//  QList<QSvgAbstractAnimation *>
//      QSvgAbstractAnimator::animationsForNode(const QSvgNode *node) const
extern "C" Q_DECL_EXPORT
QList<QSvgAbstractAnimation *> *ritual_ZNK20QSvgAbstractAnimator17animationsForNodeEPK8QSvgNode(
    const QSvgAbstractAnimator *self,
    const QSvgNode *node) {
  return new QList<QSvgAbstractAnimation *>(self->animationsForNode(node));
}

//  void QSvgAbstractAnimator::advanceAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimator17advanceAnimationsEv(
    QSvgAbstractAnimator *self) {
  self->advanceAnimations();
}

//  void QSvgAbstractAnimator::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimator16restartAnimationEv(
    QSvgAbstractAnimator *self) {
  self->restartAnimation();
}

//  qint64 QSvgAbstractAnimator::currentElapsed()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN20QSvgAbstractAnimator14currentElapsedEv(
    QSvgAbstractAnimator *self) {
  return self->currentElapsed();
}

//  void QSvgAbstractAnimator::setAnimatorTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimator15setAnimatorTimeEx(
    QSvgAbstractAnimator *self,
    qint64 time) {
  self->setAnimatorTime(time);
}

//  void QSvgAbstractAnimator::setAnimationDuration(qint64 dur)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSvgAbstractAnimator20setAnimationDurationEx(
    QSvgAbstractAnimator *self,
    qint64 dur) {
  self->setAnimationDuration(dur);
}

//  qint64 QSvgAbstractAnimator::animationDuration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QSvgAbstractAnimator17animationDurationEv(
    const QSvgAbstractAnimator *self) {
  return self->animationDuration();
}

//  QList<QSvgAbstractAnimation *>
//      QSvgAbstractAnimator::combinedAnimationsForNode(const QSvgNode *node)
//      const
extern "C" Q_DECL_EXPORT
QList<QSvgAbstractAnimation *> *ritual_ZNK20QSvgAbstractAnimator25combinedAnimationsForNodeEPK8QSvgNode(
    const QSvgAbstractAnimator *self,
    const QSvgNode *node) {
  return new QList<QSvgAbstractAnimation *>(
      self->combinedAnimationsForNode(
          node));
}

//  a Python function taken by a CuteQSvgAbstractAnimator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAbstractAnimator(
    QSvgAbstractAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAbstractAnimator *>(self)->take(key, call);
}
