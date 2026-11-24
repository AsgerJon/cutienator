//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickAnima
//  tion/6.12.0/Qt3DQuickAnimation/private/quick3dmorphinganimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/qt3dquickanimation_global_p.h>
#include <Qt3DQuickAnimation/Qt3DQuickAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickAnimation/6.12.0/Qt3DQuickAnimation/private/quick3dmorphinganimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::Quick::QQuick3DMorphingAnimation that Python can take functions over in. Every Qt3DAnimation::Quick::QQuick3DMorphingAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_Quick_QQuick3DMorphingAnimation : public Qt3DAnimation::Quick::QQuick3DMorphingAnimation {
public:
  using Qt3DAnimation::Quick::QQuick3DMorphingAnimation::QQuick3DMorphingAnimation;
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall0 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall0>(taken[0]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall1 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall1>(taken[1]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall2 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall2>(taken[2]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall3 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall3>(taken[3]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall4 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall4>(taken[4]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall5 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall5>(taken[5]);
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
      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall6 call = reinterpret_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DAnimation::Quick::QQuick3DMorphingAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation5Quick25QQuick3DMorphingAnimation10metaObjectEv(
    const Qt3DAnimation::Quick::QQuick3DMorphingAnimation *self) {
  return self->metaObject();
}

//  QString Qt3DAnimation::Quick::QQuick3DMorphingAnimation::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation5Quick25QQuick3DMorphingAnimation2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DAnimation::Quick::QQuick3DMorphingAnimation::tr(
          s,
          c,
          n));
}

//  QMorphingAnimation *Qt3DAnimation::Quick::QQuick3DMorphingAnimation::pare
//      ntMorphingAnimation() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimation *ritual_ZNK13Qt3DAnimation5Quick25QQuick3DMorphingAnimation23parentMorphingAnimationEv(
    const Qt3DAnimation::Quick::QQuick3DMorphingAnimation *self) {
  return self->parentMorphingAnimation();
}

//  a Python function taken by a
//      CuteQt3DAnimation_Quick_QQuick3DMorphingAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Quick_QQuick3DMorphingAnimation(
    Qt3DAnimation::Quick::QQuick3DMorphingAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Quick_QQuick3DMorphingAnimation *>(self)->take(key, call);
}
