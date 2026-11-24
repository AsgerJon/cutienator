//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <cstring>

//  A QQuickAbstractAnimationPrivate that Python can take functions over in. Every QQuickAbstractAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAbstractAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAbstractAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAbstractAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAbstractAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickAbstractAnimationPrivate : public QQuickAbstractAnimationPrivate {
public:
  using QQuickAbstractAnimationPrivate::QQuickAbstractAnimationPrivate;
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
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickAbstractAnimationPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimationPrivate::animationFinished(a0);
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
      CuteQQuickAbstractAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickAbstractAnimationPrivateCall1>(taken[1]);
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
      CuteQQuickAbstractAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickAbstractAnimationPrivateCall2>(taken[2]);
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
      CuteQQuickAbstractAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickAbstractAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickAbstractAnimation *QQuickAbstractAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation *ritual_ZN30QQuickAbstractAnimationPrivate6q_funcEv(
    QQuickAbstractAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickAbstractAnimation *QQuickAbstractAnimationPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickAbstractAnimation *ritual_ZNK30QQuickAbstractAnimationPrivate6q_funcEv(
    const QQuickAbstractAnimationPrivate *self) {
  return self->q_func();
}

//  QQuickAbstractAnimationPrivate::QQuickAbstractAnimationPrivate()
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimationPrivate *ritual_ZN30QQuickAbstractAnimationPrivateC1Ev() {
  return new CuteQQuickAbstractAnimationPrivate();
}

//  void QQuickAbstractAnimationPrivate::commence()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickAbstractAnimationPrivate8commenceEv(
    QQuickAbstractAnimationPrivate *self) {
  self->commence();
}

//  void
//      QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnimationJ
//      ob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickAbstractAnimationPrivate17animationFinishedEP21QAbstractAnimationJob(
    QQuickAbstractAnimationPrivate *self,
    QAbstractAnimationJob *a0) {
  self->animationFinished(a0);
}

//  QQmlProperty QQuickAbstractAnimationPrivate::createProperty(QObject *obj,
//      const QString &str, QObject *infoObj, QString *errorMessage)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN30QQuickAbstractAnimationPrivate14createPropertyEP7QObjectRK7QStringS1_PS2_(
    QObject *obj,
    const QString *str,
    QObject *infoObj,
    QString *errorMessage) {
  return new QQmlProperty(
      QQuickAbstractAnimationPrivate::createProperty(
          obj,
          *str,
          infoObj,
          errorMessage));
}

//  void QQuickAbstractAnimationPrivate::animationGroupDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickAbstractAnimationPrivate19animationGroupDirtyEv(
    QQuickAbstractAnimationPrivate *self) {
  self->animationGroupDirty();
}

//  QQuickAbstractAnimationPrivate as the QAnimationJobChangeListener it is
//      built on
extern "C" Q_DECL_EXPORT
QAnimationJobChangeListener *ritual_cast_QQuickAbstractAnimationPrivate_QAnimationJobChangeListener(
    QQuickAbstractAnimationPrivate *self) {
  return static_cast<QAnimationJobChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickAbstractAnimationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractAnimationPrivate(
    QQuickAbstractAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractAnimationPrivate *>(self)->take(key, call);
}

//  void
//      QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnimationJ
//      ob *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickAbstractAnimationPrivate17animationFinishedEP21QAbstractAnimationJob(
    QQuickAbstractAnimationPrivate *self,
    QAbstractAnimationJob *a0) {
  self->QQuickAbstractAnimationPrivate::animationFinished(a0);
}
