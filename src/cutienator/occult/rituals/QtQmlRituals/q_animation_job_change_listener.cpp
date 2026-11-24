//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QAnimationJobChangeListener that Python can take functions over in. Every QAnimationJobChangeListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationJobChangeListenerCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationJobChangeListenerCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationJobChangeListenerCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationJobChangeListenerCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQAnimationJobChangeListener : public QAnimationJobChangeListener {
public:
  using QAnimationJobChangeListener::QAnimationJobChangeListener;
  CuteQAnimationJobChangeListener(const QAnimationJobChangeListener &other) : QAnimationJobChangeListener(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void
  //      QAnimationJobChangeListener::animationFinished(QAbstractAnimation
  //      Job *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationJobChangeListenerCall0 call = reinterpret_cast<CuteQAnimationJobChangeListenerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationFinished(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationStateChanged(QAbstractAnim
  //      ationJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationJobChangeListenerCall1 call = reinterpret_cast<CuteQAnimationJobChangeListenerCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationJobChangeListenerCall2 call = reinterpret_cast<CuteQAnimationJobChangeListenerCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAnimationJobChangeListenerCall3 call = reinterpret_cast<CuteQAnimationJobChangeListenerCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QAnimationJobChangeListener::~QAnimationJobChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAnimationJobChangeListenerD1Ev(
    QAnimationJobChangeListener *self) {
  delete self;
}

//  void QAnimationJobChangeListener::animationFinished(QAbstractAnimationJob
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0) {
  self->animationFinished(a0);
}

//  void
//      QAnimationJobChangeListener::animationStateChanged(QAbstractAnimation
//      Job *a0, QAbstractAnimationJob::State a1,
//      QAbstractAnimationJob::State a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0,
    QAbstractAnimationJob::State a1,
    QAbstractAnimationJob::State a2) {
  self->animationStateChanged(a0, a1, a2);
}

//  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstractAn
//      imationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0) {
  self->animationCurrentLoopChanged(a0);
}

//  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstractAn
//      imationJob *a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0,
    int a1) {
  self->animationCurrentTimeChanged(a0, a1);
}

//  a Python function taken by a CuteQAnimationJobChangeListener, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationJobChangeListener(
    QAnimationJobChangeListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationJobChangeListener *>(self)->take(key, call);
}

//  void QAnimationJobChangeListener::animationFinished(QAbstractAnimationJob
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0) {
  self->QAnimationJobChangeListener::animationFinished(a0);
}

//  void
//      QAnimationJobChangeListener::animationStateChanged(QAbstractAnimation
//      Job *a0, QAbstractAnimationJob::State a1,
//      QAbstractAnimationJob::State a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0,
    QAbstractAnimationJob::State a1,
    QAbstractAnimationJob::State a2) {
  self->QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
}

//  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstractAn
//      imationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0) {
  self->QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
}

//  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstractAn
//      imationJob *a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi(
    QAnimationJobChangeListener *self,
    QAbstractAnimationJob *a0,
    int a1) {
  self->QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
}

#endif  // QT_CONFIG(qml_animation)
