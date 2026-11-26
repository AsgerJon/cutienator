//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/levelofdetail_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/levelofdetail_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DRender::Render::LevelOfDetail that Python can take functions over in. Every Qt3DRender::Render::LevelOfDetail
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_LevelOfDetailCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_LevelOfDetail : public Qt3DRender::Render::LevelOfDetail {
public:
  using Qt3DRender::Render::LevelOfDetail::LevelOfDetail;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_LevelOfDetailCall0 call = reinterpret_cast<CuteQt3DRender_Render_LevelOfDetailCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::LevelOfDetail::LevelOfDetail()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LevelOfDetail *ritual_ZN10Qt3DRender6Render13LevelOfDetailC1Ev() {
  return new CuteQt3DRender_Render_LevelOfDetail();
}

//  Qt3DRender::Render::LevelOfDetail::~LevelOfDetail()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13LevelOfDetailD1Ev(
    Qt3DRender::Render::LevelOfDetail *self) {
  delete self;
}

//  void Qt3DRender::Render::LevelOfDetail::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13LevelOfDetail7cleanupEv(
    Qt3DRender::Render::LevelOfDetail *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13LevelOfDetail16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::LevelOfDetail *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId Qt3DRender::Render::LevelOfDetail::camera() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render13LevelOfDetail6cameraEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return new Qt3DCore::QNodeId(self->camera());
}

//  int Qt3DRender::Render::LevelOfDetail::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render13LevelOfDetail12currentIndexEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return self->currentIndex();
}

//  QLevelOfDetail::ThresholdType
//      Qt3DRender::Render::LevelOfDetail::thresholdType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetail::ThresholdType ritual_ZNK10Qt3DRender6Render13LevelOfDetail13thresholdTypeEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return self->thresholdType();
}

//  QList<qreal> Qt3DRender::Render::LevelOfDetail::thresholds() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK10Qt3DRender6Render13LevelOfDetail10thresholdsEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return new QList<qreal>(self->thresholds());
}

//  float Qt3DRender::Render::LevelOfDetail::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render13LevelOfDetail6radiusEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return self->radius();
}

//  QVector3D Qt3DRender::Render::LevelOfDetail::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render13LevelOfDetail6centerEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return new QVector3D(self->center());
}

//  bool Qt3DRender::Render::LevelOfDetail::hasBoundingVolumeOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13LevelOfDetail25hasBoundingVolumeOverrideEv(
    const Qt3DRender::Render::LevelOfDetail *self) {
  return self->hasBoundingVolumeOverride();
}

//  void Qt3DRender::Render::LevelOfDetail::setCurrentIndex(int currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13LevelOfDetail15setCurrentIndexEi(
    Qt3DRender::Render::LevelOfDetail *self,
    int currentIndex) {
  self->setCurrentIndex(currentIndex);
}

//  a Python function taken by a CuteQt3DRender_Render_LevelOfDetail, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_LevelOfDetail(
    Qt3DRender::Render::LevelOfDetail *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_LevelOfDetail *>(self)->take(key, call);
}

//  void Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render13LevelOfDetail16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::LevelOfDetail *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::LevelOfDetail::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<qreal> a ritual of Qt3DRender::Render::LevelOfDetail gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_LevelOfDetail__QList_qreal(
    QList<qreal> *self) {
  delete self;
}
