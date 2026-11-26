//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qdispatchcompute.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qdispatchcompute.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QDispatchCompute that Python can take functions over in. Every Qt3DRender::QDispatchCompute
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QDispatchComputeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QDispatchComputeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDispatchComputeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDispatchComputeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDispatchComputeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDispatchComputeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDispatchComputeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QDispatchCompute : public Qt3DRender::QDispatchCompute {
public:
  using Qt3DRender::QDispatchCompute::QDispatchCompute;
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
      CuteQt3DRender_QDispatchComputeCall0 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall0>(taken[0]);
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
      CuteQt3DRender_QDispatchComputeCall1 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall1>(taken[1]);
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
      CuteQt3DRender_QDispatchComputeCall2 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall2>(taken[2]);
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
      CuteQt3DRender_QDispatchComputeCall3 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall3>(taken[3]);
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
      CuteQt3DRender_QDispatchComputeCall4 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall4>(taken[4]);
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
      CuteQt3DRender_QDispatchComputeCall5 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall5>(taken[5]);
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
      CuteQt3DRender_QDispatchComputeCall6 call = reinterpret_cast<CuteQt3DRender_QDispatchComputeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QDispatchCompute::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender16QDispatchCompute10metaObjectEv(
    const Qt3DRender::QDispatchCompute *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QDispatchCompute::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender16QDispatchCompute11qt_metacastEPKc(
    Qt3DRender::QDispatchCompute *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QDispatchCompute::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender16QDispatchCompute11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QDispatchCompute *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QDispatchCompute::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender16QDispatchCompute2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QDispatchCompute::tr(s, c, n));
}

//  Qt3DRender::QDispatchCompute::QDispatchCompute(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QDispatchCompute *ritual_ZN10Qt3DRender16QDispatchComputeC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QDispatchCompute(parent);
}

//  Qt3DRender::QDispatchCompute::~QDispatchCompute()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchComputeD1Ev(
    Qt3DRender::QDispatchCompute *self) {
  delete self;
}

//  int Qt3DRender::QDispatchCompute::workGroupX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupXEv(
    const Qt3DRender::QDispatchCompute *self) {
  return self->workGroupX();
}

//  int Qt3DRender::QDispatchCompute::workGroupY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupYEv(
    const Qt3DRender::QDispatchCompute *self) {
  return self->workGroupY();
}

//  int Qt3DRender::QDispatchCompute::workGroupZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupZEv(
    const Qt3DRender::QDispatchCompute *self) {
  return self->workGroupZ();
}

//  void Qt3DRender::QDispatchCompute::setWorkGroupX(int workGroupX)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupXEi(
    Qt3DRender::QDispatchCompute *self,
    int workGroupX) {
  self->setWorkGroupX(workGroupX);
}

//  void Qt3DRender::QDispatchCompute::setWorkGroupY(int workGroupY)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupYEi(
    Qt3DRender::QDispatchCompute *self,
    int workGroupY) {
  self->setWorkGroupY(workGroupY);
}

//  void Qt3DRender::QDispatchCompute::setWorkGroupZ(int workGroupZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupZEi(
    Qt3DRender::QDispatchCompute *self,
    int workGroupZ) {
  self->setWorkGroupZ(workGroupZ);
}

//  void Qt3DRender::QDispatchCompute::workGroupXChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute17workGroupXChangedEv(
    Qt3DRender::QDispatchCompute *self) {
  self->workGroupXChanged();
}

//  void Qt3DRender::QDispatchCompute::workGroupYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute17workGroupYChangedEv(
    Qt3DRender::QDispatchCompute *self) {
  self->workGroupYChanged();
}

//  void Qt3DRender::QDispatchCompute::workGroupZChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QDispatchCompute17workGroupZChangedEv(
    Qt3DRender::QDispatchCompute *self) {
  self->workGroupZChanged();
}

//  QDispatchComputePrivate *Qt3DRender::QDispatchCompute::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QDispatchComputePrivate *ritual_ZN10Qt3DRender16QDispatchCompute6d_funcEv(
    Qt3DRender::QDispatchCompute *self) {
  return self->d_func();
}

//  const QDispatchComputePrivate *Qt3DRender::QDispatchCompute::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QDispatchComputePrivate *ritual_ZNK10Qt3DRender16QDispatchCompute6d_funcEv(
    const Qt3DRender::QDispatchCompute *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QDispatchCompute, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QDispatchCompute(
    Qt3DRender::QDispatchCompute *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QDispatchCompute *>(self)->take(key, call);
}
