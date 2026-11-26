//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrendersurfaceselector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrendersurfaceselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A Qt3DRender::QRenderSurfaceSelectorPrivate that Python can take functions over in. Every Qt3DRender::QRenderSurfaceSelectorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QRenderSurfaceSelectorPrivateCall1)(const void *, int *);
class CuteQt3DRender_QRenderSurfaceSelectorPrivate : public Qt3DRender::QRenderSurfaceSelectorPrivate {
public:
  using Qt3DRender::QRenderSurfaceSelectorPrivate::QRenderSurfaceSelectorPrivate;
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
      CuteQt3DRender_QRenderSurfaceSelectorPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderSurfaceSelectorPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderSurfaceSelectorPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QRenderSurfaceSelectorPrivate::QRenderSurfaceSelectorPrivate(
//      )
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSurfaceSelectorPrivate *ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivateC1Ev() {
  return new CuteQt3DRender_QRenderSurfaceSelectorPrivate();
}

//  Qt3DRender::QRenderSurfaceSelectorPrivate::~QRenderSurfaceSelectorPrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivateD1Ev(
    Qt3DRender::QRenderSurfaceSelectorPrivate *self) {
  delete self;
}

//  QRenderSurfaceSelector
//      *Qt3DRender::QRenderSurfaceSelectorPrivate::find(QObject *rootObject)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSurfaceSelector *ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivate4findEP7QObject(
    QObject *rootObject) {
  return Qt3DRender::QRenderSurfaceSelectorPrivate::find(rootObject);
}

//  void Qt3DRender::QRenderSurfaceSelectorPrivate::setExternalRenderTargetSi
//      ze(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender29QRenderSurfaceSelectorPrivate27setExternalRenderTargetSizeERK5QSize(
    Qt3DRender::QRenderSurfaceSelectorPrivate *self,
    const QSize *size) {
  self->setExternalRenderTargetSize(*size);
}

//  QSize
//      Qt3DRender::QRenderSurfaceSelectorPrivate::externalRenderTargetSize()
//      const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DRender29QRenderSurfaceSelectorPrivate24externalRenderTargetSizeEv(
    const Qt3DRender::QRenderSurfaceSelectorPrivate *self) {
  return new QSize(self->externalRenderTargetSize());
}

//  a Python function taken by a
//      CuteQt3DRender_QRenderSurfaceSelectorPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderSurfaceSelectorPrivate(
    Qt3DRender::QRenderSurfaceSelectorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderSurfaceSelectorPrivate *>(self)->take(key, call);
}
