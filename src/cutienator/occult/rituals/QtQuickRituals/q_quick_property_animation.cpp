//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qeasingcurve.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPropertyAnimation that Python can take functions over in. Every QQuickPropertyAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickPropertyAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickPropertyAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickPropertyAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickPropertyAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickPropertyAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickPropertyAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPropertyAnimation : public QQuickPropertyAnimation {
public:
  using QQuickPropertyAnimation::QQuickPropertyAnimation;
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
      CuteQQuickPropertyAnimationCall0 call = reinterpret_cast<CuteQQuickPropertyAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPropertyAnimationCall1 call = reinterpret_cast<CuteQQuickPropertyAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPropertyAnimationCall2 call = reinterpret_cast<CuteQQuickPropertyAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPropertyAnimationCall3 call = reinterpret_cast<CuteQQuickPropertyAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPropertyAnimationCall4 call = reinterpret_cast<CuteQQuickPropertyAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPropertyAnimationCall5 call = reinterpret_cast<CuteQQuickPropertyAnimationCall5>(taken[5]);
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
      CuteQQuickPropertyAnimationCall6 call = reinterpret_cast<CuteQQuickPropertyAnimationCall6>(taken[6]);
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
      CuteQQuickPropertyAnimationCall7 call = reinterpret_cast<CuteQQuickPropertyAnimationCall7>(taken[7]);
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
      CuteQQuickPropertyAnimationCall8 call = reinterpret_cast<CuteQQuickPropertyAnimationCall8>(taken[8]);
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
      CuteQQuickPropertyAnimationCall9 call = reinterpret_cast<CuteQQuickPropertyAnimationCall9>(taken[9]);
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
      CuteQQuickPropertyAnimationCall10 call = reinterpret_cast<CuteQQuickPropertyAnimationCall10>(taken[10]);
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
      CuteQQuickPropertyAnimationCall11 call = reinterpret_cast<CuteQQuickPropertyAnimationCall11>(taken[11]);
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
      CuteQQuickPropertyAnimationCall12 call = reinterpret_cast<CuteQQuickPropertyAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPropertyAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickPropertyAnimation10metaObjectEv(
    const QQuickPropertyAnimation *self) {
  return self->metaObject();
}

//  QString QQuickPropertyAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickPropertyAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPropertyAnimation::tr(s, c, n));
}

//  QQuickPropertyAnimationPrivate *QQuickPropertyAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimationPrivate *ritual_ZN23QQuickPropertyAnimation6d_funcEv(
    QQuickPropertyAnimation *self) {
  return self->d_func();
}

//  const QQuickPropertyAnimationPrivate *QQuickPropertyAnimation::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickPropertyAnimationPrivate *ritual_ZNK23QQuickPropertyAnimation6d_funcEv(
    const QQuickPropertyAnimation *self) {
  return self->d_func();
}

//  QQuickPropertyAnimation::QQuickPropertyAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimation *ritual_ZN23QQuickPropertyAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPropertyAnimation(parent);
}

//  QQuickPropertyAnimation::~QQuickPropertyAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimationD1Ev(QQuickPropertyAnimation *self) {
  delete self;
}

//  int QQuickPropertyAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickPropertyAnimation8durationEv(
    const QQuickPropertyAnimation *self) {
  return self->duration();
}

//  void QQuickPropertyAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation11setDurationEi(
    QQuickPropertyAnimation *self,
    int a0) {
  self->setDuration(a0);
}

//  QVariant QQuickPropertyAnimation::from() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQuickPropertyAnimation4fromEv(
    const QQuickPropertyAnimation *self) {
  return new QVariant(self->from());
}

//  void QQuickPropertyAnimation::setFrom(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation7setFromERK8QVariant(
    QQuickPropertyAnimation *self,
    const QVariant *a0) {
  self->setFrom(*a0);
}

//  QVariant QQuickPropertyAnimation::to() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQuickPropertyAnimation2toEv(
    const QQuickPropertyAnimation *self) {
  return new QVariant(self->to());
}

//  void QQuickPropertyAnimation::setTo(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation5setToERK8QVariant(
    QQuickPropertyAnimation *self,
    const QVariant *a0) {
  self->setTo(*a0);
}

//  QEasingCurve QQuickPropertyAnimation::easing() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK23QQuickPropertyAnimation6easingEv(
    const QQuickPropertyAnimation *self) {
  return new QEasingCurve(self->easing());
}

//  void QQuickPropertyAnimation::setEasing(const QEasingCurve &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation9setEasingERK12QEasingCurve(
    QQuickPropertyAnimation *self,
    const QEasingCurve *a0) {
  self->setEasing(*a0);
}

//  QObject *QQuickPropertyAnimation::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK23QQuickPropertyAnimation6targetEv(
    const QQuickPropertyAnimation *self) {
  return self->target();
}

//  void QQuickPropertyAnimation::setTargetObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation15setTargetObjectEP7QObject(
    QQuickPropertyAnimation *self,
    QObject *a0) {
  self->setTargetObject(a0);
}

//  QString QQuickPropertyAnimation::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickPropertyAnimation8propertyEv(
    const QQuickPropertyAnimation *self) {
  return new QString(self->property());
}

//  void QQuickPropertyAnimation::setProperty(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation11setPropertyERK7QString(
    QQuickPropertyAnimation *self,
    const QString *a0) {
  self->setProperty(*a0);
}

//  QString QQuickPropertyAnimation::properties() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickPropertyAnimation10propertiesEv(
    const QQuickPropertyAnimation *self) {
  return new QString(self->properties());
}

//  void QQuickPropertyAnimation::setProperties(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickPropertyAnimation13setPropertiesERK7QString(
    QQuickPropertyAnimation *self,
    const QString *a0) {
  self->setProperties(*a0);
}

//  a Python function taken by a CuteQQuickPropertyAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPropertyAnimation(
    QQuickPropertyAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPropertyAnimation *>(self)->take(key, call);
}

//  int QQuickPropertyAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QQuickPropertyAnimation8durationEv(
    const QQuickPropertyAnimation *self) {
  return self->QQuickPropertyAnimation::duration();
}

//  void QQuickPropertyAnimation::setDuration(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickPropertyAnimation11setDurationEi(
    QQuickPropertyAnimation *self,
    int a0) {
  self->QQuickPropertyAnimation::setDuration(a0);
}
