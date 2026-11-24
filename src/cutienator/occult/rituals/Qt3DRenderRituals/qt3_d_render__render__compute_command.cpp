//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/computecommand_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/computecommand_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::ComputeCommand that Python can take functions over in. Every Qt3DRender::Render::ComputeCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_ComputeCommandCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_ComputeCommand : public Qt3DRender::Render::ComputeCommand {
public:
  using Qt3DRender::Render::ComputeCommand::ComputeCommand;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ComputeCommandCall0 call = reinterpret_cast<CuteQt3DRender_Render_ComputeCommandCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  int Qt3DRender::Render::ComputeCommand::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render14ComputeCommand1xEv(
    const Qt3DRender::Render::ComputeCommand *self) {
  return self->x();
}

//  int Qt3DRender::Render::ComputeCommand::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render14ComputeCommand1yEv(
    const Qt3DRender::Render::ComputeCommand *self) {
  return self->y();
}

//  int Qt3DRender::Render::ComputeCommand::z() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render14ComputeCommand1zEv(
    const Qt3DRender::Render::ComputeCommand *self) {
  return self->z();
}

//  int Qt3DRender::Render::ComputeCommand::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render14ComputeCommand10frameCountEv(
    const Qt3DRender::Render::ComputeCommand *self) {
  return self->frameCount();
}

//  QComputeCommand::RunType Qt3DRender::Render::ComputeCommand::runType()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QComputeCommand::RunType ritual_ZNK10Qt3DRender6Render14ComputeCommand7runTypeEv(
    const Qt3DRender::Render::ComputeCommand *self) {
  return self->runType();
}

//  a Python function taken by a CuteQt3DRender_Render_ComputeCommand, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_ComputeCommand(
    Qt3DRender::Render::ComputeCommand *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_ComputeCommand *>(self)->take(key, call);
}

//  void Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render14ComputeCommand16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ComputeCommand *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ComputeCommand::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
