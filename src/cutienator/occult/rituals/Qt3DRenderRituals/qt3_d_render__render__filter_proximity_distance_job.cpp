//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/filterproximitydistancejob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/filterproximitydistancejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::FilterProximityDistanceJob that Python can take functions over in. Every Qt3DRender::Render::FilterProximityDistanceJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Render_FilterProximityDistanceJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_FilterProximityDistanceJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
class CuteQt3DRender_Render_FilterProximityDistanceJob : public Qt3DRender::Render::FilterProximityDistanceJob {
public:
  using Qt3DRender::Render::FilterProximityDistanceJob::FilterProximityDistanceJob;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DRender::Render::FilterProximityDistanceJob::isRequired()
  bool isRequired() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_FilterProximityDistanceJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_FilterProximityDistanceJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Render::FilterProximityDistanceJob::isRequired();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_FilterProximityDistanceJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_FilterProximityDistanceJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }
};

//  Qt3DRender::Render::FilterProximityDistanceJob::FilterProximityDistanceJo
//      b()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FilterProximityDistanceJob *ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJobC1Ev() {
  return new CuteQt3DRender_Render_FilterProximityDistanceJob();
}

//  Qt3DRender::Render::FilterProximityDistanceJob::~FilterProximityDistanceJ
//      ob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJobD1Ev(
    Qt3DRender::Render::FilterProximityDistanceJob *self) {
  delete self;
}

//  void
//      Qt3DRender::Render::FilterProximityDistanceJob::setManager(NodeManage
//      rs *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob10setManagerEPNS0_12NodeManagersE(
    Qt3DRender::Render::FilterProximityDistanceJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManager(manager);
}

//  void Qt3DRender::Render::FilterProximityDistanceJob::setProximityFilterId
//      s(const Qt3DCore::QNodeIdVector &proximityFilterIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob21setProximityFilterIdsERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterProximityDistanceJob *self,
    const Qt3DCore::QNodeIdVector *proximityFilterIds) {
  self->setProximityFilterIds(*proximityFilterIds);
}

//  bool Qt3DRender::Render::FilterProximityDistanceJob::hasProximityFilter()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render26FilterProximityDistanceJob18hasProximityFilterEv(
    const Qt3DRender::Render::FilterProximityDistanceJob *self) {
  return self->hasProximityFilter();
}

//  void Qt3DRender::Render::FilterProximityDistanceJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob3runEv(
    Qt3DRender::Render::FilterProximityDistanceJob *self) {
  self->run();
}

//  const std::vector<Entity *>
//      &Qt3DRender::Render::FilterProximityDistanceJob::filteredEntities()
//      const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::Render::Entity *> *ritual_ZNK10Qt3DRender6Render26FilterProximityDistanceJob16filteredEntitiesEv(
    const Qt3DRender::Render::FilterProximityDistanceJob *self) {
  return &(self->filteredEntities());
}

//  bool Qt3DRender::Render::FilterProximityDistanceJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob10isRequiredEv(
    Qt3DRender::Render::FilterProximityDistanceJob *self) {
  return self->isRequired();
}

//  void Qt3DRender::Render::FilterProximityDistanceJob::selectAllEntities()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob17selectAllEntitiesEv(
    Qt3DRender::Render::FilterProximityDistanceJob *self) {
  self->selectAllEntities();
}

//  void Qt3DRender::Render::FilterProximityDistanceJob::filterEntities(const
//      std::vector<Entity *> &entitiesToFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render26FilterProximityDistanceJob14filterEntitiesERKSt6vectorIPNS0_6EntityESaIS4_EE(
    Qt3DRender::Render::FilterProximityDistanceJob *self,
    const std::vector<Qt3DRender::Render::Entity *> *entitiesToFilter) {
  self->filterEntities(*entitiesToFilter);
}

//  a Python function taken by a
//      CuteQt3DRender_Render_FilterProximityDistanceJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_FilterProximityDistanceJob(
    Qt3DRender::Render::FilterProximityDistanceJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_FilterProximityDistanceJob *>(self)->take(key, call);
}

//  bool Qt3DRender::Render::FilterProximityDistanceJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render26FilterProximityDistanceJob10isRequiredEv(
    Qt3DRender::Render::FilterProximityDistanceJob *self) {
  return self->Qt3DRender::Render::FilterProximityDistanceJob::isRequired();
}
