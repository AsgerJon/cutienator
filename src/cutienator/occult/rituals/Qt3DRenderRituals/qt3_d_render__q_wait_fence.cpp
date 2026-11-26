//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qwaitfence.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qwaitfence.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QWaitFence that Python can take functions over in. Every Qt3DRender::QWaitFence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QWaitFenceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QWaitFenceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QWaitFenceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QWaitFenceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QWaitFenceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QWaitFenceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QWaitFenceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QWaitFence : public Qt3DRender::QWaitFence {
public:
  using Qt3DRender::QWaitFence::QWaitFence;
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
      CuteQt3DRender_QWaitFenceCall0 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall0>(taken[0]);
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
      CuteQt3DRender_QWaitFenceCall1 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall1>(taken[1]);
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
      CuteQt3DRender_QWaitFenceCall2 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall2>(taken[2]);
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
      CuteQt3DRender_QWaitFenceCall3 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall3>(taken[3]);
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
      CuteQt3DRender_QWaitFenceCall4 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall4>(taken[4]);
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
      CuteQt3DRender_QWaitFenceCall5 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall5>(taken[5]);
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
      CuteQt3DRender_QWaitFenceCall6 call = reinterpret_cast<CuteQt3DRender_QWaitFenceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QWaitFence::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QWaitFence10metaObjectEv(
    const Qt3DRender::QWaitFence *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QWaitFence::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QWaitFence11qt_metacastEPKc(
    Qt3DRender::QWaitFence *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QWaitFence::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QWaitFence11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QWaitFence *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QWaitFence::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QWaitFence2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QWaitFence::tr(s, c, n));
}

//  Qt3DRender::QWaitFence::QWaitFence(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QWaitFence *ritual_ZN10Qt3DRender10QWaitFenceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QWaitFence(parent);
}

//  Qt3DRender::QWaitFence::~QWaitFence()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFenceD1Ev(Qt3DRender::QWaitFence *self) {
  delete self;
}

//  void Qt3DRender::QWaitFence::setHandleType(HandleType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence13setHandleTypeENS0_10HandleTypeE(
    Qt3DRender::QWaitFence *self,
    Qt3DRender::QWaitFence::HandleType type) {
  self->setHandleType(type);
}

//  void Qt3DRender::QWaitFence::setHandle(QVariant handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence9setHandleE8QVariant(
    Qt3DRender::QWaitFence *self,
    const QVariant *handle) {
  self->setHandle(*handle);
}

//  HandleType Qt3DRender::QWaitFence::handleType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QWaitFence::HandleType ritual_ZNK10Qt3DRender10QWaitFence10handleTypeEv(
    const Qt3DRender::QWaitFence *self) {
  return self->handleType();
}

//  QVariant Qt3DRender::QWaitFence::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender10QWaitFence6handleEv(
    const Qt3DRender::QWaitFence *self) {
  return new QVariant(self->handle());
}

//  bool Qt3DRender::QWaitFence::waitOnCPU() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QWaitFence9waitOnCPUEv(
    const Qt3DRender::QWaitFence *self) {
  return self->waitOnCPU();
}

//  void Qt3DRender::QWaitFence::setWaitOnCPU(bool waitOnCPU)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence12setWaitOnCPUEb(
    Qt3DRender::QWaitFence *self,
    bool waitOnCPU) {
  self->setWaitOnCPU(waitOnCPU);
}

//  quint64 Qt3DRender::QWaitFence::timeout() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK10Qt3DRender10QWaitFence7timeoutEv(
    const Qt3DRender::QWaitFence *self) {
  return self->timeout();
}

//  void Qt3DRender::QWaitFence::setTimeout(quint64 timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence10setTimeoutEy(
    Qt3DRender::QWaitFence *self,
    quint64 timeout) {
  self->setTimeout(timeout);
}

//  void Qt3DRender::QWaitFence::waitOnCPUChanged(bool waitOnCPU)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence16waitOnCPUChangedEb(
    Qt3DRender::QWaitFence *self,
    bool waitOnCPU) {
  self->waitOnCPUChanged(waitOnCPU);
}

//  void Qt3DRender::QWaitFence::timeoutChanged(quint64 timeoutChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence14timeoutChangedEy(
    Qt3DRender::QWaitFence *self,
    quint64 timeoutChanged) {
  self->timeoutChanged(timeoutChanged);
}

//  void Qt3DRender::QWaitFence::handleTypeChanged(HandleType handleType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence17handleTypeChangedENS0_10HandleTypeE(
    Qt3DRender::QWaitFence *self,
    Qt3DRender::QWaitFence::HandleType handleType) {
  self->handleTypeChanged(handleType);
}

//  void Qt3DRender::QWaitFence::handleChanged(QVariant handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QWaitFence13handleChangedE8QVariant(
    Qt3DRender::QWaitFence *self,
    const QVariant *handle) {
  self->handleChanged(*handle);
}

//  Qt3DRender::QWaitFence::QWaitFence(QWaitFencePrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QWaitFence *ritual_ZN10Qt3DRender10QWaitFenceC1ERNS_17QWaitFencePrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QWaitFencePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QWaitFence(*dd, parent);
}

//  QWaitFencePrivate *Qt3DRender::QWaitFence::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QWaitFencePrivate *ritual_ZN10Qt3DRender10QWaitFence6d_funcEv(
    Qt3DRender::QWaitFence *self) {
  return self->d_func();
}

//  const QWaitFencePrivate *Qt3DRender::QWaitFence::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QWaitFencePrivate *ritual_ZNK10Qt3DRender10QWaitFence6d_funcEv(
    const Qt3DRender::QWaitFence *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QWaitFence, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QWaitFence(
    Qt3DRender::QWaitFence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QWaitFence *>(self)->take(key, call);
}
