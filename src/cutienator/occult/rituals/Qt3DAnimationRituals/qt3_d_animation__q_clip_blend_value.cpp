//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qclipblendvalue.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qclipblendvalue.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QClipBlendValue that Python can take functions over in. Every Qt3DAnimation::QClipBlendValue
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QClipBlendValueCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QClipBlendValueCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClipBlendValueCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClipBlendValueCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClipBlendValueCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClipBlendValueCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClipBlendValueCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QClipBlendValue : public Qt3DAnimation::QClipBlendValue {
public:
  using Qt3DAnimation::QClipBlendValue::QClipBlendValue;
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
      CuteQt3DAnimation_QClipBlendValueCall0 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall0>(taken[0]);
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
      CuteQt3DAnimation_QClipBlendValueCall1 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall1>(taken[1]);
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
      CuteQt3DAnimation_QClipBlendValueCall2 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall2>(taken[2]);
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
      CuteQt3DAnimation_QClipBlendValueCall3 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall3>(taken[3]);
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
      CuteQt3DAnimation_QClipBlendValueCall4 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall4>(taken[4]);
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
      CuteQt3DAnimation_QClipBlendValueCall5 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall5>(taken[5]);
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
      CuteQt3DAnimation_QClipBlendValueCall6 call = reinterpret_cast<CuteQt3DAnimation_QClipBlendValueCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QClipBlendValue::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation15QClipBlendValue10metaObjectEv(
    const Qt3DAnimation::QClipBlendValue *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QClipBlendValue::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation15QClipBlendValue11qt_metacastEPKc(
    Qt3DAnimation::QClipBlendValue *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QClipBlendValue::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation15QClipBlendValue11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QClipBlendValue *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QClipBlendValue::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation15QClipBlendValue2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QClipBlendValue::tr(s, c, n));
}

//  Qt3DAnimation::QClipBlendValue::QClipBlendValue(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClipBlendValue *ritual_ZN13Qt3DAnimation15QClipBlendValueC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QClipBlendValue(parent);
}

//  Qt3DAnimation::QClipBlendValue::QClipBlendValue(Qt3DAnimation::QAbstractA
//      nimationClip *clip, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClipBlendValue *ritual_ZN13Qt3DAnimation15QClipBlendValueC1EPNS_22QAbstractAnimationClipEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QAbstractAnimationClip *clip,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QClipBlendValue(clip, parent);
}

//  Qt3DAnimation::QClipBlendValue::~QClipBlendValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QClipBlendValueD1Ev(
    Qt3DAnimation::QClipBlendValue *self) {
  delete self;
}

//  Qt3DAnimation::QAbstractAnimationClip
//      *Qt3DAnimation::QClipBlendValue::clip() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimationClip *ritual_ZNK13Qt3DAnimation15QClipBlendValue4clipEv(
    const Qt3DAnimation::QClipBlendValue *self) {
  return self->clip();
}

//  void Qt3DAnimation::QClipBlendValue::setClip(Qt3DAnimation::QAbstractAnim
//      ationClip *clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QClipBlendValue7setClipEPNS_22QAbstractAnimationClipE(
    Qt3DAnimation::QClipBlendValue *self,
    Qt3DAnimation::QAbstractAnimationClip *clip) {
  self->setClip(clip);
}

//  void Qt3DAnimation::QClipBlendValue::clipChanged(Qt3DAnimation::QAbstract
//      AnimationClip *clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QClipBlendValue11clipChangedEPNS_22QAbstractAnimationClipE(
    Qt3DAnimation::QClipBlendValue *self,
    Qt3DAnimation::QAbstractAnimationClip *clip) {
  self->clipChanged(clip);
}

//  Qt3DAnimation::QClipBlendValue::QClipBlendValue(QClipBlendValuePrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClipBlendValue *ritual_ZN13Qt3DAnimation15QClipBlendValueC1ERNS_22QClipBlendValuePrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QClipBlendValuePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QClipBlendValue(*dd, parent);
}

//  QClipBlendValuePrivate *Qt3DAnimation::QClipBlendValue::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClipBlendValuePrivate *ritual_ZN13Qt3DAnimation15QClipBlendValue6d_funcEv(
    Qt3DAnimation::QClipBlendValue *self) {
  return self->d_func();
}

//  const QClipBlendValuePrivate *Qt3DAnimation::QClipBlendValue::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QClipBlendValuePrivate *ritual_ZNK13Qt3DAnimation15QClipBlendValue6d_funcEv(
    const Qt3DAnimation::QClipBlendValue *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QClipBlendValue, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QClipBlendValue(
    Qt3DAnimation::QClipBlendValue *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QClipBlendValue *>(self)->take(key, call);
}
