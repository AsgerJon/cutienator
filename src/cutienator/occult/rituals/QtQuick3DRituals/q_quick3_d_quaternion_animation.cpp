//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dquaternionanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dquaternionanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DQuaternionAnimation that Python can take functions over in. Every QQuick3DQuaternionAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuick3DQuaternionAnimationCall0)(const void *, int *);
typedef void (*CuteQQuick3DQuaternionAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuick3DQuaternionAnimationCall2)(const void *, int *);
typedef void (*CuteQQuick3DQuaternionAnimationCall3)(const void *, int *);
typedef int (*CuteQQuick3DQuaternionAnimationCall4)(const void *, int *);
typedef void (*CuteQQuick3DQuaternionAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuaternionAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuaternionAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DQuaternionAnimation : public QQuick3DQuaternionAnimation {
public:
  using QQuick3DQuaternionAnimation::QQuick3DQuaternionAnimation;
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
      CuteQQuick3DQuaternionAnimationCall0 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DQuaternionAnimationCall1 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DQuaternionAnimationCall2 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DQuaternionAnimationCall3 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DQuaternionAnimationCall4 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DQuaternionAnimationCall5 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall5>(taken[5]);
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
      CuteQQuick3DQuaternionAnimationCall6 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall6>(taken[6]);
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
      CuteQQuick3DQuaternionAnimationCall7 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall7>(taken[7]);
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
      CuteQQuick3DQuaternionAnimationCall8 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall8>(taken[8]);
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
      CuteQQuick3DQuaternionAnimationCall9 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall9>(taken[9]);
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
      CuteQQuick3DQuaternionAnimationCall10 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall10>(taken[10]);
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
      CuteQQuick3DQuaternionAnimationCall11 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall11>(taken[11]);
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
      CuteQQuick3DQuaternionAnimationCall12 call = reinterpret_cast<CuteQQuick3DQuaternionAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DQuaternionAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuick3DQuaternionAnimation10metaObjectEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->metaObject();
}

//  QString QQuick3DQuaternionAnimation::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuick3DQuaternionAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DQuaternionAnimation::tr(s, c, n));
}

//  QQuick3DQuaternionAnimation::QQuick3DQuaternionAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DQuaternionAnimation *ritual_ZN27QQuick3DQuaternionAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DQuaternionAnimation(parent);
}

//  QQuaternion QQuick3DQuaternionAnimation::from() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK27QQuick3DQuaternionAnimation4fromEv(
    const QQuick3DQuaternionAnimation *self) {
  return new QQuaternion(self->from());
}

//  void QQuick3DQuaternionAnimation::setFrom(const QQuaternion &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation7setFromERK11QQuaternion(
    QQuick3DQuaternionAnimation *self,
    const QQuaternion *f) {
  self->setFrom(*f);
}

//  QQuaternion QQuick3DQuaternionAnimation::to() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK27QQuick3DQuaternionAnimation2toEv(
    const QQuick3DQuaternionAnimation *self) {
  return new QQuaternion(self->to());
}

//  void QQuick3DQuaternionAnimation::setTo(const QQuaternion &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation5setToERK11QQuaternion(
    QQuick3DQuaternionAnimation *self,
    const QQuaternion *t) {
  self->setTo(*t);
}

//  Type QQuick3DQuaternionAnimation::type() const
extern "C" Q_DECL_EXPORT
QQuick3DQuaternionAnimation::Type ritual_ZNK27QQuick3DQuaternionAnimation4typeEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->type();
}

//  void QQuick3DQuaternionAnimation::setType(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation7setTypeENS_4TypeE(
    QQuick3DQuaternionAnimation *self,
    QQuick3DQuaternionAnimation::Type type) {
  self->setType(type);
}

//  float QQuick3DQuaternionAnimation::fromXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation13fromXRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->fromXRotation();
}

//  void QQuick3DQuaternionAnimation::setFromXRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation16setFromXRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setFromXRotation(f);
}

//  float QQuick3DQuaternionAnimation::fromYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation13fromYRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->fromYRotation();
}

//  void QQuick3DQuaternionAnimation::setFromYRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation16setFromYRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setFromYRotation(f);
}

//  float QQuick3DQuaternionAnimation::fromZRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation13fromZRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->fromZRotation();
}

//  void QQuick3DQuaternionAnimation::setFromZRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation16setFromZRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setFromZRotation(f);
}

//  float QQuick3DQuaternionAnimation::toXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation11toXRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->toXRotation();
}

//  void QQuick3DQuaternionAnimation::setToXRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation14setToXRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setToXRotation(f);
}

//  float QQuick3DQuaternionAnimation::toYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation11toYRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->toYRotation();
}

//  void QQuick3DQuaternionAnimation::setToYRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation14setToYRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setToYRotation(f);
}

//  float QQuick3DQuaternionAnimation::toZRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QQuick3DQuaternionAnimation11toZRotationEv(
    const QQuick3DQuaternionAnimation *self) {
  return self->toZRotation();
}

//  void QQuick3DQuaternionAnimation::setToZRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuick3DQuaternionAnimation14setToZRotationEf(
    QQuick3DQuaternionAnimation *self,
    float f) {
  self->setToZRotation(f);
}

//  a Python function taken by a CuteQQuick3DQuaternionAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DQuaternionAnimation(
    QQuick3DQuaternionAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DQuaternionAnimation *>(self)->take(key, call);
}
