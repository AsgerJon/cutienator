//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickColorAnimation that Python can take functions over in. Every QQuickColorAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickColorAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickColorAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickColorAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickColorAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickColorAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickColorAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickColorAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickColorAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickColorAnimation : public QQuickColorAnimation {
public:
  using QQuickColorAnimation::QQuickColorAnimation;
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
      CuteQQuickColorAnimationCall0 call = reinterpret_cast<CuteQQuickColorAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickColorAnimationCall1 call = reinterpret_cast<CuteQQuickColorAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickColorAnimationCall2 call = reinterpret_cast<CuteQQuickColorAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickColorAnimationCall3 call = reinterpret_cast<CuteQQuickColorAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickColorAnimationCall4 call = reinterpret_cast<CuteQQuickColorAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickColorAnimationCall5 call = reinterpret_cast<CuteQQuickColorAnimationCall5>(taken[5]);
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
      CuteQQuickColorAnimationCall6 call = reinterpret_cast<CuteQQuickColorAnimationCall6>(taken[6]);
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
      CuteQQuickColorAnimationCall7 call = reinterpret_cast<CuteQQuickColorAnimationCall7>(taken[7]);
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
      CuteQQuickColorAnimationCall8 call = reinterpret_cast<CuteQQuickColorAnimationCall8>(taken[8]);
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
      CuteQQuickColorAnimationCall9 call = reinterpret_cast<CuteQQuickColorAnimationCall9>(taken[9]);
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
      CuteQQuickColorAnimationCall10 call = reinterpret_cast<CuteQQuickColorAnimationCall10>(taken[10]);
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
      CuteQQuickColorAnimationCall11 call = reinterpret_cast<CuteQQuickColorAnimationCall11>(taken[11]);
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
      CuteQQuickColorAnimationCall12 call = reinterpret_cast<CuteQQuickColorAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickColorAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickColorAnimation10metaObjectEv(
    const QQuickColorAnimation *self) {
  return self->metaObject();
}

//  QString QQuickColorAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickColorAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorAnimation::tr(s, c, n));
}

//  QQuickPropertyAnimationPrivate *QQuickColorAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimationPrivate *ritual_ZN20QQuickColorAnimation6d_funcEv(
    QQuickColorAnimation *self) {
  return self->d_func();
}

//  const QQuickPropertyAnimationPrivate *QQuickColorAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickPropertyAnimationPrivate *ritual_ZNK20QQuickColorAnimation6d_funcEv(
    const QQuickColorAnimation *self) {
  return self->d_func();
}

//  QQuickColorAnimation::QQuickColorAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickColorAnimation *ritual_ZN20QQuickColorAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickColorAnimation(parent);
}

//  QQuickColorAnimation::~QQuickColorAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorAnimationD1Ev(QQuickColorAnimation *self) {
  delete self;
}

//  QColor QQuickColorAnimation::from() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorAnimation4fromEv(
    const QQuickColorAnimation *self) {
  return new QColor(self->from());
}

//  void QQuickColorAnimation::setFrom(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorAnimation7setFromERK6QColor(
    QQuickColorAnimation *self,
    const QColor *a0) {
  self->setFrom(*a0);
}

//  QColor QQuickColorAnimation::to() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickColorAnimation2toEv(
    const QQuickColorAnimation *self) {
  return new QColor(self->to());
}

//  void QQuickColorAnimation::setTo(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickColorAnimation5setToERK6QColor(
    QQuickColorAnimation *self,
    const QColor *a0) {
  self->setTo(*a0);
}

//  a Python function taken by a CuteQQuickColorAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickColorAnimation(
    QQuickColorAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickColorAnimation *>(self)->take(key, call);
}
