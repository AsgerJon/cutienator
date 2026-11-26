//  Written by hand on 2026-11-25 from
//  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Its header does not stand alone: Q_DECLARE_PUBLIC in it names
//  'QAbstractPhysicalDeviceBackendNode', which only the header of that
//  class declares, so that header is included first. Not written: the
//  data members. The class declares no virtual function of its own: the
//  Cute class takes those of Qt3DCore::QBackendNodePrivate.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h>
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p_p.h>
#include <cstring>

//  A Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate that Python can take functions over in. Every Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall0)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall1)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall2)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall3)(const void *, Qt3DCore::QNode *, int *);
class CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivate : public Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate {
public:
  using Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::QAbstractPhysicalDeviceBackendNodePrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNodeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
  void addedToEntity(Qt3DCore::QNode *frontend) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall0>(taken[0]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::addedToEntity(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode
  //      *frontend)
  void removedFromEntity(Qt3DCore::QNode *frontend) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall1>(taken[1]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::removedFromEntity(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::componentAdded(QNode *frontend)
  void componentAdded(Qt3DCore::QNode *frontend) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall2 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall2>(taken[2]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::componentAdded(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode *frontend)
  void componentRemoved(Qt3DCore::QNode *frontend) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall3 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivateCall3>(taken[3]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::componentRemoved(frontend);
  }
};

//  Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::QAbstractPhysicalDeviceBackendNodePrivate(Qt3DCore::QBackendNode::Mode
//      mode)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *ritual_ZN9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivateC1EN8Qt3DCore12QBackendNode4ModeE(
    Qt3DCore::QBackendNode::Mode mode) {
  return new CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivate(mode);
}

//  void
//      Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::addAxisSetting(int
//      axisIdentifier, Qt3DCore::QNodeId axisSettingId)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate14addAxisSettingEiN8Qt3DCore7QNodeIdE(
    Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self,
    int axisIdentifier,
    const Qt3DCore::QNodeId *axisSettingId) {
  self->addAxisSetting(axisIdentifier, *axisSettingId);
}

//  void
//      Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::removeAxisSetting(Qt3DCore::QNodeId
//      axisSettingsId)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate17removeAxisSettingEN8Qt3DCore7QNodeIdE(
    Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self,
    const Qt3DCore::QNodeId *axisSettingsId) {
  self->removeAxisSetting(*axisSettingsId);
}

//  Input::MovingAverage
//      &Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::getOrCreateFilter(int
//      axisIdentifier)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MovingAverage *ritual_ZN9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate17getOrCreateFilterEi(
    Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self,
    int axisIdentifier) {
  return &(self->getOrCreateFilter(axisIdentifier));
}

//  Input::AxisSetting
//      *Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::getAxisSetting(Qt3DCore::QNodeId
//      axisSettingId) const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisSetting *ritual_ZNK9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate14getAxisSettingEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self,
    const Qt3DCore::QNodeId *axisSettingId) {
  return self->getAxisSetting(*axisSettingId);
}

//  QAbstractPhysicalDeviceBackendNode
//      *Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceBackendNode *ritual_ZN9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate6q_funcEv(
    Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self) {
  return self->q_func();
}

//  const QAbstractPhysicalDeviceBackendNode
//      *Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDeviceBackendNode *ritual_ZNK9Qt3DInput41QAbstractPhysicalDeviceBackendNodePrivate6q_funcEv(
    const Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractPhysicalDeviceBackendNodePrivate(
    Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodePrivate *>(self)->take(key, call);
}
