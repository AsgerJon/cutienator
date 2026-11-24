//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::Input::MouseDevice that Python can take functions over in. Every Qt3DInput::Input::MouseDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef float (*CuteQt3DInput_Input_MouseDeviceCall0)(const void *, int, int *);
typedef bool (*CuteQt3DInput_Input_MouseDeviceCall1)(const void *, int, int *);
typedef void (*CuteQt3DInput_Input_MouseDeviceCall2)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef void (*CuteQt3DInput_Input_MouseDeviceCall3)(const void *, int *);
class CuteQt3DInput_Input_MouseDevice : public Qt3DInput::Input::MouseDevice {
public:
  using Qt3DInput::Input::MouseDevice::MouseDevice;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode9axisValueEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode15isButtonPressedEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  float Qt3DInput::Input::MouseDevice::axisValue(int axisIdentifier)
  //      const
  float axisValue(int axisIdentifier) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_MouseDeviceCall0 call = reinterpret_cast<CuteQt3DInput_Input_MouseDeviceCall0>(taken[0]);
      float given = call(this, axisIdentifier, &handled);
      if (handled) return given;
    }
    return Qt3DInput::Input::MouseDevice::axisValue(axisIdentifier);
  }

  //  bool Qt3DInput::Input::MouseDevice::isButtonPressed(int
  //      buttonIdentifier) const
  bool isButtonPressed(int buttonIdentifier) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_Input_MouseDeviceCall1 call = reinterpret_cast<CuteQt3DInput_Input_MouseDeviceCall1>(taken[1]);
      bool given = call(this, buttonIdentifier, &handled);
      if (handled) return given;
    }
    return Qt3DInput::Input::MouseDevice::isButtonPressed(buttonIdentifier);
  }

  //  void Qt3DInput::Input::MouseDevice::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_Input_MouseDeviceCall2 call = reinterpret_cast<CuteQt3DInput_Input_MouseDeviceCall2>(taken[2]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::MouseDevice::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()
  void cleanup() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_Input_MouseDeviceCall3 call = reinterpret_cast<CuteQt3DInput_Input_MouseDeviceCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup();
  }
};

//  a Python function taken by a CuteQt3DInput_Input_MouseDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_MouseDevice(
    Qt3DInput::Input::MouseDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_MouseDevice *>(self)->take(key, call);
}
