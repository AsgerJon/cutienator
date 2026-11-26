//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qlayer.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qlayer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QLayer that Python can take functions over in. Every Qt3DRender::QLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLayerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLayerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QLayer : public Qt3DRender::QLayer {
public:
  using Qt3DRender::QLayer::QLayer;
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
      CuteQt3DRender_QLayerCall0 call = reinterpret_cast<CuteQt3DRender_QLayerCall0>(taken[0]);
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
      CuteQt3DRender_QLayerCall1 call = reinterpret_cast<CuteQt3DRender_QLayerCall1>(taken[1]);
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
      CuteQt3DRender_QLayerCall2 call = reinterpret_cast<CuteQt3DRender_QLayerCall2>(taken[2]);
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
      CuteQt3DRender_QLayerCall3 call = reinterpret_cast<CuteQt3DRender_QLayerCall3>(taken[3]);
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
      CuteQt3DRender_QLayerCall4 call = reinterpret_cast<CuteQt3DRender_QLayerCall4>(taken[4]);
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
      CuteQt3DRender_QLayerCall5 call = reinterpret_cast<CuteQt3DRender_QLayerCall5>(taken[5]);
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
      CuteQt3DRender_QLayerCall6 call = reinterpret_cast<CuteQt3DRender_QLayerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6QLayer10metaObjectEv(
    const Qt3DRender::QLayer *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QLayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6QLayer11qt_metacastEPKc(
    Qt3DRender::QLayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QLayer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6QLayer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QLayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QLayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6QLayer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QLayer::tr(s, c, n));
}

//  Qt3DRender::QLayer::QLayer(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayer *ritual_ZN10Qt3DRender6QLayerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLayer(parent);
}

//  Qt3DRender::QLayer::~QLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6QLayerD1Ev(Qt3DRender::QLayer *self) {
  delete self;
}

//  bool Qt3DRender::QLayer::recursive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6QLayer9recursiveEv(
    const Qt3DRender::QLayer *self) {
  return self->recursive();
}

//  void Qt3DRender::QLayer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6QLayer12setRecursiveEb(
    Qt3DRender::QLayer *self,
    bool recursive) {
  self->setRecursive(recursive);
}

//  void Qt3DRender::QLayer::recursiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6QLayer16recursiveChangedEv(
    Qt3DRender::QLayer *self) {
  self->recursiveChanged();
}

//  Qt3DRender::QLayer::QLayer(QLayerPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayer *ritual_ZN10Qt3DRender6QLayerC1ERNS_13QLayerPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QLayerPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLayer(*dd, parent);
}

//  QLayerPrivate *Qt3DRender::QLayer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerPrivate *ritual_ZN10Qt3DRender6QLayer6d_funcEv(
    Qt3DRender::QLayer *self) {
  return self->d_func();
}

//  const QLayerPrivate *Qt3DRender::QLayer::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QLayerPrivate *ritual_ZNK10Qt3DRender6QLayer6d_funcEv(
    const Qt3DRender::QLayer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QLayer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QLayer(
    Qt3DRender::QLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QLayer *>(self)->take(key, call);
}
