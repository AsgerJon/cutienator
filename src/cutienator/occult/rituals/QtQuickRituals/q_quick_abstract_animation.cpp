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

//  A QQuickAbstractAnimation that Python can take functions over in. Every QQuickAbstractAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAbstractAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickAbstractAnimationCall1)(const void *, int *);
typedef int (*CuteQQuickAbstractAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickAbstractAnimationCall3)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAbstractAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAbstractAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAbstractAnimation : public QQuickAbstractAnimation {
public:
  using QQuickAbstractAnimation::QQuickAbstractAnimation;
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
      CuteQQuickAbstractAnimationCall0 call = reinterpret_cast<CuteQQuickAbstractAnimationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractAnimationCall1 call = reinterpret_cast<CuteQQuickAbstractAnimationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractAnimationCall2 call = reinterpret_cast<CuteQQuickAbstractAnimationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractAnimationCall3 call = reinterpret_cast<CuteQQuickAbstractAnimationCall3>(taken[3]);
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
      CuteQQuickAbstractAnimationCall4 call = reinterpret_cast<CuteQQuickAbstractAnimationCall4>(taken[4]);
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
      CuteQQuickAbstractAnimationCall5 call = reinterpret_cast<CuteQQuickAbstractAnimationCall5>(taken[5]);
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
      CuteQQuickAbstractAnimationCall6 call = reinterpret_cast<CuteQQuickAbstractAnimationCall6>(taken[6]);
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
      CuteQQuickAbstractAnimationCall7 call = reinterpret_cast<CuteQQuickAbstractAnimationCall7>(taken[7]);
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
      CuteQQuickAbstractAnimationCall8 call = reinterpret_cast<CuteQQuickAbstractAnimationCall8>(taken[8]);
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
      CuteQQuickAbstractAnimationCall9 call = reinterpret_cast<CuteQQuickAbstractAnimationCall9>(taken[9]);
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
      CuteQQuickAbstractAnimationCall10 call = reinterpret_cast<CuteQQuickAbstractAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAbstractAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickAbstractAnimation10metaObjectEv(
    const QQuickAbstractAnimation *self) {
  return self->metaObject();
}

//  QString QQuickAbstractAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickAbstractAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAbstractAnimation::tr(s, c, n));
}

//  QQuickAbstractAnimationPrivate *QQuickAbstractAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimationPrivate *ritual_ZN23QQuickAbstractAnimation6d_funcEv(
    QQuickAbstractAnimation *self) {
  return self->d_func();
}

//  const QQuickAbstractAnimationPrivate *QQuickAbstractAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickAbstractAnimationPrivate *ritual_ZNK23QQuickAbstractAnimation6d_funcEv(
    const QQuickAbstractAnimation *self) {
  return self->d_func();
}

//  void QQuickAbstractAnimation::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation24qt_qmlMarker_uncreatableEv(
    QQuickAbstractAnimation *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickAbstractAnimation::QQuickAbstractAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation *ritual_ZN23QQuickAbstractAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickAbstractAnimation(parent);
}

//  QQuickAbstractAnimation::~QQuickAbstractAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimationD1Ev(QQuickAbstractAnimation *self) {
  delete self;
}

//  bool QQuickAbstractAnimation::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickAbstractAnimation9isRunningEv(
    const QQuickAbstractAnimation *self) {
  return self->isRunning();
}

//  void QQuickAbstractAnimation::setRunning(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation10setRunningEb(
    QQuickAbstractAnimation *self,
    bool a0) {
  self->setRunning(a0);
}

//  bool QQuickAbstractAnimation::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickAbstractAnimation8isPausedEv(
    const QQuickAbstractAnimation *self) {
  return self->isPaused();
}

//  void QQuickAbstractAnimation::setPaused(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation9setPausedEb(
    QQuickAbstractAnimation *self,
    bool a0) {
  self->setPaused(a0);
}

//  bool QQuickAbstractAnimation::alwaysRunToEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickAbstractAnimation14alwaysRunToEndEv(
    const QQuickAbstractAnimation *self) {
  return self->alwaysRunToEnd();
}

//  void QQuickAbstractAnimation::setAlwaysRunToEnd(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation17setAlwaysRunToEndEb(
    QQuickAbstractAnimation *self,
    bool a0) {
  self->setAlwaysRunToEnd(a0);
}

//  int QQuickAbstractAnimation::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickAbstractAnimation5loopsEv(
    const QQuickAbstractAnimation *self) {
  return self->loops();
}

//  void QQuickAbstractAnimation::setLoops(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation8setLoopsEi(
    QQuickAbstractAnimation *self,
    int a0) {
  self->setLoops(a0);
}

//  int QQuickAbstractAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickAbstractAnimation8durationEv(
    const QQuickAbstractAnimation *self) {
  return self->duration();
}

//  int QQuickAbstractAnimation::currentTime()
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickAbstractAnimation11currentTimeEv(
    QQuickAbstractAnimation *self) {
  return self->currentTime();
}

//  void QQuickAbstractAnimation::setCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation14setCurrentTimeEi(
    QQuickAbstractAnimation *self,
    int a0) {
  self->setCurrentTime(a0);
}

//  QQuickAnimationGroup *QQuickAbstractAnimation::group() const
extern "C" Q_DECL_EXPORT
QQuickAnimationGroup *ritual_ZNK23QQuickAbstractAnimation5groupEv(
    const QQuickAbstractAnimation *self) {
  return self->group();
}

//  void QQuickAbstractAnimation::setGroup(QQuickAnimationGroup *a0, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation8setGroupEP20QQuickAnimationGroupi(
    QQuickAbstractAnimation *self,
    QQuickAnimationGroup *a0,
    int index) {
  self->setGroup(a0, index);
}

//  void QQuickAbstractAnimation::setDefaultTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation16setDefaultTargetERK12QQmlProperty(
    QQuickAbstractAnimation *self,
    const QQmlProperty *a0) {
  self->setDefaultTarget(*a0);
}

//  void QQuickAbstractAnimation::setDisableUserControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation21setDisableUserControlEv(
    QQuickAbstractAnimation *self) {
  self->setDisableUserControl();
}

//  void QQuickAbstractAnimation::setEnableUserControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation20setEnableUserControlEv(
    QQuickAbstractAnimation *self) {
  self->setEnableUserControl();
}

//  bool QQuickAbstractAnimation::userControlDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickAbstractAnimation19userControlDisabledEv(
    const QQuickAbstractAnimation *self) {
  return self->userControlDisabled();
}

//  void QQuickAbstractAnimation::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation10classBeginEv(
    QQuickAbstractAnimation *self) {
  self->classBegin();
}

//  void QQuickAbstractAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation17componentCompleteEv(
    QQuickAbstractAnimation *self) {
  self->componentComplete();
}

//  ThreadingModel QQuickAbstractAnimation::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_ZNK23QQuickAbstractAnimation14threadingModelEv(
    const QQuickAbstractAnimation *self) {
  return self->threadingModel();
}

//  void QQuickAbstractAnimation::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation7restartEv(
    QQuickAbstractAnimation *self) {
  self->restart();
}

//  void QQuickAbstractAnimation::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation5startEv(
    QQuickAbstractAnimation *self) {
  self->start();
}

//  void QQuickAbstractAnimation::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation5pauseEv(
    QQuickAbstractAnimation *self) {
  self->pause();
}

//  void QQuickAbstractAnimation::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation6resumeEv(
    QQuickAbstractAnimation *self) {
  self->resume();
}

//  void QQuickAbstractAnimation::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation4stopEv(
    QQuickAbstractAnimation *self) {
  self->stop();
}

//  void QQuickAbstractAnimation::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation8completeEv(
    QQuickAbstractAnimation *self) {
  self->complete();
}

//  QAbstractAnimationJob
//      *QQuickAbstractAnimation::initInstance(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN23QQuickAbstractAnimation12initInstanceEP21QAbstractAnimationJob(
    QQuickAbstractAnimation *self,
    QAbstractAnimationJob *animation) {
  return self->initInstance(animation);
}

//  QAbstractAnimationJob *QQuickAbstractAnimation::qtAnimation()
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN23QQuickAbstractAnimation11qtAnimationEv(
    QQuickAbstractAnimation *self) {
  return self->qtAnimation();
}

//  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation9setTargetERK12QQmlProperty(
    QQuickAbstractAnimation *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  void QQuickAbstractAnimation::notifyRunningChanged(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAbstractAnimation20notifyRunningChangedEb(
    QQuickAbstractAnimation *self,
    bool running) {
  self->notifyRunningChanged(running);
}

//  QQuickAbstractAnimation as the QQmlPropertyValueSource it is built on
extern "C" Q_DECL_EXPORT
QQmlPropertyValueSource *ritual_cast_QQuickAbstractAnimation_QQmlPropertyValueSource(
    QQuickAbstractAnimation *self) {
  return static_cast<QQmlPropertyValueSource *>(self);
}

//  QQuickAbstractAnimation as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickAbstractAnimation_QQmlParserStatus(
    QQuickAbstractAnimation *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickAbstractAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractAnimation(
    QQuickAbstractAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractAnimation *>(self)->take(key, call);
}

//  void QQuickAbstractAnimation::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickAbstractAnimation10classBeginEv(
    QQuickAbstractAnimation *self) {
  self->QQuickAbstractAnimation::classBegin();
}

//  void QQuickAbstractAnimation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickAbstractAnimation17componentCompleteEv(
    QQuickAbstractAnimation *self) {
  self->QQuickAbstractAnimation::componentComplete();
}

//  ThreadingModel QQuickAbstractAnimation::threadingModel() const
extern "C" Q_DECL_EXPORT
QQuickAbstractAnimation::ThreadingModel ritual_own_ZNK23QQuickAbstractAnimation14threadingModelEv(
    const QQuickAbstractAnimation *self) {
  return self->QQuickAbstractAnimation::threadingModel();
}

//  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickAbstractAnimation9setTargetERK12QQmlProperty(
    QQuickAbstractAnimation *self,
    const QQmlProperty *a0) {
  self->QQuickAbstractAnimation::setTarget(*a0);
}
