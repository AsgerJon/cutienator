//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPauseAnimation that Python can take functions over in. Every QQuickPauseAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPauseAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickPauseAnimationCall1)(const void *, int *);
typedef int (*CuteQQuickPauseAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickPauseAnimationCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPauseAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPauseAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPauseAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPauseAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPauseAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPauseAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPauseAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPauseAnimation : public QQuickPauseAnimation {
public:
  using QQuickPauseAnimation::QQuickPauseAnimation;
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
      CuteQQuickPauseAnimationCall0 call = reinterpret_cast<CuteQQuickPauseAnimationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPauseAnimationCall1 call = reinterpret_cast<CuteQQuickPauseAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPauseAnimationCall2 call = reinterpret_cast<CuteQQuickPauseAnimationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPauseAnimationCall3 call = reinterpret_cast<CuteQQuickPauseAnimationCall3>(taken[3]);
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
      CuteQQuickPauseAnimationCall4 call = reinterpret_cast<CuteQQuickPauseAnimationCall4>(taken[4]);
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
      CuteQQuickPauseAnimationCall5 call = reinterpret_cast<CuteQQuickPauseAnimationCall5>(taken[5]);
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
      CuteQQuickPauseAnimationCall6 call = reinterpret_cast<CuteQQuickPauseAnimationCall6>(taken[6]);
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
      CuteQQuickPauseAnimationCall7 call = reinterpret_cast<CuteQQuickPauseAnimationCall7>(taken[7]);
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
      CuteQQuickPauseAnimationCall8 call = reinterpret_cast<CuteQQuickPauseAnimationCall8>(taken[8]);
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
      CuteQQuickPauseAnimationCall9 call = reinterpret_cast<CuteQQuickPauseAnimationCall9>(taken[9]);
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
      CuteQQuickPauseAnimationCall10 call = reinterpret_cast<CuteQQuickPauseAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPauseAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickPauseAnimation10metaObjectEv(
    const QQuickPauseAnimation *self) {
  return self->metaObject();
}

//  QString QQuickPauseAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickPauseAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPauseAnimation::tr(s, c, n));
}

//  QQuickPauseAnimationPrivate *QQuickPauseAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPauseAnimationPrivate *ritual_ZN20QQuickPauseAnimation6d_funcEv(
    QQuickPauseAnimation *self) {
  return self->d_func();
}

//  const QQuickPauseAnimationPrivate *QQuickPauseAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPauseAnimationPrivate *ritual_ZNK20QQuickPauseAnimation6d_funcEv(
    const QQuickPauseAnimation *self) {
  return self->d_func();
}

//  QQuickPauseAnimation::QQuickPauseAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPauseAnimation *ritual_ZN20QQuickPauseAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPauseAnimation(parent);
}

//  QQuickPauseAnimation::~QQuickPauseAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPauseAnimationD1Ev(QQuickPauseAnimation *self) {
  delete self;
}

//  int QQuickPauseAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickPauseAnimation8durationEv(
    const QQuickPauseAnimation *self) {
  return self->duration();
}

//  void QQuickPauseAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPauseAnimation11setDurationEi(
    QQuickPauseAnimation *self,
    int a0) {
  self->setDuration(a0);
}

//  a Python function taken by a CuteQQuickPauseAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPauseAnimation(
    QQuickPauseAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPauseAnimation *>(self)->take(key, call);
}
