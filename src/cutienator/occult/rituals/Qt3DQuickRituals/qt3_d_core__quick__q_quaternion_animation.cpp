//  Written by hand on 2026-11-25 from
//  Qt3DQuick/6.12.0/Qt3DQuick/private/qquaternionanimation_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: 'qt_metacast', and the free function
//  'q_quaternionInterpolator', which is not of the class. The class
//  declares no virtual function, so it has no 'own_' rituals; the
//  functions Python takes over are those of its bases.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qquaternionanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::Quick::QQuaternionAnimation that Python can take functions
//  over in. Every Qt3DCore::Quick::QQuaternionAnimation Python makes is
//  one. Each function below asks the Python function handed over for it,
//  and runs Qt's own without one.
typedef int (*CuteQt3DCore_Quick_QQuaternionAnimationCall0)(const void *, int *);
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall1)(const void *, int, int *);
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall2)(const void *, int *);
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall3)(const void *, int *);
typedef int (*CuteQt3DCore_Quick_QQuaternionAnimationCall4)(const void *, int *);
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_QQuaternionAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_Quick_QQuaternionAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_Quick_QQuaternionAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_Quick_QQuaternionAnimation : public Qt3DCore::Quick::QQuaternionAnimation {
public:
  using Qt3DCore::Quick::QQuaternionAnimation::QQuaternionAnimation;
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall0 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_Quick_QQuaternionAnimationCall1 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_Quick_QQuaternionAnimationCall2 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_Quick_QQuaternionAnimationCall3 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_Quick_QQuaternionAnimationCall4 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_Quick_QQuaternionAnimationCall5 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall5>(taken[5]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall6 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall6>(taken[6]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall7 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall7>(taken[7]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall8 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall8>(taken[8]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall9 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall9>(taken[9]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall10 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall10>(taken[10]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall11 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall11>(taken[11]);
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
      CuteQt3DCore_Quick_QQuaternionAnimationCall12 call = reinterpret_cast<CuteQt3DCore_Quick_QQuaternionAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::Quick::QQuaternionAnimation::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation10metaObjectEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->metaObject();
}

//  QString Qt3DCore::Quick::QQuaternionAnimation::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::QQuaternionAnimation::tr(s, c, n));
}

//  Qt3DCore::Quick::QQuaternionAnimationPrivate
//      *Qt3DCore::Quick::QQuaternionAnimation::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQuaternionAnimationPrivate *ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation6d_funcEv(
    Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->d_func();
}

//  const Qt3DCore::Quick::QQuaternionAnimationPrivate
//      *Qt3DCore::Quick::QQuaternionAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::QQuaternionAnimationPrivate *ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation6d_funcEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->d_func();
}

//  Qt3DCore::Quick::QQuaternionAnimation::QQuaternionAnimation(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQuaternionAnimation *ritual_ZN8Qt3DCore5Quick20QQuaternionAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_Quick_QQuaternionAnimation(parent);
}

//  QQuaternion Qt3DCore::Quick::QQuaternionAnimation::from() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation4fromEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return new QQuaternion(self->from());
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setFrom(const QQuaternion &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation7setFromERK11QQuaternion(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    const QQuaternion *f) {
  self->setFrom(*f);
}

//  QQuaternion Qt3DCore::Quick::QQuaternionAnimation::to() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation2toEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return new QQuaternion(self->to());
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setTo(const QQuaternion &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation5setToERK11QQuaternion(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    const QQuaternion *t) {
  self->setTo(*t);
}

//  Type Qt3DCore::Quick::QQuaternionAnimation::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation4typeEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return static_cast<int>(self->type());
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setType(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation7setTypeENS1_4TypeE(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    Qt3DCore::Quick::QQuaternionAnimation::Type type) {
  self->setType(type);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::fromXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromXRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->fromXRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setFromXRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromXRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setFromXRotation(f);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::fromYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromYRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->fromYRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setFromYRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromYRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setFromYRotation(f);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::fromZRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation13fromZRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->fromZRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setFromZRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation16setFromZRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setFromZRotation(f);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::toXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toXRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->toXRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setToXRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToXRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setToXRotation(f);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::toYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toYRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->toYRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setToYRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToYRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setToYRotation(f);
}

//  float Qt3DCore::Quick::QQuaternionAnimation::toZRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore5Quick20QQuaternionAnimation11toZRotationEv(
    const Qt3DCore::Quick::QQuaternionAnimation *self) {
  return self->toZRotation();
}

//  void Qt3DCore::Quick::QQuaternionAnimation::setToZRotation(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation14setToZRotationEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float f) {
  self->setToZRotation(f);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::typeChanged(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation11typeChangedENS1_4TypeE(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    Qt3DCore::Quick::QQuaternionAnimation::Type type) {
  self->typeChanged(type);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::fromXRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromXRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->fromXRotationChanged(value);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::fromYRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromYRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->fromYRotationChanged(value);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::fromZRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation20fromZRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->fromZRotationChanged(value);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::toXRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toXRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->toXRotationChanged(value);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::toYRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toYRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->toYRotationChanged(value);
}

//  void Qt3DCore::Quick::QQuaternionAnimation::toZRotationChanged(float
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick20QQuaternionAnimation18toZRotationChangedEf(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    float value) {
  self->toZRotationChanged(value);
}

//  a Python function taken by a CuteQt3DCore_Quick_QQuaternionAnimation, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_Quick_QQuaternionAnimation(
    Qt3DCore::Quick::QQuaternionAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_Quick_QQuaternionAnimation *>(self)->take(key, call);
}
