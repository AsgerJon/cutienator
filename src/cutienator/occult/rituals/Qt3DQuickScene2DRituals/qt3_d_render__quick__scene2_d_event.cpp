//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2devent_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2devent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Quick::Scene2DEvent that Python can take functions over in. Every Qt3DRender::Quick::Scene2DEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Quick_Scene2DEventCall0)(const void *, bool, int *);
typedef void * (*CuteQt3DRender_Quick_Scene2DEventCall1)(const void *, int *);
class CuteQt3DRender_Quick_Scene2DEvent : public Qt3DRender::Quick::Scene2DEvent {
public:
  using Qt3DRender::Quick::Scene2DEvent::Scene2DEvent;
  CuteQt3DRender_Quick_Scene2DEvent(const Qt3DRender::Quick::Scene2DEvent & other) : Qt3DRender::Quick::Scene2DEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DEventCall0 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DEventCall1 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  Qt3DRender::Quick::Scene2DEvent::Scene2DEvent(Type type)
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::Scene2DEvent *ritual_ZN10Qt3DRender5Quick12Scene2DEventC1ENS1_4TypeE(
    Qt3DRender::Quick::Scene2DEvent::Type type) {
  return new CuteQt3DRender_Quick_Scene2DEvent(type);
}

//  Qt3DRender::Quick::Scene2DEvent::~Scene2DEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick12Scene2DEventD1Ev(
    Qt3DRender::Quick::Scene2DEvent *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_Quick_Scene2DEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Quick_Scene2DEvent(
    Qt3DRender::Quick::Scene2DEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Quick_Scene2DEvent *>(self)->take(key, call);
}
