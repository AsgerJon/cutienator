//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrenderaspect.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrenderaspect.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRenderAspect that Python can take functions over in. Every Qt3DRender::QRenderAspect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderAspectCall0)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectCall1)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectCall2)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectCall3)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectCall4)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderAspectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderAspectCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderAspectCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderAspectCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderAspectCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderAspectCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderAspectCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderAspect : public Qt3DRender::QRenderAspect {
public:
  using Qt3DRender::QRenderAspect::QRenderAspect;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect12onRegisteredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect14onUnregisteredEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect15onEngineStartupEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect16onEngineShutdownEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect8jobsDoneEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore15QAbstractAspect9frameDoneEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Qt3DRender::QRenderAspect::onRegistered()
  void onRegistered() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall0 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspect::onRegistered();
  }

  //  void Qt3DRender::QRenderAspect::onUnregistered()
  void onUnregistered() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall1 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspect::onUnregistered();
  }

  //  void Qt3DRender::QRenderAspect::onEngineStartup()
  void onEngineStartup() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall2 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspect::onEngineStartup();
  }

  //  void Qt3DCore::QAbstractAspect::onEngineShutdown()
  void onEngineShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall3 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::onEngineShutdown();
  }

  //  void Qt3DCore::QAbstractAspect::jobsDone()
  void jobsDone() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall4 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspect::frameDone()
  void frameDone() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall5 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspect::frameDone();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall6 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall7 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall8 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall9 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall10 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall11 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectCall12 call = reinterpret_cast<CuteQt3DRender_QRenderAspectCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderAspect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QRenderAspect10metaObjectEv(
    const Qt3DRender::QRenderAspect *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QRenderAspect::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QRenderAspect2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderAspect::tr(s, c, n));
}

//  QRenderAspectPrivate *Qt3DRender::QRenderAspect::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspectPrivate *ritual_ZN10Qt3DRender13QRenderAspect6d_funcEv(
    Qt3DRender::QRenderAspect *self) {
  return self->d_func();
}

//  const QRenderAspectPrivate *Qt3DRender::QRenderAspect::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderAspectPrivate *ritual_ZNK10Qt3DRender13QRenderAspect6d_funcEv(
    const Qt3DRender::QRenderAspect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderAspect, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderAspect(
    Qt3DRender::QRenderAspect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderAspect *>(self)->take(key, call);
}

//  void Qt3DRender::QRenderAspect::onRegistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender13QRenderAspect12onRegisteredEv(
    Qt3DRender::QRenderAspect *self) {
  self->Qt3DRender::QRenderAspect::onRegistered();
}

//  void Qt3DRender::QRenderAspect::onUnregistered()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender13QRenderAspect14onUnregisteredEv(
    Qt3DRender::QRenderAspect *self) {
  self->Qt3DRender::QRenderAspect::onUnregistered();
}

//  void Qt3DRender::QRenderAspect::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender13QRenderAspect15onEngineStartupEv(
    Qt3DRender::QRenderAspect *self) {
  self->Qt3DRender::QRenderAspect::onEngineStartup();
}
