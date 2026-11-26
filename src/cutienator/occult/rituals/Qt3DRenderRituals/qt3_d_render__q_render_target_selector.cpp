//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendertargetselector.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qrendertargetselector.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRenderTargetSelector that Python can take functions over in. Every Qt3DRender::QRenderTargetSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetSelectorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetSelectorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetSelectorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetSelectorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetSelectorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetSelectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetSelectorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderTargetSelector : public Qt3DRender::QRenderTargetSelector {
public:
  using Qt3DRender::QRenderTargetSelector::QRenderTargetSelector;
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
      CuteQt3DRender_QRenderTargetSelectorCall0 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall0>(taken[0]);
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
      CuteQt3DRender_QRenderTargetSelectorCall1 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall1>(taken[1]);
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
      CuteQt3DRender_QRenderTargetSelectorCall2 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall2>(taken[2]);
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
      CuteQt3DRender_QRenderTargetSelectorCall3 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall3>(taken[3]);
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
      CuteQt3DRender_QRenderTargetSelectorCall4 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall4>(taken[4]);
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
      CuteQt3DRender_QRenderTargetSelectorCall5 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall5>(taken[5]);
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
      CuteQt3DRender_QRenderTargetSelectorCall6 call = reinterpret_cast<CuteQt3DRender_QRenderTargetSelectorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderTargetSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender21QRenderTargetSelector10metaObjectEv(
    const Qt3DRender::QRenderTargetSelector *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderTargetSelector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender21QRenderTargetSelector11qt_metacastEPKc(
    Qt3DRender::QRenderTargetSelector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderTargetSelector::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender21QRenderTargetSelector11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderTargetSelector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderTargetSelector::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender21QRenderTargetSelector2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderTargetSelector::tr(s, c, n));
}

//  Qt3DRender::QRenderTargetSelector::QRenderTargetSelector(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetSelector *ritual_ZN10Qt3DRender21QRenderTargetSelectorC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTargetSelector(parent);
}

//  Qt3DRender::QRenderTargetSelector::~QRenderTargetSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderTargetSelectorD1Ev(
    Qt3DRender::QRenderTargetSelector *self) {
  delete self;
}

//  QRenderTarget *Qt3DRender::QRenderTargetSelector::target() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTarget *ritual_ZNK10Qt3DRender21QRenderTargetSelector6targetEv(
    const Qt3DRender::QRenderTargetSelector *self) {
  return self->target();
}

//  void Qt3DRender::QRenderTargetSelector::setTarget(QRenderTarget *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderTargetSelector9setTargetEPNS_13QRenderTargetE(
    Qt3DRender::QRenderTargetSelector *self,
    Qt3DRender::QRenderTarget *target) {
  self->setTarget(target);
}

//  void Qt3DRender::QRenderTargetSelector::targetChanged(QRenderTarget
//      *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QRenderTargetSelector13targetChangedEPNS_13QRenderTargetE(
    Qt3DRender::QRenderTargetSelector *self,
    Qt3DRender::QRenderTarget *target) {
  self->targetChanged(target);
}

//  Qt3DRender::QRenderTargetSelector::QRenderTargetSelector(QRenderTargetSel
//      ectorPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetSelector *ritual_ZN10Qt3DRender21QRenderTargetSelectorC1ERNS_28QRenderTargetSelectorPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderTargetSelectorPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTargetSelector(*dd, parent);
}

//  QRenderTargetSelectorPrivate *Qt3DRender::QRenderTargetSelector::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetSelectorPrivate *ritual_ZN10Qt3DRender21QRenderTargetSelector6d_funcEv(
    Qt3DRender::QRenderTargetSelector *self) {
  return self->d_func();
}

//  const QRenderTargetSelectorPrivate
//      *Qt3DRender::QRenderTargetSelector::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderTargetSelectorPrivate *ritual_ZNK10Qt3DRender21QRenderTargetSelector6d_funcEv(
    const Qt3DRender::QRenderTargetSelector *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderTargetSelector, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderTargetSelector(
    Qt3DRender::QRenderTargetSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderTargetSelector *>(self)->take(key, call);
}
