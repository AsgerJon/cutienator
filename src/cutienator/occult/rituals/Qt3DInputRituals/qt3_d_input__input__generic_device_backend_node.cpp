//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::Input::GenericDeviceBackendNode that Python can take functions over in. Every Qt3DInput::Input::GenericDeviceBackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_Input_GenericDeviceBackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef void (*CuteQt3DInput_Input_GenericDeviceBackendNodeCall1)(const void *, int *);
typedef float (*CuteQt3DInput_Input_GenericDeviceBackendNodeCall2)(const void *, int, int *);
typedef bool (*CuteQt3DInput_Input_GenericDeviceBackendNodeCall3)(const void *, int, int *);
class CuteQt3DInput_Input_GenericDeviceBackendNode : public Qt3DInput::Input::GenericDeviceBackendNode {
public:
  using Qt3DInput::Input::GenericDeviceBackendNode::GenericDeviceBackendNode;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode9axisValueEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode15isButtonPressedEi")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void
  //      Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(cons
  //      t Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_GenericDeviceBackendNodeCall0 call = reinterpret_cast<CuteQt3DInput_Input_GenericDeviceBackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  void Qt3DInput::Input::GenericDeviceBackendNode::cleanup()
  void cleanup() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_Input_GenericDeviceBackendNodeCall1 call = reinterpret_cast<CuteQt3DInput_Input_GenericDeviceBackendNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::GenericDeviceBackendNode::cleanup();
  }

  //  float Qt3DInput::Input::GenericDeviceBackendNode::axisValue(int
  //      axisIdentifier) const
  float axisValue(int axisIdentifier) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_Input_GenericDeviceBackendNodeCall2 call = reinterpret_cast<CuteQt3DInput_Input_GenericDeviceBackendNodeCall2>(taken[2]);
      float given = call(this, axisIdentifier, &handled);
      if (handled) return given;
    }
    return Qt3DInput::Input::GenericDeviceBackendNode::axisValue(axisIdentifier);
  }

  //  bool Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(int
  //      buttonIdentifier) const
  bool isButtonPressed(int buttonIdentifier) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_Input_GenericDeviceBackendNodeCall3 call = reinterpret_cast<CuteQt3DInput_Input_GenericDeviceBackendNodeCall3>(taken[3]);
      bool given = call(this, buttonIdentifier, &handled);
      if (handled) return given;
    }
    return Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(buttonIdentifier);
  }
};

//  a Python function taken by a
//      CuteQt3DInput_Input_GenericDeviceBackendNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_GenericDeviceBackendNode(
    Qt3DInput::Input::GenericDeviceBackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_GenericDeviceBackendNode *>(self)->take(key, call);
}
