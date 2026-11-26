//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendercapabilities.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendercapabilities.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DRender::QRenderCapabilities that Python can take functions over in. Every Qt3DRender::QRenderCapabilities
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderCapabilitiesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderCapabilitiesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderCapabilitiesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderCapabilitiesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderCapabilitiesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderCapabilitiesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderCapabilitiesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderCapabilities : public Qt3DRender::QRenderCapabilities {
public:
  using Qt3DRender::QRenderCapabilities::QRenderCapabilities;
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
      CuteQt3DRender_QRenderCapabilitiesCall0 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall0>(taken[0]);
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
      CuteQt3DRender_QRenderCapabilitiesCall1 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall1>(taken[1]);
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
      CuteQt3DRender_QRenderCapabilitiesCall2 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall2>(taken[2]);
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
      CuteQt3DRender_QRenderCapabilitiesCall3 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall3>(taken[3]);
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
      CuteQt3DRender_QRenderCapabilitiesCall4 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall4>(taken[4]);
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
      CuteQt3DRender_QRenderCapabilitiesCall5 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall5>(taken[5]);
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
      CuteQt3DRender_QRenderCapabilitiesCall6 call = reinterpret_cast<CuteQt3DRender_QRenderCapabilitiesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderCapabilities::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender19QRenderCapabilities10metaObjectEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderCapabilities::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender19QRenderCapabilities11qt_metacastEPKc(
    Qt3DRender::QRenderCapabilities *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderCapabilities::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender19QRenderCapabilities11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderCapabilities *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderCapabilities::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender19QRenderCapabilities2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderCapabilities::tr(s, c, n));
}

//  Qt3DRender::QRenderCapabilities::QRenderCapabilities(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilities *ritual_ZN10Qt3DRender19QRenderCapabilitiesC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_QRenderCapabilities(parent);
}

//  Qt3DRender::QRenderCapabilities::~QRenderCapabilities()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderCapabilitiesD1Ev(
    Qt3DRender::QRenderCapabilities *self) {
  delete self;
}

//  bool Qt3DRender::QRenderCapabilities::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCapabilities7isValidEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->isValid();
}

//  API Qt3DRender::QRenderCapabilities::api() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilities::API ritual_ZNK10Qt3DRender19QRenderCapabilities3apiEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->api();
}

//  Profile Qt3DRender::QRenderCapabilities::profile() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilities::Profile ritual_ZNK10Qt3DRender19QRenderCapabilities7profileEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->profile();
}

//  int Qt3DRender::QRenderCapabilities::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities12majorVersionEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->majorVersion();
}

//  int Qt3DRender::QRenderCapabilities::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities12minorVersionEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->minorVersion();
}

//  QStringList Qt3DRender::QRenderCapabilities::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender19QRenderCapabilities10extensionsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return new QList<QString>(self->extensions());
}

//  QString Qt3DRender::QRenderCapabilities::vendor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender19QRenderCapabilities6vendorEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return new QString(self->vendor());
}

//  QString Qt3DRender::QRenderCapabilities::renderer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender19QRenderCapabilities8rendererEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return new QString(self->renderer());
}

//  QString Qt3DRender::QRenderCapabilities::driverVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender19QRenderCapabilities13driverVersionEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return new QString(self->driverVersion());
}

//  QString Qt3DRender::QRenderCapabilities::glslVersion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender19QRenderCapabilities11glslVersionEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return new QString(self->glslVersion());
}

//  int Qt3DRender::QRenderCapabilities::maxSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities10maxSamplesEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxSamples();
}

//  int Qt3DRender::QRenderCapabilities::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities14maxTextureSizeEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxTextureSize();
}

//  int Qt3DRender::QRenderCapabilities::maxTextureUnits() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities15maxTextureUnitsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxTextureUnits();
}

//  int Qt3DRender::QRenderCapabilities::maxTextureLayers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities16maxTextureLayersEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxTextureLayers();
}

//  bool Qt3DRender::QRenderCapabilities::supportsUBO() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCapabilities11supportsUBOEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->supportsUBO();
}

//  int Qt3DRender::QRenderCapabilities::maxUBOSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities10maxUBOSizeEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxUBOSize();
}

//  int Qt3DRender::QRenderCapabilities::maxUBOBindings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities14maxUBOBindingsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxUBOBindings();
}

//  bool Qt3DRender::QRenderCapabilities::supportsSSBO() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCapabilities12supportsSSBOEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->supportsSSBO();
}

//  int Qt3DRender::QRenderCapabilities::maxSSBOSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities11maxSSBOSizeEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxSSBOSize();
}

//  int Qt3DRender::QRenderCapabilities::maxSSBOBindings() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities15maxSSBOBindingsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxSSBOBindings();
}

//  bool Qt3DRender::QRenderCapabilities::supportsImageStore() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCapabilities18supportsImageStoreEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->supportsImageStore();
}

//  int Qt3DRender::QRenderCapabilities::maxImageUnits() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities13maxImageUnitsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxImageUnits();
}

//  bool Qt3DRender::QRenderCapabilities::supportsCompute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCapabilities15supportsComputeEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->supportsCompute();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountXEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupCountX();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountYEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupCountY();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupCountZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities18maxWorkGroupCountZEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupCountZ();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeXEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupSizeX();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeYEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupSizeY();
}

//  int Qt3DRender::QRenderCapabilities::maxWorkGroupSizeZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities17maxWorkGroupSizeZEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxWorkGroupSizeZ();
}

//  int Qt3DRender::QRenderCapabilities::maxComputeInvocations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities21maxComputeInvocationsEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxComputeInvocations();
}

//  int Qt3DRender::QRenderCapabilities::maxComputeSharedMemorySize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCapabilities26maxComputeSharedMemorySizeEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->maxComputeSharedMemorySize();
}

//  QRenderCapabilitiesPrivate *Qt3DRender::QRenderCapabilities::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapabilitiesPrivate *ritual_ZN10Qt3DRender19QRenderCapabilities6d_funcEv(
    Qt3DRender::QRenderCapabilities *self) {
  return self->d_func();
}

//  const QRenderCapabilitiesPrivate
//      *Qt3DRender::QRenderCapabilities::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCapabilitiesPrivate *ritual_ZNK10Qt3DRender19QRenderCapabilities6d_funcEv(
    const Qt3DRender::QRenderCapabilities *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderCapabilities, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderCapabilities(
    Qt3DRender::QRenderCapabilities *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderCapabilities *>(self)->take(key, call);
}
