//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qabstractskeleton.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qabstractskeleton.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QAbstractSkeleton that Python can take functions over in. Every Qt3DCore::QAbstractSkeleton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractSkeletonCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractSkeletonCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractSkeletonCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractSkeletonCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractSkeletonCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractSkeletonCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractSkeletonCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAbstractSkeleton : public Qt3DCore::QAbstractSkeleton {
public:
  using Qt3DCore::QAbstractSkeleton::QAbstractSkeleton;
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
      CuteQt3DCore_QAbstractSkeletonCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall0>(taken[0]);
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
      CuteQt3DCore_QAbstractSkeletonCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall1>(taken[1]);
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
      CuteQt3DCore_QAbstractSkeletonCall2 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall2>(taken[2]);
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
      CuteQt3DCore_QAbstractSkeletonCall3 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall3>(taken[3]);
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
      CuteQt3DCore_QAbstractSkeletonCall4 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall4>(taken[4]);
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
      CuteQt3DCore_QAbstractSkeletonCall5 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall5>(taken[5]);
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
      CuteQt3DCore_QAbstractSkeletonCall6 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAbstractSkeleton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore17QAbstractSkeleton10metaObjectEv(
    const Qt3DCore::QAbstractSkeleton *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QAbstractSkeleton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore17QAbstractSkeleton11qt_metacastEPKc(
    Qt3DCore::QAbstractSkeleton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QAbstractSkeleton::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore17QAbstractSkeleton11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QAbstractSkeleton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QAbstractSkeleton::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore17QAbstractSkeleton2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAbstractSkeleton::tr(s, c, n));
}

//  Qt3DCore::QAbstractSkeleton::~QAbstractSkeleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAbstractSkeletonD1Ev(
    Qt3DCore::QAbstractSkeleton *self) {
  delete self;
}

//  int Qt3DCore::QAbstractSkeleton::jointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8Qt3DCore17QAbstractSkeleton10jointCountEv(
    const Qt3DCore::QAbstractSkeleton *self) {
  return self->jointCount();
}

//  void Qt3DCore::QAbstractSkeleton::jointCountChanged(int jointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAbstractSkeleton17jointCountChangedEi(
    Qt3DCore::QAbstractSkeleton *self,
    int jointCount) {
  self->jointCountChanged(jointCount);
}

//  Qt3DCore::QAbstractSkeleton::QAbstractSkeleton(QAbstractSkeletonPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeleton *ritual_ZN8Qt3DCore17QAbstractSkeletonC1ERNS_24QAbstractSkeletonPrivateEPNS_5QNodeE(
    Qt3DCore::QAbstractSkeletonPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QAbstractSkeleton(*dd, parent);
}

//  QAbstractSkeletonPrivate *Qt3DCore::QAbstractSkeleton::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeletonPrivate *ritual_ZN8Qt3DCore17QAbstractSkeleton6d_funcEv(
    Qt3DCore::QAbstractSkeleton *self) {
  return self->d_func();
}

//  const QAbstractSkeletonPrivate *Qt3DCore::QAbstractSkeleton::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractSkeletonPrivate *ritual_ZNK8Qt3DCore17QAbstractSkeleton6d_funcEv(
    const Qt3DCore::QAbstractSkeleton *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QAbstractSkeleton, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractSkeleton(
    Qt3DCore::QAbstractSkeleton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractSkeleton *>(self)->take(key, call);
}
