//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dsceneenvironment_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dsceneenvironment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuick3DSceneEnvironment may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DSceneEnvironment : QQuick3DSceneEnvironment {
  using QQuick3DSceneEnvironment::updateSpatialNode;
  using QQuick3DSceneEnvironment::itemChange;
  using QQuick3DSceneEnvironment::useBuiltinTonemapper;
};

//  A QQuick3DSceneEnvironment that Python can take functions over in. Every QQuick3DSceneEnvironment
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DSceneEnvironmentCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DSceneEnvironmentCall1)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef bool (*CuteQQuick3DSceneEnvironmentCall2)(const void *, int *);
typedef void (*CuteQQuick3DSceneEnvironmentCall3)(const void *, int *);
typedef void (*CuteQQuick3DSceneEnvironmentCall4)(const void *, int *);
typedef void (*CuteQQuick3DSceneEnvironmentCall5)(const void *, int *);
typedef void (*CuteQQuick3DSceneEnvironmentCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSceneEnvironmentCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSceneEnvironmentCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneEnvironmentCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneEnvironmentCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneEnvironmentCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneEnvironmentCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSceneEnvironmentCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSceneEnvironment : public QQuick3DSceneEnvironment {
public:
  using QQuick3DSceneEnvironment::QQuick3DSceneEnvironment;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DSceneEnvironment::updateSpatialNode(QSSGRenderGraphObjec
  //      t *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall0 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DSceneEnvironment::updateSpatialNode(node);
  }

  //  void QQuick3DSceneEnvironment::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall1 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall1>(taken[1]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DSceneEnvironment::itemChange(a0, a1);
  }

  //  bool QQuick3DSceneEnvironment::useBuiltinTonemapper() const
  bool useBuiltinTonemapper() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall2 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DSceneEnvironment::useBuiltinTonemapper();
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall3 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall4 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall5 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall6 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall7 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall8 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall9 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall10 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall11 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall12 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DSceneEnvironmentCall13 call = reinterpret_cast<CuteQQuick3DSceneEnvironmentCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSceneEnvironment::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DSceneEnvironment10metaObjectEv(
    const QQuick3DSceneEnvironment *self) {
  return self->metaObject();
}

//  void *QQuick3DSceneEnvironment::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuick3DSceneEnvironment11qt_metacastEPKc(
    QQuick3DSceneEnvironment *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSceneEnvironment::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuick3DSceneEnvironment11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSceneEnvironment *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DSceneEnvironment::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DSceneEnvironment2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DSceneEnvironment::tr(s, c, n));
}

//  QQuick3DSceneEnvironment::QQuick3DSceneEnvironment(QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment *ritual_ZN24QQuick3DSceneEnvironmentC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new CuteQQuick3DSceneEnvironment(parent);
}

//  QQuick3DSceneEnvironment::~QQuick3DSceneEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironmentD1Ev(
    QQuick3DSceneEnvironment *self) {
  delete self;
}

//  QQuick3DEnvironmentAAModeValues
//      QQuick3DSceneEnvironment::antialiasingMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentAAModeValues ritual_ZNK24QQuick3DSceneEnvironment16antialiasingModeEv(
    const QQuick3DSceneEnvironment *self) {
  return self->antialiasingMode();
}

//  QQuick3DEnvironmentAAQualityValues
//      QQuick3DSceneEnvironment::antialiasingQuality() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentAAQualityValues ritual_ZNK24QQuick3DSceneEnvironment19antialiasingQualityEv(
    const QQuick3DSceneEnvironment *self) {
  return self->antialiasingQuality();
}

//  QQuick3DEnvironmentTemporalAAMode
//      QQuick3DSceneEnvironment::temporalAAMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentTemporalAAMode ritual_ZNK24QQuick3DSceneEnvironment14temporalAAModeEv(
    const QQuick3DSceneEnvironment *self) {
  return self->temporalAAMode();
}

//  bool QQuick3DSceneEnvironment::temporalAAEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment17temporalAAEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->temporalAAEnabled();
}

//  float QQuick3DSceneEnvironment::temporalAAStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment18temporalAAStrengthEv(
    const QQuick3DSceneEnvironment *self) {
  return self->temporalAAStrength();
}

//  QQuick3DEnvironmentBackgroundTypes
//      QQuick3DSceneEnvironment::backgroundMode() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentBackgroundTypes ritual_ZNK24QQuick3DSceneEnvironment14backgroundModeEv(
    const QQuick3DSceneEnvironment *self) {
  return self->backgroundMode();
}

//  QColor QQuick3DSceneEnvironment::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QQuick3DSceneEnvironment10clearColorEv(
    const QQuick3DSceneEnvironment *self) {
  return new QColor(self->clearColor());
}

//  float QQuick3DSceneEnvironment::aoStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment10aoStrengthEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoStrength();
}

//  float QQuick3DSceneEnvironment::aoDistance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment10aoDistanceEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoDistance();
}

//  float QQuick3DSceneEnvironment::aoSoftness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment10aoSoftnessEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoSoftness();
}

//  bool QQuick3DSceneEnvironment::aoDither() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment8aoDitherEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoDither();
}

//  int QQuick3DSceneEnvironment::aoSampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuick3DSceneEnvironment12aoSampleRateEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoSampleRate();
}

//  float QQuick3DSceneEnvironment::aoBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment6aoBiasEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoBias();
}

//  bool QQuick3DSceneEnvironment::aoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment9aoEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->aoEnabled();
}

//  void QQuick3DSceneEnvironment::setAoEnabled(bool newAoEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment12setAoEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool newAoEnabled) {
  self->setAoEnabled(newAoEnabled);
}

//  QQuick3DTexture *QQuick3DSceneEnvironment::lightProbe() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK24QQuick3DSceneEnvironment10lightProbeEv(
    const QQuick3DSceneEnvironment *self) {
  return self->lightProbe();
}

//  QQuick3DSkyMaterial *QQuick3DSceneEnvironment::skyMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DSkyMaterial *ritual_ZNK24QQuick3DSceneEnvironment11skyMaterialEv(
    const QQuick3DSceneEnvironment *self) {
  return self->skyMaterial();
}

//  float QQuick3DSceneEnvironment::probeExposure() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment13probeExposureEv(
    const QQuick3DSceneEnvironment *self) {
  return self->probeExposure();
}

//  float QQuick3DSceneEnvironment::probeHorizon() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment12probeHorizonEv(
    const QQuick3DSceneEnvironment *self) {
  return self->probeHorizon();
}

//  QVector3D QQuick3DSceneEnvironment::probeOrientation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK24QQuick3DSceneEnvironment16probeOrientationEv(
    const QQuick3DSceneEnvironment *self) {
  return new QVector3D(self->probeOrientation());
}

//  bool QQuick3DSceneEnvironment::depthTestEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment16depthTestEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->depthTestEnabled();
}

//  bool QQuick3DSceneEnvironment::depthPrePassEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment19depthPrePassEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->depthPrePassEnabled();
}

//  QQuick3DEnvironmentTonemapModes QQuick3DSceneEnvironment::tonemapMode()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentTonemapModes ritual_ZNK24QQuick3DSceneEnvironment11tonemapModeEv(
    const QQuick3DSceneEnvironment *self) {
  return self->tonemapMode();
}

//  QQmlListProperty<QQuick3DEffect> QQuick3DSceneEnvironment::effects()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DEffect> *ritual_ZN24QQuick3DSceneEnvironment7effectsEv(
    QQuick3DSceneEnvironment *self) {
  return new QQmlListProperty<QQuick3DEffect>(self->effects());
}

//  float QQuick3DSceneEnvironment::skyboxBlurAmount() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment16skyboxBlurAmountEv(
    const QQuick3DSceneEnvironment *self) {
  return self->skyboxBlurAmount();
}

//  bool QQuick3DSceneEnvironment::specularAAEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment17specularAAEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->specularAAEnabled();
}

//  QQuick3DLightmapper *QQuick3DSceneEnvironment::lightmapper() const
extern "C" Q_DECL_EXPORT
QQuick3DLightmapper *ritual_ZNK24QQuick3DSceneEnvironment11lightmapperEv(
    const QQuick3DSceneEnvironment *self) {
  return self->lightmapper();
}

//  QQuick3DCubeMapTexture *QQuick3DSceneEnvironment::skyBoxCubeMap() const
extern "C" Q_DECL_EXPORT
QQuick3DCubeMapTexture *ritual_ZNK24QQuick3DSceneEnvironment13skyBoxCubeMapEv(
    const QQuick3DSceneEnvironment *self) {
  return self->skyBoxCubeMap();
}

//  QQuick3DDebugSettings *QQuick3DSceneEnvironment::debugSettings() const
extern "C" Q_DECL_EXPORT
QQuick3DDebugSettings *ritual_ZNK24QQuick3DSceneEnvironment13debugSettingsEv(
    const QQuick3DSceneEnvironment *self) {
  return self->debugSettings();
}

//  QRect QQuick3DSceneEnvironment::scissorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QQuick3DSceneEnvironment11scissorRectEv(
    const QQuick3DSceneEnvironment *self) {
  return new QRect(self->scissorRect());
}

//  QQuick3DFog *QQuick3DSceneEnvironment::fog() const
extern "C" Q_DECL_EXPORT
QQuick3DFog *ritual_ZNK24QQuick3DSceneEnvironment3fogEv(
    const QQuick3DSceneEnvironment *self) {
  return self->fog();
}

//  QQuick3DEnvironmentOITMethod QQuick3DSceneEnvironment::oitMethod() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment::QQuick3DEnvironmentOITMethod ritual_ZNK24QQuick3DSceneEnvironment9oitMethodEv(
    const QQuick3DSceneEnvironment *self) {
  return self->oitMethod();
}

//  bool QQuick3DSceneEnvironment::gridEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment11gridEnabledEv(
    const QQuick3DSceneEnvironment *self) {
  return self->gridEnabled();
}

//  void QQuick3DSceneEnvironment::setGridEnabled(bool newGridEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment14setGridEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool newGridEnabled) {
  self->setGridEnabled(newGridEnabled);
}

//  float QQuick3DSceneEnvironment::gridScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DSceneEnvironment9gridScaleEv(
    const QQuick3DSceneEnvironment *self) {
  return self->gridScale();
}

//  void QQuick3DSceneEnvironment::setGridScale(float newGridScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment12setGridScaleEf(
    QQuick3DSceneEnvironment *self,
    float newGridScale) {
  self->setGridScale(newGridScale);
}

//  uint QQuick3DSceneEnvironment::gridFlags() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK24QQuick3DSceneEnvironment9gridFlagsEv(
    const QQuick3DSceneEnvironment *self) {
  return self->gridFlags();
}

//  void QQuick3DSceneEnvironment::setGridFlags(uint newGridFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment12setGridFlagsEj(
    QQuick3DSceneEnvironment *self,
    uint newGridFlags) {
  self->setGridFlags(newGridFlags);
}

//  void QQuick3DSceneEnvironment::setAntialiasingMode(QQuick3DSceneEnvironme
//      nt::QQuick3DEnvironmentAAModeValues antialiasingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19setAntialiasingModeENS_31QQuick3DEnvironmentAAModeValuesE(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneEnvironment::QQuick3DEnvironmentAAModeValues antialiasingMode) {
  self->setAntialiasingMode(antialiasingMode);
}

//  void QQuick3DSceneEnvironment::setAntialiasingQuality(QQuick3DSceneEnviro
//      nment::QQuick3DEnvironmentAAQualityValues antialiasingQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment22setAntialiasingQualityENS_34QQuick3DEnvironmentAAQualityValuesE(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneEnvironment::QQuick3DEnvironmentAAQualityValues antialiasingQuality) {
  self->setAntialiasingQuality(antialiasingQuality);
}

//  void QQuick3DSceneEnvironment::setTemporalAAMode(const
//      QQuick3DEnvironmentTemporalAAMode &newTemporalAAMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17setTemporalAAModeERKNS_33QQuick3DEnvironmentTemporalAAModeE(
    QQuick3DSceneEnvironment *self,
    const QQuick3DSceneEnvironment::QQuick3DEnvironmentTemporalAAMode *newTemporalAAMode) {
  self->setTemporalAAMode(*newTemporalAAMode);
}

//  void QQuick3DSceneEnvironment::setTemporalAAEnabled(bool
//      temporalAAEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment20setTemporalAAEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool temporalAAEnabled) {
  self->setTemporalAAEnabled(temporalAAEnabled);
}

//  void QQuick3DSceneEnvironment::setTemporalAAStrength(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment21setTemporalAAStrengthEf(
    QQuick3DSceneEnvironment *self,
    float strength) {
  self->setTemporalAAStrength(strength);
}

//  void QQuick3DSceneEnvironment::setBackgroundMode(QQuick3DSceneEnvironment
//      ::QQuick3DEnvironmentBackgroundTypes backgroundMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17setBackgroundModeENS_34QQuick3DEnvironmentBackgroundTypesE(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneEnvironment::QQuick3DEnvironmentBackgroundTypes backgroundMode) {
  self->setBackgroundMode(backgroundMode);
}

//  void QQuick3DSceneEnvironment::setClearColor(const QColor &clearColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13setClearColorERK6QColor(
    QQuick3DSceneEnvironment *self,
    const QColor *clearColor) {
  self->setClearColor(*clearColor);
}

//  void QQuick3DSceneEnvironment::setAoStrength(float aoStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13setAoStrengthEf(
    QQuick3DSceneEnvironment *self,
    float aoStrength) {
  self->setAoStrength(aoStrength);
}

//  void QQuick3DSceneEnvironment::setAoDistance(float aoDistance)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13setAoDistanceEf(
    QQuick3DSceneEnvironment *self,
    float aoDistance) {
  self->setAoDistance(aoDistance);
}

//  void QQuick3DSceneEnvironment::setAoSoftness(float aoSoftness)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13setAoSoftnessEf(
    QQuick3DSceneEnvironment *self,
    float aoSoftness) {
  self->setAoSoftness(aoSoftness);
}

//  void QQuick3DSceneEnvironment::setAoDither(bool aoDither)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment11setAoDitherEb(
    QQuick3DSceneEnvironment *self,
    bool aoDither) {
  self->setAoDither(aoDither);
}

//  void QQuick3DSceneEnvironment::setAoSampleRate(int aoSampleRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment15setAoSampleRateEi(
    QQuick3DSceneEnvironment *self,
    int aoSampleRate) {
  self->setAoSampleRate(aoSampleRate);
}

//  void QQuick3DSceneEnvironment::setAoBias(float aoBias)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment9setAoBiasEf(
    QQuick3DSceneEnvironment *self,
    float aoBias) {
  self->setAoBias(aoBias);
}

//  void QQuick3DSceneEnvironment::setLightProbe(QQuick3DTexture *lightProbe)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13setLightProbeEP15QQuick3DTexture(
    QQuick3DSceneEnvironment *self,
    QQuick3DTexture *lightProbe) {
  self->setLightProbe(lightProbe);
}

//  void QQuick3DSceneEnvironment::setSkyMaterial(QQuick3DSkyMaterial
//      *skyMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment14setSkyMaterialEP19QQuick3DSkyMaterial(
    QQuick3DSceneEnvironment *self,
    QQuick3DSkyMaterial *skyMaterial) {
  self->setSkyMaterial(skyMaterial);
}

//  void QQuick3DSceneEnvironment::setProbeExposure(float probeExposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment16setProbeExposureEf(
    QQuick3DSceneEnvironment *self,
    float probeExposure) {
  self->setProbeExposure(probeExposure);
}

//  void QQuick3DSceneEnvironment::setProbeHorizon(float probeHorizon)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment15setProbeHorizonEf(
    QQuick3DSceneEnvironment *self,
    float probeHorizon) {
  self->setProbeHorizon(probeHorizon);
}

//  void QQuick3DSceneEnvironment::setProbeOrientation(const QVector3D
//      &orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19setProbeOrientationERK9QVector3D(
    QQuick3DSceneEnvironment *self,
    const QVector3D *orientation) {
  self->setProbeOrientation(*orientation);
}

//  void QQuick3DSceneEnvironment::setDepthTestEnabled(bool depthTestEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19setDepthTestEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool depthTestEnabled) {
  self->setDepthTestEnabled(depthTestEnabled);
}

//  void QQuick3DSceneEnvironment::setDepthPrePassEnabled(bool
//      depthPrePassEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment22setDepthPrePassEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool depthPrePassEnabled) {
  self->setDepthPrePassEnabled(depthPrePassEnabled);
}

//  void QQuick3DSceneEnvironment::setTonemapMode(QQuick3DSceneEnvironment::Q
//      Quick3DEnvironmentTonemapModes tonemapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment14setTonemapModeENS_31QQuick3DEnvironmentTonemapModesE(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneEnvironment::QQuick3DEnvironmentTonemapModes tonemapMode) {
  self->setTonemapMode(tonemapMode);
}

//  void QQuick3DSceneEnvironment::setSkyboxBlurAmount(float
//      newSkyboxBlurAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19setSkyboxBlurAmountEf(
    QQuick3DSceneEnvironment *self,
    float newSkyboxBlurAmount) {
  self->setSkyboxBlurAmount(newSkyboxBlurAmount);
}

//  void QQuick3DSceneEnvironment::setSpecularAAEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment20setSpecularAAEnabledEb(
    QQuick3DSceneEnvironment *self,
    bool enabled) {
  self->setSpecularAAEnabled(enabled);
}

//  void QQuick3DSceneEnvironment::setSkyBoxCubeMap(QQuick3DCubeMapTexture
//      *newSkyBoxCubeMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment16setSkyBoxCubeMapEP22QQuick3DCubeMapTexture(
    QQuick3DSceneEnvironment *self,
    QQuick3DCubeMapTexture *newSkyBoxCubeMap) {
  self->setSkyBoxCubeMap(newSkyBoxCubeMap);
}

//  void QQuick3DSceneEnvironment::setLightmapper(QQuick3DLightmapper
//      *lightmapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment14setLightmapperEP19QQuick3DLightmapper(
    QQuick3DSceneEnvironment *self,
    QQuick3DLightmapper *lightmapper) {
  self->setLightmapper(lightmapper);
}

//  void QQuick3DSceneEnvironment::setDebugSettings(QQuick3DDebugSettings
//      *newDebugSettings)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment16setDebugSettingsEP21QQuick3DDebugSettings(
    QQuick3DSceneEnvironment *self,
    QQuick3DDebugSettings *newDebugSettings) {
  self->setDebugSettings(newDebugSettings);
}

//  void QQuick3DSceneEnvironment::setScissorRect(QRect scissorRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment14setScissorRectE5QRect(
    QQuick3DSceneEnvironment *self,
    const QRect *scissorRect) {
  self->setScissorRect(*scissorRect);
}

//  void QQuick3DSceneEnvironment::setFog(QQuick3DFog *fog)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment6setFogEP11QQuick3DFog(
    QQuick3DSceneEnvironment *self,
    QQuick3DFog *fog) {
  self->setFog(fog);
}

//  void QQuick3DSceneEnvironment::setOitMethod(QQuick3DSceneEnvironment::QQu
//      ick3DEnvironmentOITMethod mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment12setOitMethodENS_28QQuick3DEnvironmentOITMethodE(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneEnvironment::QQuick3DEnvironmentOITMethod mode) {
  self->setOitMethod(mode);
}

//  void QQuick3DSceneEnvironment::antialiasingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment23antialiasingModeChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->antialiasingModeChanged();
}

//  void QQuick3DSceneEnvironment::antialiasingQualityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment26antialiasingQualityChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->antialiasingQualityChanged();
}

//  void QQuick3DSceneEnvironment::temporalAAModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment21temporalAAModeChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->temporalAAModeChanged();
}

//  void QQuick3DSceneEnvironment::temporalAAEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment24temporalAAEnabledChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->temporalAAEnabledChanged();
}

//  void QQuick3DSceneEnvironment::temporalAAStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment25temporalAAStrengthChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->temporalAAStrengthChanged();
}

//  void QQuick3DSceneEnvironment::backgroundModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment21backgroundModeChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->backgroundModeChanged();
}

//  void QQuick3DSceneEnvironment::clearColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17clearColorChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->clearColorChanged();
}

//  void QQuick3DSceneEnvironment::aoStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17aoStrengthChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoStrengthChanged();
}

//  void QQuick3DSceneEnvironment::aoDistanceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17aoDistanceChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoDistanceChanged();
}

//  void QQuick3DSceneEnvironment::aoSoftnessChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17aoSoftnessChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoSoftnessChanged();
}

//  void QQuick3DSceneEnvironment::aoDitherChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment15aoDitherChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoDitherChanged();
}

//  void QQuick3DSceneEnvironment::aoSampleRateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19aoSampleRateChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoSampleRateChanged();
}

//  void QQuick3DSceneEnvironment::aoBiasChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment13aoBiasChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoBiasChanged();
}

//  void QQuick3DSceneEnvironment::aoEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment16aoEnabledChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->aoEnabledChanged();
}

//  void QQuick3DSceneEnvironment::lightProbeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment17lightProbeChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->lightProbeChanged();
}

//  void QQuick3DSceneEnvironment::skyMaterialChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment18skyMaterialChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->skyMaterialChanged();
}

//  void QQuick3DSceneEnvironment::probeExposureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment20probeExposureChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->probeExposureChanged();
}

//  void QQuick3DSceneEnvironment::probeHorizonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment19probeHorizonChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->probeHorizonChanged();
}

//  void QQuick3DSceneEnvironment::probeOrientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment23probeOrientationChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->probeOrientationChanged();
}

//  void QQuick3DSceneEnvironment::depthTestEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment23depthTestEnabledChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->depthTestEnabledChanged();
}

//  void QQuick3DSceneEnvironment::depthPrePassEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment26depthPrePassEnabledChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->depthPrePassEnabledChanged();
}

//  void QQuick3DSceneEnvironment::tonemapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment18tonemapModeChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->tonemapModeChanged();
}

//  void QQuick3DSceneEnvironment::skyboxBlurAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment23skyboxBlurAmountChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->skyboxBlurAmountChanged();
}

//  void QQuick3DSceneEnvironment::specularAAEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment24specularAAEnabledChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->specularAAEnabledChanged();
}

//  void QQuick3DSceneEnvironment::lightmapperChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment18lightmapperChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->lightmapperChanged();
}

//  void QQuick3DSceneEnvironment::skyBoxCubeMapChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment20skyBoxCubeMapChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->skyBoxCubeMapChanged();
}

//  void QQuick3DSceneEnvironment::debugSettingsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment20debugSettingsChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->debugSettingsChanged();
}

//  void QQuick3DSceneEnvironment::scissorRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment18scissorRectChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->scissorRectChanged();
}

//  void QQuick3DSceneEnvironment::fogChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment10fogChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->fogChanged();
}

//  void QQuick3DSceneEnvironment::oitMethodChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment16oitMethodChangedEv(
    QQuick3DSceneEnvironment *self) {
  self->oitMethodChanged();
}

//  QSSGRenderGraphObject
//      *QQuick3DSceneEnvironment::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN24QQuick3DSceneEnvironment17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSceneEnvironment *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DSceneEnvironment::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DSceneEnvironment *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  const QVector<QQuick3DEffect *> &QQuick3DSceneEnvironment::effectList()
//      const
extern "C" Q_DECL_EXPORT
const QVector<QQuick3DEffect *> *ritual_ZNK24QQuick3DSceneEnvironment10effectListEv(
    const QQuick3DSceneEnvironment *self) {
  return &(self->effectList());
}

//  bool QQuick3DSceneEnvironment::useBuiltinTonemapper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv(
    const QQuick3DSceneEnvironment *self) {
  return self->useBuiltinTonemapper();
}

//  float QQuick3DSceneEnvironment::defaultAoDistance()
extern "C" Q_DECL_EXPORT
float ritual_ZN24QQuick3DSceneEnvironment17defaultAoDistanceEv() {
  return QQuick3DSceneEnvironment::defaultAoDistance();
}

//  void QQuick3DSceneEnvironment::qmlAppendEffect(QQmlListProperty<QQuick3DE
//      ffect> *list, QQuick3DEffect *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment15qmlAppendEffectEP16QQmlListPropertyI14QQuick3DEffectEPS1_(
    QQmlListProperty<QQuick3DEffect> *list,
    QQuick3DEffect *effect) {
  QQuick3DSceneEnvironment::qmlAppendEffect(list, effect);
}

//  QQuick3DEffect
//      *QQuick3DSceneEnvironment::qmlEffectAt(QQmlListProperty<QQuick3DEffec
//      t> *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuick3DEffect *ritual_ZN24QQuick3DSceneEnvironment11qmlEffectAtEP16QQmlListPropertyI14QQuick3DEffectEx(
    QQmlListProperty<QQuick3DEffect> *list,
    qsizetype index) {
  return QQuick3DSceneEnvironment::qmlEffectAt(list, index);
}

//  qsizetype QQuick3DSceneEnvironment::qmlEffectsCount(QQmlListProperty<QQui
//      ck3DEffect> *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QQuick3DSceneEnvironment15qmlEffectsCountEP16QQmlListPropertyI14QQuick3DEffectE(
    QQmlListProperty<QQuick3DEffect> *list) {
  return QQuick3DSceneEnvironment::qmlEffectsCount(list);
}

//  void QQuick3DSceneEnvironment::qmlClearEffects(QQmlListProperty<QQuick3DE
//      ffect> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment15qmlClearEffectsEP16QQmlListPropertyI14QQuick3DEffectE(
    QQmlListProperty<QQuick3DEffect> *list) {
  QQuick3DSceneEnvironment::qmlClearEffects(list);
}

//  void QQuick3DSceneEnvironment::updateSceneManager(QQuick3DSceneManager
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSceneEnvironment18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DSceneEnvironment *self,
    QQuick3DSceneManager *manager) {
  self->updateSceneManager(manager);
}

//  a Python function taken by a CuteQQuick3DSceneEnvironment, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSceneEnvironment(
    QQuick3DSceneEnvironment *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSceneEnvironment *>(self)->take(key, call);
}

//  QSSGRenderGraphObject
//      *QQuick3DSceneEnvironment::updateSpatialNode(QSSGRenderGraphObject
//      *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN24QQuick3DSceneEnvironment17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DSceneEnvironment *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DSceneEnvironment *>(self)->OwnQQuick3DSceneEnvironment::updateSpatialNode(
      node);
}

//  void QQuick3DSceneEnvironment::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DSceneEnvironment10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DSceneEnvironment *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DSceneEnvironment *>(self)->OwnQQuick3DSceneEnvironment::itemChange(
      a0,
      *a1);
}

//  bool QQuick3DSceneEnvironment::useBuiltinTonemapper() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQuick3DSceneEnvironment20useBuiltinTonemapperEv(
    const QQuick3DSceneEnvironment *self) {
  return static_cast<const OwnQQuick3DSceneEnvironment *>(self)->OwnQQuick3DSceneEnvironment::useBuiltinTonemapper();
}

//  a QQmlListProperty<QQuick3DEffect> a ritual of QQuick3DSceneEnvironment
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSceneEnvironment__QQmlListProperty_QQuick3DEffect(
    QQmlListProperty<QQuick3DEffect> *self) {
  delete self;
}
