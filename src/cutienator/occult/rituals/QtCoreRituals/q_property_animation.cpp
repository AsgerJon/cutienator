//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPropertyAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPropertyAnimation : QPropertyAnimation {
  using QPropertyAnimation::event;
  using QPropertyAnimation::updateCurrentValue;
  using QPropertyAnimation::updateState;
};

//  A QPropertyAnimation that Python can take functions over in. Every QPropertyAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQPropertyAnimationCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQPropertyAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQPropertyAnimationCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteQPropertyAnimationCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQPropertyAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQPropertyAnimationCall5)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQPropertyAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPropertyAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPropertyAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPropertyAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPropertyAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPropertyAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPropertyAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPropertyAnimation : public QPropertyAnimation {
public:
  using QPropertyAnimation::QPropertyAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QPropertyAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPropertyAnimationCall0 call = reinterpret_cast<CuteQPropertyAnimationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPropertyAnimation::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QPropertyAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPropertyAnimationCall1 call = reinterpret_cast<CuteQPropertyAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QPropertyAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QPropertyAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPropertyAnimationCall2 call = reinterpret_cast<CuteQPropertyAnimationCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QPropertyAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPropertyAnimationCall3 call = reinterpret_cast<CuteQPropertyAnimationCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::duration();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPropertyAnimationCall4 call = reinterpret_cast<CuteQPropertyAnimationCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  QVariant QVariantAnimation::interpolated(const QVariant &from, const
  //      QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPropertyAnimationCall5 call = reinterpret_cast<CuteQPropertyAnimationCall5>(taken[5]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return QVariantAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPropertyAnimationCall6 call = reinterpret_cast<CuteQPropertyAnimationCall6>(taken[6]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPropertyAnimationCall7 call = reinterpret_cast<CuteQPropertyAnimationCall7>(taken[7]);
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
      CuteQPropertyAnimationCall8 call = reinterpret_cast<CuteQPropertyAnimationCall8>(taken[8]);
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
      CuteQPropertyAnimationCall9 call = reinterpret_cast<CuteQPropertyAnimationCall9>(taken[9]);
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
      CuteQPropertyAnimationCall10 call = reinterpret_cast<CuteQPropertyAnimationCall10>(taken[10]);
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
      CuteQPropertyAnimationCall11 call = reinterpret_cast<CuteQPropertyAnimationCall11>(taken[11]);
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
      CuteQPropertyAnimationCall12 call = reinterpret_cast<CuteQPropertyAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPropertyAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPropertyAnimation10metaObjectEv(
    const QPropertyAnimation *self) {
  return self->metaObject();
}

//  QString QPropertyAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPropertyAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPropertyAnimation::tr(s, c, n));
}

//  QPropertyAnimation::QPropertyAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QPropertyAnimation *ritual_ZN18QPropertyAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQPropertyAnimation(parent);
}

//  QPropertyAnimation::QPropertyAnimation(QObject *target, const QByteArray
//      &propertyName, QObject *parent)
extern "C" Q_DECL_EXPORT
QPropertyAnimation *ritual_ZN18QPropertyAnimationC1EP7QObjectRK10QByteArrayS1_(
    QObject *target,
    const QByteArray *propertyName,
    QObject *parent) {
  return new CuteQPropertyAnimation(target, *propertyName, parent);
}

//  QPropertyAnimation::~QPropertyAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimationD1Ev(QPropertyAnimation *self) {
  delete self;
}

//  QObject *QPropertyAnimation::targetObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QPropertyAnimation12targetObjectEv(
    const QPropertyAnimation *self) {
  return self->targetObject();
}

//  void QPropertyAnimation::setTargetObject(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation15setTargetObjectEP7QObject(
    QPropertyAnimation *self,
    QObject *target) {
  self->setTargetObject(target);
}

//  QByteArray QPropertyAnimation::propertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QPropertyAnimation12propertyNameEv(
    const QPropertyAnimation *self) {
  return new QByteArray(self->propertyName());
}

//  void QPropertyAnimation::setPropertyName(const QByteArray &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation15setPropertyNameERK10QByteArray(
    QPropertyAnimation *self,
    const QByteArray *propertyName) {
  self->setPropertyName(*propertyName);
}

//  bool QPropertyAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QPropertyAnimation5eventEP6QEvent(
    QPropertyAnimation *self,
    QEvent *event) {
  return self->event(event);
}

//  void QPropertyAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation18updateCurrentValueERK8QVariant(
    QPropertyAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  void QPropertyAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    QPropertyAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  QPropertyAnimationPrivate *QPropertyAnimation::d_func()
extern "C" Q_DECL_EXPORT
QPropertyAnimationPrivate *ritual_ZN18QPropertyAnimation6d_funcEv(
    QPropertyAnimation *self) {
  return self->d_func();
}

//  const QPropertyAnimationPrivate *QPropertyAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QPropertyAnimationPrivate *ritual_ZNK18QPropertyAnimation6d_funcEv(
    const QPropertyAnimation *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPropertyAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPropertyAnimation(
    QPropertyAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPropertyAnimation *>(self)->take(key, call);
}

//  bool QPropertyAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QPropertyAnimation5eventEP6QEvent(
    QPropertyAnimation *self,
    QEvent *event) {
  return static_cast<OwnQPropertyAnimation *>(self)->OwnQPropertyAnimation::event(
      event);
}

//  void QPropertyAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPropertyAnimation18updateCurrentValueERK8QVariant(
    QPropertyAnimation *self,
    const QVariant *value) {
  static_cast<OwnQPropertyAnimation *>(self)->OwnQPropertyAnimation::updateCurrentValue(
      *value);
}

//  void QPropertyAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPropertyAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    QPropertyAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnQPropertyAnimation *>(self)->OwnQPropertyAnimation::updateState(
      newState,
      oldState);
}

#endif  // QT_CONFIG(animation)
