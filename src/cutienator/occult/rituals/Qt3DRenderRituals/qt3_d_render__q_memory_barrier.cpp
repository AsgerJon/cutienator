//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qmemorybarrier.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qmemorybarrier.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QMemoryBarrier that Python can take functions over in. Every Qt3DRender::QMemoryBarrier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMemoryBarrierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMemoryBarrierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMemoryBarrierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMemoryBarrierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMemoryBarrierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMemoryBarrierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMemoryBarrierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QMemoryBarrier : public Qt3DRender::QMemoryBarrier {
public:
  using Qt3DRender::QMemoryBarrier::QMemoryBarrier;
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
      CuteQt3DRender_QMemoryBarrierCall0 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall0>(taken[0]);
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
      CuteQt3DRender_QMemoryBarrierCall1 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall1>(taken[1]);
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
      CuteQt3DRender_QMemoryBarrierCall2 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall2>(taken[2]);
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
      CuteQt3DRender_QMemoryBarrierCall3 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall3>(taken[3]);
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
      CuteQt3DRender_QMemoryBarrierCall4 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall4>(taken[4]);
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
      CuteQt3DRender_QMemoryBarrierCall5 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall5>(taken[5]);
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
      CuteQt3DRender_QMemoryBarrierCall6 call = reinterpret_cast<CuteQt3DRender_QMemoryBarrierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QMemoryBarrier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QMemoryBarrier10metaObjectEv(
    const Qt3DRender::QMemoryBarrier *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QMemoryBarrier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender14QMemoryBarrier11qt_metacastEPKc(
    Qt3DRender::QMemoryBarrier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QMemoryBarrier::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender14QMemoryBarrier11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QMemoryBarrier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QMemoryBarrier::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QMemoryBarrier2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QMemoryBarrier::tr(s, c, n));
}

//  Qt3DRender::QMemoryBarrier::QMemoryBarrier(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMemoryBarrier *ritual_ZN10Qt3DRender14QMemoryBarrierC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMemoryBarrier(parent);
}

//  Qt3DRender::QMemoryBarrier::~QMemoryBarrier()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QMemoryBarrierD1Ev(
    Qt3DRender::QMemoryBarrier *self) {
  delete self;
}

//  Operations Qt3DRender::QMemoryBarrier::waitOperations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender14QMemoryBarrier14waitOperationsEv(
    const Qt3DRender::QMemoryBarrier *self) {
  return static_cast<int>(self->waitOperations().toInt());
}

//  void
//      Qt3DRender::QMemoryBarrier::setWaitOperations(QMemoryBarrier::Operati
//      ons operations)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QMemoryBarrier17setWaitOperationsE6QFlagsINS0_9OperationEE(
    Qt3DRender::QMemoryBarrier *self,
    int operations) {
  self->setWaitOperations(
      QFlags<Qt3DRender::QMemoryBarrier::Operation>::fromInt(operations));
}

//  void Qt3DRender::QMemoryBarrier::waitOperationsChanged(QMemoryBarrier::Op
//      erations barrierTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender14QMemoryBarrier21waitOperationsChangedE6QFlagsINS0_9OperationEE(
    Qt3DRender::QMemoryBarrier *self,
    int barrierTypes) {
  self->waitOperationsChanged(
      QFlags<Qt3DRender::QMemoryBarrier::Operation>::fromInt(barrierTypes));
}

//  Qt3DRender::QMemoryBarrier::QMemoryBarrier(QMemoryBarrierPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMemoryBarrier *ritual_ZN10Qt3DRender14QMemoryBarrierC1ERNS_21QMemoryBarrierPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QMemoryBarrierPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMemoryBarrier(*dd, parent);
}

//  QMemoryBarrierPrivate *Qt3DRender::QMemoryBarrier::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMemoryBarrierPrivate *ritual_ZN10Qt3DRender14QMemoryBarrier6d_funcEv(
    Qt3DRender::QMemoryBarrier *self) {
  return self->d_func();
}

//  const QMemoryBarrierPrivate *Qt3DRender::QMemoryBarrier::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QMemoryBarrierPrivate *ritual_ZNK10Qt3DRender14QMemoryBarrier6d_funcEv(
    const Qt3DRender::QMemoryBarrier *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QMemoryBarrier, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QMemoryBarrier(
    Qt3DRender::QMemoryBarrier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QMemoryBarrier *>(self)->take(key, call);
}
