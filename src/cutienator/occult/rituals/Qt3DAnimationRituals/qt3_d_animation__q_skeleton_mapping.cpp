//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qskeletonmapping.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qskeletonmapping.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QSkeletonMapping that Python can take functions over in. Every Qt3DAnimation::QSkeletonMapping
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QSkeletonMappingCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QSkeletonMappingCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QSkeletonMappingCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QSkeletonMappingCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QSkeletonMappingCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QSkeletonMappingCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QSkeletonMappingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QSkeletonMapping : public Qt3DAnimation::QSkeletonMapping {
public:
  using Qt3DAnimation::QSkeletonMapping::QSkeletonMapping;
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
      CuteQt3DAnimation_QSkeletonMappingCall0 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall0>(taken[0]);
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
      CuteQt3DAnimation_QSkeletonMappingCall1 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall1>(taken[1]);
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
      CuteQt3DAnimation_QSkeletonMappingCall2 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall2>(taken[2]);
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
      CuteQt3DAnimation_QSkeletonMappingCall3 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall3>(taken[3]);
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
      CuteQt3DAnimation_QSkeletonMappingCall4 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall4>(taken[4]);
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
      CuteQt3DAnimation_QSkeletonMappingCall5 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall5>(taken[5]);
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
      CuteQt3DAnimation_QSkeletonMappingCall6 call = reinterpret_cast<CuteQt3DAnimation_QSkeletonMappingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QSkeletonMapping::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation16QSkeletonMapping10metaObjectEv(
    const Qt3DAnimation::QSkeletonMapping *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QSkeletonMapping::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation16QSkeletonMapping11qt_metacastEPKc(
    Qt3DAnimation::QSkeletonMapping *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QSkeletonMapping::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation16QSkeletonMapping11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QSkeletonMapping *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QSkeletonMapping::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation16QSkeletonMapping2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QSkeletonMapping::tr(s, c, n));
}

//  Qt3DAnimation::QSkeletonMapping::QSkeletonMapping(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QSkeletonMapping *ritual_ZN13Qt3DAnimation16QSkeletonMappingC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QSkeletonMapping(parent);
}

//  Qt3DAnimation::QSkeletonMapping::~QSkeletonMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation16QSkeletonMappingD1Ev(
    Qt3DAnimation::QSkeletonMapping *self) {
  delete self;
}

//  Qt3DCore::QAbstractSkeleton *Qt3DAnimation::QSkeletonMapping::skeleton()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeleton *ritual_ZNK13Qt3DAnimation16QSkeletonMapping8skeletonEv(
    const Qt3DAnimation::QSkeletonMapping *self) {
  return self->skeleton();
}

//  void
//      Qt3DAnimation::QSkeletonMapping::setSkeleton(Qt3DCore::QAbstractSkele
//      ton *skeleton)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation16QSkeletonMapping11setSkeletonEPN8Qt3DCore17QAbstractSkeletonE(
    Qt3DAnimation::QSkeletonMapping *self,
    Qt3DCore::QAbstractSkeleton *skeleton) {
  self->setSkeleton(skeleton);
}

//  void Qt3DAnimation::QSkeletonMapping::skeletonChanged(Qt3DCore::QAbstract
//      Skeleton *skeleton)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation16QSkeletonMapping15skeletonChangedEPN8Qt3DCore17QAbstractSkeletonE(
    Qt3DAnimation::QSkeletonMapping *self,
    Qt3DCore::QAbstractSkeleton *skeleton) {
  self->skeletonChanged(skeleton);
}

//  Qt3DAnimation::QSkeletonMapping::QSkeletonMapping(QSkeletonMappingPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QSkeletonMapping *ritual_ZN13Qt3DAnimation16QSkeletonMappingC1ERNS_23QSkeletonMappingPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QSkeletonMappingPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QSkeletonMapping(*dd, parent);
}

//  QSkeletonMappingPrivate *Qt3DAnimation::QSkeletonMapping::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QSkeletonMappingPrivate *ritual_ZN13Qt3DAnimation16QSkeletonMapping6d_funcEv(
    Qt3DAnimation::QSkeletonMapping *self) {
  return self->d_func();
}

//  const QSkeletonMappingPrivate *Qt3DAnimation::QSkeletonMapping::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QSkeletonMappingPrivate *ritual_ZNK13Qt3DAnimation16QSkeletonMapping6d_funcEv(
    const Qt3DAnimation::QSkeletonMapping *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QSkeletonMapping, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QSkeletonMapping(
    Qt3DAnimation::QSkeletonMapping *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QSkeletonMapping *>(self)->take(key, call);
}
