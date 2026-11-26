//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QQuickGeoCoordinateAnimation that Python can take functions over in. Every QQuickGeoCoordinateAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickGeoCoordinateAnimationCall0)(const void *, int *);
typedef void (*CuteQQuickGeoCoordinateAnimationCall1)(const void *, int, int *);
typedef void (*CuteQQuickGeoCoordinateAnimationCall2)(const void *, int *);
typedef void (*CuteQQuickGeoCoordinateAnimationCall3)(const void *, int *);
typedef int (*CuteQQuickGeoCoordinateAnimationCall4)(const void *, int *);
typedef void (*CuteQQuickGeoCoordinateAnimationCall5)(const void *, const QQmlProperty *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGeoCoordinateAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGeoCoordinateAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGeoCoordinateAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGeoCoordinateAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGeoCoordinateAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGeoCoordinateAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGeoCoordinateAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGeoCoordinateAnimation : public QQuickGeoCoordinateAnimation {
public:
  using QQuickGeoCoordinateAnimation::QQuickGeoCoordinateAnimation;
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
      CuteQQuickGeoCoordinateAnimationCall0 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPropertyAnimation::duration();
  }

  //  void QQuickPropertyAnimation::setDuration(int a0)
  void setDuration(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickGeoCoordinateAnimationCall1 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimation::setDuration(a0);
  }

  //  void QQuickAbstractAnimation::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickGeoCoordinateAnimationCall2 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::classBegin();
  }

  //  void QQuickAbstractAnimation::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickGeoCoordinateAnimationCall3 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimation::componentComplete();
  }

  //  ThreadingModel QQuickAbstractAnimation::threadingModel() const
  QQuickAbstractAnimation::ThreadingModel threadingModel() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickGeoCoordinateAnimationCall4 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickAbstractAnimation::ThreadingModel>(given);
    }
    return QQuickAbstractAnimation::threadingModel();
  }

  //  void QQuickAbstractAnimation::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickGeoCoordinateAnimationCall5 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall5>(taken[5]);
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
      CuteQQuickGeoCoordinateAnimationCall6 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall6>(taken[6]);
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
      CuteQQuickGeoCoordinateAnimationCall7 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall7>(taken[7]);
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
      CuteQQuickGeoCoordinateAnimationCall8 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall8>(taken[8]);
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
      CuteQQuickGeoCoordinateAnimationCall9 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall9>(taken[9]);
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
      CuteQQuickGeoCoordinateAnimationCall10 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall10>(taken[10]);
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
      CuteQQuickGeoCoordinateAnimationCall11 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall11>(taken[11]);
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
      CuteQQuickGeoCoordinateAnimationCall12 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGeoCoordinateAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickGeoCoordinateAnimation10metaObjectEv(
    const QQuickGeoCoordinateAnimation *self) {
  return self->metaObject();
}

//  void *QQuickGeoCoordinateAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickGeoCoordinateAnimation11qt_metacastEPKc(
    QQuickGeoCoordinateAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGeoCoordinateAnimation::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickGeoCoordinateAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGeoCoordinateAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGeoCoordinateAnimation::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickGeoCoordinateAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGeoCoordinateAnimation::tr(s, c, n));
}

//  QQuickGeoCoordinateAnimationPrivate
//      *QQuickGeoCoordinateAnimation::d_func()
extern "C" Q_DECL_EXPORT
QQuickGeoCoordinateAnimationPrivate *ritual_ZN28QQuickGeoCoordinateAnimation6d_funcEv(
    QQuickGeoCoordinateAnimation *self) {
  return self->d_func();
}

//  const QQuickGeoCoordinateAnimationPrivate
//      *QQuickGeoCoordinateAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickGeoCoordinateAnimationPrivate *ritual_ZNK28QQuickGeoCoordinateAnimation6d_funcEv(
    const QQuickGeoCoordinateAnimation *self) {
  return self->d_func();
}

//  QQuickGeoCoordinateAnimation::QQuickGeoCoordinateAnimation(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickGeoCoordinateAnimation *ritual_ZN28QQuickGeoCoordinateAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickGeoCoordinateAnimation(parent);
}

//  QQuickGeoCoordinateAnimation::~QQuickGeoCoordinateAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickGeoCoordinateAnimationD1Ev(
    QQuickGeoCoordinateAnimation *self) {
  delete self;
}

//  QGeoCoordinate QQuickGeoCoordinateAnimation::from() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK28QQuickGeoCoordinateAnimation4fromEv(
    const QQuickGeoCoordinateAnimation *self) {
  return new QGeoCoordinate(self->from());
}

//  void QQuickGeoCoordinateAnimation::setFrom(const QGeoCoordinate &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickGeoCoordinateAnimation7setFromERK14QGeoCoordinate(
    QQuickGeoCoordinateAnimation *self,
    const QGeoCoordinate *a0) {
  self->setFrom(*a0);
}

//  QGeoCoordinate QQuickGeoCoordinateAnimation::to() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK28QQuickGeoCoordinateAnimation2toEv(
    const QQuickGeoCoordinateAnimation *self) {
  return new QGeoCoordinate(self->to());
}

//  void QQuickGeoCoordinateAnimation::setTo(const QGeoCoordinate &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickGeoCoordinateAnimation5setToERK14QGeoCoordinate(
    QQuickGeoCoordinateAnimation *self,
    const QGeoCoordinate *a0) {
  self->setTo(*a0);
}

//  Direction QQuickGeoCoordinateAnimation::direction() const
extern "C" Q_DECL_EXPORT
QQuickGeoCoordinateAnimation::Direction ritual_ZNK28QQuickGeoCoordinateAnimation9directionEv(
    const QQuickGeoCoordinateAnimation *self) {
  return self->direction();
}

//  void QQuickGeoCoordinateAnimation::setDirection(Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickGeoCoordinateAnimation12setDirectionENS_9DirectionE(
    QQuickGeoCoordinateAnimation *self,
    QQuickGeoCoordinateAnimation::Direction direction) {
  self->setDirection(direction);
}

//  QBindable<Direction> QQuickGeoCoordinateAnimation::bindableDirection()
extern "C" Q_DECL_EXPORT
QBindable<QQuickGeoCoordinateAnimation::Direction> *ritual_ZN28QQuickGeoCoordinateAnimation17bindableDirectionEv(
    QQuickGeoCoordinateAnimation *self) {
  return new QBindable<QQuickGeoCoordinateAnimation::Direction>(
      self->bindableDirection());
}

//  void QQuickGeoCoordinateAnimation::directionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickGeoCoordinateAnimation16directionChangedEv(
    QQuickGeoCoordinateAnimation *self) {
  self->directionChanged();
}

//  a Python function taken by a CuteQQuickGeoCoordinateAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGeoCoordinateAnimation(
    QQuickGeoCoordinateAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGeoCoordinateAnimation *>(self)->take(key, call);
}

//  a QBindable<QQuickGeoCoordinateAnimation::Direction> a ritual of
//      QQuickGeoCoordinateAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickGeoCoordinateAnimation__QBindable_QQuickGeoCoordinateAnimation_Direction(
    QBindable<QQuickGeoCoordinateAnimation::Direction> *self) {
  delete self;
}
