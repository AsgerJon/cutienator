//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qstencilmask.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qstencilmask.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QStencilMask that Python can take functions over in. Every Qt3DRender::QStencilMask
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilMaskCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilMaskCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilMaskCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilMaskCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilMaskCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilMaskCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilMaskCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QStencilMask : public Qt3DRender::QStencilMask {
public:
  using Qt3DRender::QStencilMask::QStencilMask;
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
      CuteQt3DRender_QStencilMaskCall0 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall0>(taken[0]);
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
      CuteQt3DRender_QStencilMaskCall1 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall1>(taken[1]);
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
      CuteQt3DRender_QStencilMaskCall2 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall2>(taken[2]);
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
      CuteQt3DRender_QStencilMaskCall3 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall3>(taken[3]);
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
      CuteQt3DRender_QStencilMaskCall4 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall4>(taken[4]);
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
      CuteQt3DRender_QStencilMaskCall5 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall5>(taken[5]);
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
      CuteQt3DRender_QStencilMaskCall6 call = reinterpret_cast<CuteQt3DRender_QStencilMaskCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QStencilMask::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender12QStencilMask10metaObjectEv(
    const Qt3DRender::QStencilMask *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QStencilMask::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender12QStencilMask11qt_metacastEPKc(
    Qt3DRender::QStencilMask *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QStencilMask::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender12QStencilMask11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QStencilMask *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QStencilMask::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender12QStencilMask2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QStencilMask::tr(s, c, n));
}

//  Qt3DRender::QStencilMask::QStencilMask(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilMask *ritual_ZN10Qt3DRender12QStencilMaskC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QStencilMask(parent);
}

//  Qt3DRender::QStencilMask::~QStencilMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QStencilMaskD1Ev(
    Qt3DRender::QStencilMask *self) {
  delete self;
}

//  uint Qt3DRender::QStencilMask::frontOutputMask() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender12QStencilMask15frontOutputMaskEv(
    const Qt3DRender::QStencilMask *self) {
  return self->frontOutputMask();
}

//  uint Qt3DRender::QStencilMask::backOutputMask() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender12QStencilMask14backOutputMaskEv(
    const Qt3DRender::QStencilMask *self) {
  return self->backOutputMask();
}

//  void Qt3DRender::QStencilMask::setFrontOutputMask(uint frontOutputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QStencilMask18setFrontOutputMaskEj(
    Qt3DRender::QStencilMask *self,
    uint frontOutputMask) {
  self->setFrontOutputMask(frontOutputMask);
}

//  void Qt3DRender::QStencilMask::setBackOutputMask(uint backOutputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QStencilMask17setBackOutputMaskEj(
    Qt3DRender::QStencilMask *self,
    uint backOutputMask) {
  self->setBackOutputMask(backOutputMask);
}

//  void Qt3DRender::QStencilMask::frontOutputMaskChanged(uint
//      frontOutputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QStencilMask22frontOutputMaskChangedEj(
    Qt3DRender::QStencilMask *self,
    uint frontOutputMask) {
  self->frontOutputMaskChanged(frontOutputMask);
}

//  void Qt3DRender::QStencilMask::backOutputMaskChanged(uint backOutputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QStencilMask21backOutputMaskChangedEj(
    Qt3DRender::QStencilMask *self,
    uint backOutputMask) {
  self->backOutputMaskChanged(backOutputMask);
}

//  QStencilMaskPrivate *Qt3DRender::QStencilMask::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilMaskPrivate *ritual_ZN10Qt3DRender12QStencilMask6d_funcEv(
    Qt3DRender::QStencilMask *self) {
  return self->d_func();
}

//  const QStencilMaskPrivate *Qt3DRender::QStencilMask::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QStencilMaskPrivate *ritual_ZNK10Qt3DRender12QStencilMask6d_funcEv(
    const Qt3DRender::QStencilMask *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QStencilMask, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QStencilMask(
    Qt3DRender::QStencilMask *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QStencilMask *>(self)->take(key, call);
}
