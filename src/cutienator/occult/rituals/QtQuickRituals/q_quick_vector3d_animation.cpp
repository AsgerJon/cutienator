//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickVector3dAnimation that Python can take functions over in. Every QQuickVector3dAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickVector3dAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickVector3dAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickVector3dAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickVector3dAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickVector3dAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickVector3dAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVector3dAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVector3dAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVector3dAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVector3dAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVector3dAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVector3dAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVector3dAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickVector3dAnimation : public QQuickVector3dAnimation {
public:
  using QQuickVector3dAnimation::QQuickVector3dAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQuickPropertyAnimation11setDurationEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQuickAbstractAnimation14threadingModelEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QQuickPropertyAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall0 call = reinterpret_cast<CuteQQuickVector3dAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall1 call = reinterpret_cast<CuteQQuickVector3dAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall2 call = reinterpret_cast<CuteQQuickVector3dAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall3 call = reinterpret_cast<CuteQQuickVector3dAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall4 call = reinterpret_cast<CuteQQuickVector3dAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall5 call = reinterpret_cast<CuteQQuickVector3dAnimationCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::setTarget(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall6 call = reinterpret_cast<CuteQQuickVector3dAnimationCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall7 call = reinterpret_cast<CuteQQuickVector3dAnimationCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall8 call = reinterpret_cast<CuteQQuickVector3dAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall9 call = reinterpret_cast<CuteQQuickVector3dAnimationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall10 call = reinterpret_cast<CuteQQuickVector3dAnimationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall11 call = reinterpret_cast<CuteQQuickVector3dAnimationCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickVector3dAnimationCall12 call = reinterpret_cast<CuteQQuickVector3dAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickVector3dAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickVector3dAnimation10metaObjectEv(
    const QQuickVector3dAnimation *self) {
  return self->metaObject();
}

//  QString QQuickVector3dAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickVector3dAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickVector3dAnimation::tr(s, c, n));
}

//  QQuickPropertyAnimationPrivate *QQuickVector3dAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimationPrivate *ritual_ZN23QQuickVector3dAnimation6d_funcEv(
    QQuickVector3dAnimation *self) {
  return self->d_func();
}

//  const QQuickPropertyAnimationPrivate *QQuickVector3dAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickPropertyAnimationPrivate *ritual_ZNK23QQuickVector3dAnimation6d_funcEv(
    const QQuickVector3dAnimation *self) {
  return self->d_func();
}

//  QQuickVector3dAnimation::QQuickVector3dAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickVector3dAnimation *ritual_ZN23QQuickVector3dAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickVector3dAnimation(parent);
}

//  QQuickVector3dAnimation::~QQuickVector3dAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3dAnimationD1Ev(QQuickVector3dAnimation *self) {
  delete self;
}

//  QVector3D QQuickVector3dAnimation::from() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3dAnimation4fromEv(
    const QQuickVector3dAnimation *self) {
  return new QVector3D(self->from());
}

//  void QQuickVector3dAnimation::setFrom(QVector3D a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3dAnimation7setFromE9QVector3D(
    QQuickVector3dAnimation *self,
    const QVector3D *a0) {
  self->setFrom(*a0);
}

//  QVector3D QQuickVector3dAnimation::to() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3dAnimation2toEv(
    const QQuickVector3dAnimation *self) {
  return new QVector3D(self->to());
}

//  void QQuickVector3dAnimation::setTo(QVector3D a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3dAnimation5setToE9QVector3D(
    QQuickVector3dAnimation *self,
    const QVector3D *a0) {
  self->setTo(*a0);
}

//  a Python function taken by a CuteQQuickVector3dAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickVector3dAnimation(
    QQuickVector3dAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickVector3dAnimation *>(self)->take(key, call);
}
