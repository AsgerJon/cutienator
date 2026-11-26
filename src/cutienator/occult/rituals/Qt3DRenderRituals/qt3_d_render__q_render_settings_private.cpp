//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendersettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendersettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QRenderSettingsPrivate that Python can take functions over in. Every Qt3DRender::QRenderSettingsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderSettingsPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QRenderSettingsPrivateCall1)(const void *, int *);
class CuteQt3DRender_QRenderSettingsPrivate : public Qt3DRender::QRenderSettingsPrivate {
public:
  using Qt3DRender::QRenderSettingsPrivate::QRenderSettingsPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderSettingsPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderSettingsPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderSettingsPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QRenderSettingsPrivate::QRenderSettingsPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettingsPrivate *ritual_ZN10Qt3DRender22QRenderSettingsPrivateC1Ev() {
  return new CuteQt3DRender_QRenderSettingsPrivate();
}

//  void Qt3DRender::QRenderSettingsPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate4initEv(
    Qt3DRender::QRenderSettingsPrivate *self) {
  self->init();
}

//  void Qt3DRender::QRenderSettingsPrivate::invalidateFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate15invalidateFrameEv(
    Qt3DRender::QRenderSettingsPrivate *self) {
  self->invalidateFrame();
}

//  void Qt3DRender::QRenderSettingsPrivate::_q_onPickingMethodChanged(QPicki
//      ngSettings::PickMethod pickMethod)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate25_q_onPickingMethodChangedENS_16QPickingSettings10PickMethodE(
    Qt3DRender::QRenderSettingsPrivate *self,
    Qt3DRender::QPickingSettings::PickMethod pickMethod) {
  self->_q_onPickingMethodChanged(pickMethod);
}

//  void Qt3DRender::QRenderSettingsPrivate::_q_onPickResultModeChanged(QPick
//      ingSettings::PickResultMode pickResultMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate26_q_onPickResultModeChangedENS_16QPickingSettings14PickResultModeE(
    Qt3DRender::QRenderSettingsPrivate *self,
    Qt3DRender::QPickingSettings::PickResultMode pickResultMode) {
  self->_q_onPickResultModeChanged(pickResultMode);
}

//  void Qt3DRender::QRenderSettingsPrivate::_q_onFaceOrientationPickingModeC
//      hanged(QPickingSettings::FaceOrientationPickingMode
//      faceOrientationPickingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate38_q_onFaceOrientationPickingModeChangedENS_16QPickingSettings26FaceOrientationPickingModeE(
    Qt3DRender::QRenderSettingsPrivate *self,
    Qt3DRender::QPickingSettings::FaceOrientationPickingMode faceOrientationPickingMode) {
  self->_q_onFaceOrientationPickingModeChanged(faceOrientationPickingMode);
}

//  void
//      Qt3DRender::QRenderSettingsPrivate::_q_onWorldSpaceToleranceChanged(f
//      loat worldSpaceTolerance)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QRenderSettingsPrivate31_q_onWorldSpaceToleranceChangedEf(
    Qt3DRender::QRenderSettingsPrivate *self,
    float worldSpaceTolerance) {
  self->_q_onWorldSpaceToleranceChanged(worldSpaceTolerance);
}

//  QRenderSettings *Qt3DRender::QRenderSettingsPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettings *ritual_ZN10Qt3DRender22QRenderSettingsPrivate6q_funcEv(
    Qt3DRender::QRenderSettingsPrivate *self) {
  return self->q_func();
}

//  const QRenderSettings *Qt3DRender::QRenderSettingsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderSettings *ritual_ZNK10Qt3DRender22QRenderSettingsPrivate6q_funcEv(
    const Qt3DRender::QRenderSettingsPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderSettingsPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderSettingsPrivate(
    Qt3DRender::QRenderSettingsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderSettingsPrivate *>(self)->take(key, call);
}
