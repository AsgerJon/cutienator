//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/raycaster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/raycaster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::RayCaster that Python can take functions over in. Every Qt3DRender::Render::RayCaster
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_RayCasterCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_RayCaster : public Qt3DRender::Render::RayCaster {
public:
  using Qt3DRender::Render::RayCaster::RayCaster;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::RayCaster::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_RayCasterCall0 call = reinterpret_cast<CuteQt3DRender_Render_RayCasterCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::RayCaster::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::RayCaster::RayCaster()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RayCaster *ritual_ZN10Qt3DRender6Render9RayCasterC1Ev() {
  return new CuteQt3DRender_Render_RayCaster();
}

//  Qt3DRender::Render::RayCaster::~RayCaster()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9RayCasterD1Ev(
    Qt3DRender::Render::RayCaster *self) {
  delete self;
}

//  QAbstractRayCasterPrivate::RayCasterType
//      Qt3DRender::Render::RayCaster::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCasterPrivate::RayCasterType ritual_ZNK10Qt3DRender6Render9RayCaster4typeEv(
    const Qt3DRender::Render::RayCaster *self) {
  return self->type();
}

//  QAbstractRayCaster::RunMode Qt3DRender::Render::RayCaster::runMode()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::RunMode ritual_ZNK10Qt3DRender6Render9RayCaster7runModeEv(
    const Qt3DRender::Render::RayCaster *self) {
  return self->runMode();
}

//  QVector3D Qt3DRender::Render::RayCaster::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render9RayCaster6originEv(
    const Qt3DRender::Render::RayCaster *self) {
  return new QVector3D(self->origin());
}

//  QVector3D Qt3DRender::Render::RayCaster::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render9RayCaster9directionEv(
    const Qt3DRender::Render::RayCaster *self) {
  return new QVector3D(self->direction());
}

//  float Qt3DRender::Render::RayCaster::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render9RayCaster6lengthEv(
    const Qt3DRender::Render::RayCaster *self) {
  return self->length();
}

//  QPoint Qt3DRender::Render::RayCaster::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10Qt3DRender6Render9RayCaster8positionEv(
    const Qt3DRender::Render::RayCaster *self) {
  return new QPoint(self->position());
}

//  Qt3DCore::QNodeIdVector Qt3DRender::Render::RayCaster::layerIds() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK10Qt3DRender6Render9RayCaster8layerIdsEv(
    const Qt3DRender::Render::RayCaster *self) {
  return new Qt3DCore::QNodeIdVector(self->layerIds());
}

//  QAbstractRayCaster::FilterMode
//      Qt3DRender::Render::RayCaster::filterMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::FilterMode ritual_ZNK10Qt3DRender6Render9RayCaster10filterModeEv(
    const Qt3DRender::Render::RayCaster *self) {
  return self->filterMode();
}

//  void Qt3DRender::Render::RayCaster::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9RayCaster16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RayCaster *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::RayCaster::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9RayCaster7cleanupEv(
    Qt3DRender::Render::RayCaster *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::RayCaster::notifyJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9RayCaster9notifyJobEv(
    Qt3DRender::Render::RayCaster *self) {
  self->notifyJob();
}

//  a Python function taken by a CuteQt3DRender_Render_RayCaster, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_RayCaster(
    Qt3DRender::Render::RayCaster *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_RayCaster *>(self)->take(key, call);
}

//  void Qt3DRender::Render::RayCaster::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9RayCaster16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RayCaster *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RayCaster::syncFromFrontEnd(frontEnd, firstTime);
}

//  a Qt3DCore::QNodeIdVector a ritual of Qt3DRender::Render::RayCaster gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_RayCaster__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}
