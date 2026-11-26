//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/objectpicker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/objectpicker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::ObjectPicker that Python can take functions over in. Every Qt3DRender::Render::ObjectPicker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_ObjectPickerCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_ObjectPicker : public Qt3DRender::Render::ObjectPicker {
public:
  using Qt3DRender::Render::ObjectPicker::ObjectPicker;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ObjectPickerCall0 call = reinterpret_cast<CuteQt3DRender_Render_ObjectPickerCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::ObjectPicker::ObjectPicker()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ObjectPicker *ritual_ZN10Qt3DRender6Render12ObjectPickerC1Ev() {
  return new CuteQt3DRender_Render_ObjectPicker();
}

//  Qt3DRender::Render::ObjectPicker::~ObjectPicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPickerD1Ev(
    Qt3DRender::Render::ObjectPicker *self) {
  delete self;
}

//  void Qt3DRender::Render::ObjectPicker::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPicker7cleanupEv(
    Qt3DRender::Render::ObjectPicker *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPicker16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ObjectPicker *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DRender::Render::ObjectPicker::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12ObjectPicker9isPressedEv(
    const Qt3DRender::Render::ObjectPicker *self) {
  return self->isPressed();
}

//  bool Qt3DRender::Render::ObjectPicker::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12ObjectPicker14isHoverEnabledEv(
    const Qt3DRender::Render::ObjectPicker *self) {
  return self->isHoverEnabled();
}

//  bool Qt3DRender::Render::ObjectPicker::isDragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12ObjectPicker13isDragEnabledEv(
    const Qt3DRender::Render::ObjectPicker *self) {
  return self->isDragEnabled();
}

//  void Qt3DRender::Render::ObjectPicker::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPicker10setPressedEb(
    Qt3DRender::Render::ObjectPicker *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  void Qt3DRender::Render::ObjectPicker::setPriority(int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPicker11setPriorityEi(
    Qt3DRender::Render::ObjectPicker *self,
    int priority) {
  self->setPriority(priority);
}

//  int Qt3DRender::Render::ObjectPicker::priority() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12ObjectPicker8priorityEv(
    const Qt3DRender::Render::ObjectPicker *self) {
  return self->priority();
}

//  void Qt3DRender::Render::ObjectPicker::notifyJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ObjectPicker9notifyJobEv(
    Qt3DRender::Render::ObjectPicker *self) {
  self->notifyJob();
}

//  a Python function taken by a CuteQt3DRender_Render_ObjectPicker, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_ObjectPicker(
    Qt3DRender::Render::ObjectPicker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_ObjectPicker *>(self)->take(key, call);
}

//  void Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12ObjectPicker16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ObjectPicker *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ObjectPicker::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
