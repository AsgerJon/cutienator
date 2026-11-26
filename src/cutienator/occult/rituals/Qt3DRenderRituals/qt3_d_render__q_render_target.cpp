//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendertarget.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendertarget.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QRenderTarget that Python can take functions over in. Every Qt3DRender::QRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderTarget : public Qt3DRender::QRenderTarget {
public:
  using Qt3DRender::QRenderTarget::QRenderTarget;
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
      CuteQt3DRender_QRenderTargetCall0 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall0>(taken[0]);
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
      CuteQt3DRender_QRenderTargetCall1 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall1>(taken[1]);
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
      CuteQt3DRender_QRenderTargetCall2 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall2>(taken[2]);
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
      CuteQt3DRender_QRenderTargetCall3 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall3>(taken[3]);
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
      CuteQt3DRender_QRenderTargetCall4 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall4>(taken[4]);
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
      CuteQt3DRender_QRenderTargetCall5 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall5>(taken[5]);
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
      CuteQt3DRender_QRenderTargetCall6 call = reinterpret_cast<CuteQt3DRender_QRenderTargetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderTarget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QRenderTarget10metaObjectEv(
    const Qt3DRender::QRenderTarget *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderTarget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender13QRenderTarget11qt_metacastEPKc(
    Qt3DRender::QRenderTarget *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderTarget::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender13QRenderTarget11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderTarget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderTarget::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QRenderTarget2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderTarget::tr(s, c, n));
}

//  Qt3DRender::QRenderTarget::QRenderTarget(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTarget *ritual_ZN10Qt3DRender13QRenderTargetC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTarget(parent);
}

//  Qt3DRender::QRenderTarget::~QRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QRenderTargetD1Ev(
    Qt3DRender::QRenderTarget *self) {
  delete self;
}

//  void Qt3DRender::QRenderTarget::addOutput(QRenderTargetOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QRenderTarget9addOutputEPNS_19QRenderTargetOutputE(
    Qt3DRender::QRenderTarget *self,
    Qt3DRender::QRenderTargetOutput *output) {
  self->addOutput(output);
}

//  void Qt3DRender::QRenderTarget::removeOutput(QRenderTargetOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QRenderTarget12removeOutputEPNS_19QRenderTargetOutputE(
    Qt3DRender::QRenderTarget *self,
    Qt3DRender::QRenderTargetOutput *output) {
  self->removeOutput(output);
}

//  QList<QRenderTargetOutput *> Qt3DRender::QRenderTarget::outputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QRenderTargetOutput *> *ritual_ZNK10Qt3DRender13QRenderTarget7outputsEv(
    const Qt3DRender::QRenderTarget *self) {
  return new QList<Qt3DRender::QRenderTargetOutput *>(self->outputs());
}

//  Qt3DRender::QRenderTarget::QRenderTarget(QRenderTargetPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTarget *ritual_ZN10Qt3DRender13QRenderTargetC1ERNS_20QRenderTargetPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderTargetPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTarget(*dd, parent);
}

//  QRenderTargetPrivate *Qt3DRender::QRenderTarget::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetPrivate *ritual_ZN10Qt3DRender13QRenderTarget6d_funcEv(
    Qt3DRender::QRenderTarget *self) {
  return self->d_func();
}

//  const QRenderTargetPrivate *Qt3DRender::QRenderTarget::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderTargetPrivate *ritual_ZNK10Qt3DRender13QRenderTarget6d_funcEv(
    const Qt3DRender::QRenderTarget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderTarget(
    Qt3DRender::QRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderTarget *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QRenderTargetOutput *> a ritual of
//      Qt3DRender::QRenderTarget gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRenderTarget__QList_Qt3DRender_QRenderTargetOutput(
    QList<Qt3DRender::QRenderTargetOutput *> *self) {
  delete self;
}
