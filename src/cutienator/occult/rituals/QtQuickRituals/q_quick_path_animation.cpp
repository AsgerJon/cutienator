//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qpoint.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPathAnimation that Python can take functions over in. Every QQuickPathAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPathAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickPathAnimationCall1)(const void *, int *);
typedef int (*CuteQQuickPathAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickPathAnimationCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPathAnimation : public QQuickPathAnimation {
public:
  using QQuickPathAnimation::QQuickPathAnimation;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPathAnimationCall0 call = reinterpret_cast<CuteQQuickPathAnimationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPathAnimationCall1 call = reinterpret_cast<CuteQQuickPathAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPathAnimationCall2 call = reinterpret_cast<CuteQQuickPathAnimationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPathAnimationCall3 call = reinterpret_cast<CuteQQuickPathAnimationCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPathAnimationCall4 call = reinterpret_cast<CuteQQuickPathAnimationCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPathAnimationCall5 call = reinterpret_cast<CuteQQuickPathAnimationCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPathAnimationCall6 call = reinterpret_cast<CuteQQuickPathAnimationCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPathAnimationCall7 call = reinterpret_cast<CuteQQuickPathAnimationCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPathAnimationCall8 call = reinterpret_cast<CuteQQuickPathAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPathAnimationCall9 call = reinterpret_cast<CuteQQuickPathAnimationCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPathAnimationCall10 call = reinterpret_cast<CuteQQuickPathAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPathAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPathAnimation10metaObjectEv(
    const QQuickPathAnimation *self) {
  return self->metaObject();
}

//  QString QQuickPathAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickPathAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathAnimation::tr(s, c, n));
}

//  QQuickPathAnimationPrivate *QQuickPathAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPathAnimationPrivate *ritual_ZN19QQuickPathAnimation6d_funcEv(
    QQuickPathAnimation *self) {
  return self->d_func();
}

//  const QQuickPathAnimationPrivate *QQuickPathAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPathAnimationPrivate *ritual_ZNK19QQuickPathAnimation6d_funcEv(
    const QQuickPathAnimation *self) {
  return self->d_func();
}

//  QQuickPathAnimation::QQuickPathAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathAnimation *ritual_ZN19QQuickPathAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPathAnimation(parent);
}

//  QQuickPathAnimation::~QQuickPathAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimationD1Ev(QQuickPathAnimation *self) {
  delete self;
}

//  int QQuickPathAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickPathAnimation8durationEv(
    const QQuickPathAnimation *self) {
  return self->duration();
}

//  void QQuickPathAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation11setDurationEi(
    QQuickPathAnimation *self,
    int a0) {
  self->setDuration(a0);
}

//  QEasingCurve QQuickPathAnimation::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK19QQuickPathAnimation6easingEv(
    const QQuickPathAnimation *self) {
  return new QEasingCurve(self->easing());
}

//  void QQuickPathAnimation::setEasing(const QEasingCurve &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation9setEasingERK12QEasingCurve(
    QQuickPathAnimation *self,
    const QEasingCurve *a0) {
  self->setEasing(*a0);
}

//  QQuickPath *QQuickPathAnimation::path() const
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZNK19QQuickPathAnimation4pathEv(
    const QQuickPathAnimation *self) {
  return self->path();
}

//  void QQuickPathAnimation::setPath(QQuickPath *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation7setPathEP10QQuickPath(
    QQuickPathAnimation *self,
    QQuickPath *a0) {
  self->setPath(a0);
}

//  QQuickItem *QQuickPathAnimation::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK19QQuickPathAnimation6targetEv(
    const QQuickPathAnimation *self) {
  return self->target();
}

//  void QQuickPathAnimation::setTargetObject(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation15setTargetObjectEP10QQuickItem(
    QQuickPathAnimation *self,
    QQuickItem *a0) {
  self->setTargetObject(a0);
}

//  Orientation QQuickPathAnimation::orientation() const
extern "C" Q_DECL_EXPORT
QQuickPathAnimation::Orientation ritual_ZNK19QQuickPathAnimation11orientationEv(
    const QQuickPathAnimation *self) {
  return self->orientation();
}

//  void QQuickPathAnimation::setOrientation(Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation14setOrientationENS_11OrientationE(
    QQuickPathAnimation *self,
    QQuickPathAnimation::Orientation orientation) {
  self->setOrientation(orientation);
}

//  QPointF QQuickPathAnimation::anchorPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QQuickPathAnimation11anchorPointEv(
    const QQuickPathAnimation *self) {
  return new QPointF(self->anchorPoint());
}

//  void QQuickPathAnimation::setAnchorPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation14setAnchorPointERK7QPointF(
    QQuickPathAnimation *self,
    const QPointF *point) {
  self->setAnchorPoint(*point);
}

//  int QQuickPathAnimation::orientationEntryDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickPathAnimation24orientationEntryDurationEv(
    const QQuickPathAnimation *self) {
  return self->orientationEntryDuration();
}

//  void QQuickPathAnimation::setOrientationEntryDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation27setOrientationEntryDurationEi(
    QQuickPathAnimation *self,
    int a0) {
  self->setOrientationEntryDuration(a0);
}

//  int QQuickPathAnimation::orientationExitDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickPathAnimation23orientationExitDurationEv(
    const QQuickPathAnimation *self) {
  return self->orientationExitDuration();
}

//  void QQuickPathAnimation::setOrientationExitDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation26setOrientationExitDurationEi(
    QQuickPathAnimation *self,
    int a0) {
  self->setOrientationExitDuration(a0);
}

//  qreal QQuickPathAnimation::endRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickPathAnimation11endRotationEv(
    const QQuickPathAnimation *self) {
  return self->endRotation();
}

//  void QQuickPathAnimation::setEndRotation(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAnimation14setEndRotationEd(
    QQuickPathAnimation *self,
    qreal a0) {
  self->setEndRotation(a0);
}

//  a Python function taken by a CuteQQuickPathAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathAnimation(
    QQuickPathAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathAnimation *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_path)
