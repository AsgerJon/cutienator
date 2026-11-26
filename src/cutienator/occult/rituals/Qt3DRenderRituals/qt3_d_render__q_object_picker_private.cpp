//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qobjectpicker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qobjectpicker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QObjectPickerPrivate that Python can take functions over in. Every Qt3DRender::QObjectPickerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QObjectPickerPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QObjectPickerPrivateCall1)(const void *, int *);
class CuteQt3DRender_QObjectPickerPrivate : public Qt3DRender::QObjectPickerPrivate {
public:
  using Qt3DRender::QObjectPickerPrivate::QObjectPickerPrivate;
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
      CuteQt3DRender_QObjectPickerPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QObjectPickerPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QObjectPickerPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QObjectPickerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QObjectPickerPrivate::QObjectPickerPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QObjectPickerPrivate *ritual_ZN10Qt3DRender20QObjectPickerPrivateC1Ev() {
  return new CuteQt3DRender_QObjectPickerPrivate();
}

//  QObjectPicker *Qt3DRender::QObjectPickerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QObjectPicker *ritual_ZN10Qt3DRender20QObjectPickerPrivate6q_funcEv(
    Qt3DRender::QObjectPickerPrivate *self) {
  return self->q_func();
}

//  const QObjectPicker *Qt3DRender::QObjectPickerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QObjectPicker *ritual_ZNK10Qt3DRender20QObjectPickerPrivate6q_funcEv(
    const Qt3DRender::QObjectPickerPrivate *self) {
  return self->q_func();
}

//  void Qt3DRender::QObjectPickerPrivate::propagateEvent(QPickEvent *event,
//      EventType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate14propagateEventEPNS_10QPickEventENS0_9EventTypeE(
    Qt3DRender::QObjectPickerPrivate *self,
    Qt3DRender::QPickEvent *event,
    Qt3DRender::QObjectPickerPrivate::EventType type) {
  self->propagateEvent(event, type);
}

//  void Qt3DRender::QObjectPickerPrivate::pressedEvent(QPickEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate12pressedEventEPNS_10QPickEventE(
    Qt3DRender::QObjectPickerPrivate *self,
    Qt3DRender::QPickEvent *event) {
  self->pressedEvent(event);
}

//  void Qt3DRender::QObjectPickerPrivate::clickedEvent(QPickEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate12clickedEventEPNS_10QPickEventE(
    Qt3DRender::QObjectPickerPrivate *self,
    Qt3DRender::QPickEvent *event) {
  self->clickedEvent(event);
}

//  void Qt3DRender::QObjectPickerPrivate::movedEvent(QPickEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate10movedEventEPNS_10QPickEventE(
    Qt3DRender::QObjectPickerPrivate *self,
    Qt3DRender::QPickEvent *event) {
  self->movedEvent(event);
}

//  void Qt3DRender::QObjectPickerPrivate::releasedEvent(QPickEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate13releasedEventEPNS_10QPickEventE(
    Qt3DRender::QObjectPickerPrivate *self,
    Qt3DRender::QPickEvent *event) {
  self->releasedEvent(event);
}

//  void Qt3DRender::QObjectPickerPrivate::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate10setPressedEb(
    Qt3DRender::QObjectPickerPrivate *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  void Qt3DRender::QObjectPickerPrivate::setContainsMouse(bool
//      containsMouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QObjectPickerPrivate16setContainsMouseEb(
    Qt3DRender::QObjectPickerPrivate *self,
    bool containsMouse) {
  self->setContainsMouse(containsMouse);
}

//  a Python function taken by a CuteQt3DRender_QObjectPickerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QObjectPickerPrivate(
    Qt3DRender::QObjectPickerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QObjectPickerPrivate *>(self)->take(key, call);
}
