//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/frustumcullingjob_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Vector3D is QVector3D or an SSE class by
//  system, and Matrix4x4 the same, so each value taken is made as
//  Vector3D(*x) or Matrix4x4(*x), and each value given is built from its
//  coordinates. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/frustumcullingjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <cstring>

//  A Qt3DRender::Render::FrustumCullingJob that Python can take functions over in. Every Qt3DRender::Render::FrustumCullingJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Render_FrustumCullingJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_FrustumCullingJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
class CuteQt3DRender_Render_FrustumCullingJob : public Qt3DRender::Render::FrustumCullingJob {
public:
  using Qt3DRender::Render::FrustumCullingJob::FrustumCullingJob;
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

  //  bool Qt3DRender::Render::FrustumCullingJob::isRequired()
  bool isRequired() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_FrustumCullingJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_FrustumCullingJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Render::FrustumCullingJob::isRequired();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_FrustumCullingJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_FrustumCullingJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }
};

//  void *Qt3DRender::Render::FrustumCullingJob::operator new(size_t s)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render17FrustumCullingJobnwEm(size_t s) {
  return Qt3DRender::Render::FrustumCullingJob::operator new(s);
}

//  void Qt3DRender::Render::FrustumCullingJob::operator delete(void *ptr)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrustumCullingJobdlEPv(void *ptr) {
  Qt3DRender::Render::FrustumCullingJob::operator delete(ptr);
}

//  void Qt3DRender::Render::FrustumCullingJob::setRoot(Entity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrustumCullingJob7setRootEPNS0_6EntityE(
    Qt3DRender::Render::FrustumCullingJob *self,
    Qt3DRender::Render::Entity *root) {
  self->setRoot(root);
}

//  void Qt3DRender::Render::FrustumCullingJob::setManagers(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrustumCullingJob11setManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::FrustumCullingJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManagers(manager);
}

//  void Qt3DRender::Render::FrustumCullingJob::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrustumCullingJob9setActiveEb(
    Qt3DRender::Render::FrustumCullingJob *self,
    bool active) {
  self->setActive(active);
}

//  bool Qt3DRender::Render::FrustumCullingJob::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render17FrustumCullingJob8isActiveEv(
    const Qt3DRender::Render::FrustumCullingJob *self) {
  return self->isActive();
}

//  void Qt3DRender::Render::FrustumCullingJob::setViewProjection(const
//      Matrix4x4 &viewProjection)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrustumCullingJob17setViewProjectionERK10QMatrix4x4(
    Qt3DRender::Render::FrustumCullingJob *self,
    const QMatrix4x4 *viewProjection) {
  self->setViewProjection(Matrix4x4(*viewProjection));
}

//  Matrix4x4 Qt3DRender::Render::FrustumCullingJob::viewProjection() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender6Render17FrustumCullingJob14viewProjectionEv(
    const Qt3DRender::Render::FrustumCullingJob *self) {
  Matrix4x4 m = self->viewProjection();
  QMatrix4x4 *out = new QMatrix4x4();
  for (int row = 0; row < 4; ++row)
    for (int col = 0; col < 4; ++col)
      (*out)(row, col) = m(row, col);
  return out;
}

//  const std::vector<Entity *>
//      &Qt3DRender::Render::FrustumCullingJob::visibleEntities() const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::Render::Entity *> *ritual_ZNK10Qt3DRender6Render17FrustumCullingJob15visibleEntitiesEv(
    const Qt3DRender::Render::FrustumCullingJob *self) {
  return &(self->visibleEntities());
}

//  a Python function taken by a CuteQt3DRender_Render_FrustumCullingJob, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_FrustumCullingJob(
    Qt3DRender::Render::FrustumCullingJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_FrustumCullingJob *>(self)->take(key, call);
}

//  bool Qt3DRender::Render::FrustumCullingJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render17FrustumCullingJob10isRequiredEv(
    Qt3DRender::Render::FrustumCullingJob *self) {
  return self->Qt3DRender::Render::FrustumCullingJob::isRequired();
}
