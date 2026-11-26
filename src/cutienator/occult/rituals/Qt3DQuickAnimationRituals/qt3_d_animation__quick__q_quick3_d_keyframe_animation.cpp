//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickAnima
//  tion/6.12.0/Qt3DQuickAnimation/private/quick3dkeyframeanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimation_global_p.h>
#include <Qt3DQuickAnimation/Qt3DQuickAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/quick3dkeyframeanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DAnimation::Quick::QQuick3DKeyframeAnimation that Python can take functions over in. Every Qt3DAnimation::Quick::QQuick3DKeyframeAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimation : public Qt3DAnimation::Quick::QQuick3DKeyframeAnimation {
public:
  using Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::QQuick3DKeyframeAnimation;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall0 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall1 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall2 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall3 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall4 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall5 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall6 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation10metaObjectEv(
    const Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation11qt_metacastEPKc(
    Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::qt_metacall(QMetaObj
//      ect::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::tr(
          s,
          c,
          n));
}

//  Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::QQuick3DKeyframeAnimatio
//      n(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *ritual_ZN13Qt3DAnimation5Quick25QQuick3DKeyframeAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimation(parent);
}

//  QKeyframeAnimation *Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::pare
//      ntKeyframeAnimation() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimation *ritual_ZNK13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation23parentKeyframeAnimationEv(
    const Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self) {
  return self->parentKeyframeAnimation();
}

//  QQmlListProperty<Qt3DCore::QTransform>
//      Qt3DAnimation::Quick::QQuick3DKeyframeAnimation::keyframes()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DCore::QTransform> *ritual_ZN13Qt3DAnimation5Quick25QQuick3DKeyframeAnimation9keyframesEv(
    Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self) {
  return new QQmlListProperty<Qt3DCore::QTransform>(self->keyframes());
}

//  a Python function taken by a
//      CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Quick_QQuick3DKeyframeAnimation(
    Qt3DAnimation::Quick::QQuick3DKeyframeAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Quick_QQuick3DKeyframeAnimation *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DCore::QTransform> a ritual of
//      Qt3DAnimation::Quick::QQuick3DKeyframeAnimation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Quick_QQuick3DKeyframeAnimation__QQmlListProperty_Qt3DCore_QTransform(
    QQmlListProperty<Qt3DCore::QTransform> *self) {
  delete self;
}
