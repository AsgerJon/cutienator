//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendersettings.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendersettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRenderSettings that Python can take functions over in. Every Qt3DRender::QRenderSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderSettingsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderSettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderSettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderSettings : public Qt3DRender::QRenderSettings {
public:
  using Qt3DRender::QRenderSettings::QRenderSettings;
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
      CuteQt3DRender_QRenderSettingsCall0 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall0>(taken[0]);
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
      CuteQt3DRender_QRenderSettingsCall1 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall1>(taken[1]);
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
      CuteQt3DRender_QRenderSettingsCall2 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall2>(taken[2]);
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
      CuteQt3DRender_QRenderSettingsCall3 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall3>(taken[3]);
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
      CuteQt3DRender_QRenderSettingsCall4 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall4>(taken[4]);
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
      CuteQt3DRender_QRenderSettingsCall5 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall5>(taken[5]);
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
      CuteQt3DRender_QRenderSettingsCall6 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender15QRenderSettings10metaObjectEv(
    const Qt3DRender::QRenderSettings *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderSettings::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender15QRenderSettings11qt_metacastEPKc(
    Qt3DRender::QRenderSettings *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderSettings::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender15QRenderSettings11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderSettings *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderSettings::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender15QRenderSettings2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderSettings::tr(s, c, n));
}

//  Qt3DRender::QRenderSettings::QRenderSettings(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettings *ritual_ZN10Qt3DRender15QRenderSettingsC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderSettings(parent);
}

//  Qt3DRender::QRenderSettings::~QRenderSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QRenderSettingsD1Ev(
    Qt3DRender::QRenderSettings *self) {
  delete self;
}

//  QRenderCapabilities *Qt3DRender::QRenderSettings::renderCapabilities()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilities *ritual_ZN10Qt3DRender15QRenderSettings18renderCapabilitiesEv(
    Qt3DRender::QRenderSettings *self) {
  return self->renderCapabilities();
}

//  QPickingSettings *Qt3DRender::QRenderSettings::pickingSettings()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingSettings *ritual_ZN10Qt3DRender15QRenderSettings15pickingSettingsEv(
    Qt3DRender::QRenderSettings *self) {
  return self->pickingSettings();
}

//  QFrameGraphNode *Qt3DRender::QRenderSettings::activeFrameGraph() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QFrameGraphNode *ritual_ZNK10Qt3DRender15QRenderSettings16activeFrameGraphEv(
    const Qt3DRender::QRenderSettings *self) {
  return self->activeFrameGraph();
}

//  RenderPolicy Qt3DRender::QRenderSettings::renderPolicy() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettings::RenderPolicy ritual_ZNK10Qt3DRender15QRenderSettings12renderPolicyEv(
    const Qt3DRender::QRenderSettings *self) {
  return self->renderPolicy();
}

//  void Qt3DRender::QRenderSettings::setActiveFrameGraph(QFrameGraphNode
//      *activeFrameGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QRenderSettings19setActiveFrameGraphEPNS_15QFrameGraphNodeE(
    Qt3DRender::QRenderSettings *self,
    Qt3DRender::QFrameGraphNode *activeFrameGraph) {
  self->setActiveFrameGraph(activeFrameGraph);
}

//  void Qt3DRender::QRenderSettings::setRenderPolicy(RenderPolicy
//      renderPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QRenderSettings15setRenderPolicyENS0_12RenderPolicyE(
    Qt3DRender::QRenderSettings *self,
    Qt3DRender::QRenderSettings::RenderPolicy renderPolicy) {
  self->setRenderPolicy(renderPolicy);
}

//  void Qt3DRender::QRenderSettings::activeFrameGraphChanged(QFrameGraphNode
//      *activeFrameGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QRenderSettings23activeFrameGraphChangedEPNS_15QFrameGraphNodeE(
    Qt3DRender::QRenderSettings *self,
    Qt3DRender::QFrameGraphNode *activeFrameGraph) {
  self->activeFrameGraphChanged(activeFrameGraph);
}

//  void Qt3DRender::QRenderSettings::renderPolicyChanged(RenderPolicy
//      renderPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15QRenderSettings19renderPolicyChangedENS0_12RenderPolicyE(
    Qt3DRender::QRenderSettings *self,
    Qt3DRender::QRenderSettings::RenderPolicy renderPolicy) {
  self->renderPolicyChanged(renderPolicy);
}

//  QRenderSettingsPrivate *Qt3DRender::QRenderSettings::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettingsPrivate *ritual_ZN10Qt3DRender15QRenderSettings6d_funcEv(
    Qt3DRender::QRenderSettings *self) {
  return self->d_func();
}

//  const QRenderSettingsPrivate *Qt3DRender::QRenderSettings::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderSettingsPrivate *ritual_ZNK10Qt3DRender15QRenderSettings6d_funcEv(
    const Qt3DRender::QRenderSettings *self) {
  return self->d_func();
}

//  Qt3DRender::QRenderSettings::QRenderSettings(QRenderSettingsPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettings *ritual_ZN10Qt3DRender15QRenderSettingsC1ERNS_22QRenderSettingsPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderSettingsPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderSettings(*dd, parent);
}

//  a Python function taken by a CuteQt3DRender_QRenderSettings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderSettings(
    Qt3DRender::QRenderSettings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderSettings *>(self)->take(key, call);
}
