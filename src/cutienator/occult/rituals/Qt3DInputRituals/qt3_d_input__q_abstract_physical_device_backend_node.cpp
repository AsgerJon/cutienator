//  Written by dev_tooling.RitualGenerator from the records of Qt3DInput/6.12
//  .0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QAbstractPhysicalDeviceBackendNode that Python can take functions over in. Every Qt3DInput::QAbstractPhysicalDeviceBackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall0)(const void *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall1)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef float (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall2)(const void *, int, int *);
typedef bool (*CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall3)(const void *, int, int *);
class CuteQt3DInput_QAbstractPhysicalDeviceBackendNode : public Qt3DInput::QAbstractPhysicalDeviceBackendNode {
public:
  using Qt3DInput::QAbstractPhysicalDeviceBackendNode::QAbstractPhysicalDeviceBackendNode;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
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

  //  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()
  void cleanup() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup();
  }

  //  void
  //      Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(c
  //      onst Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall1>(taken[1]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  float Qt3DInput::QAbstractPhysicalDeviceBackendNode::axisValue(int
  //      axisIdentifier) const
  float axisValue(int axisIdentifier) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall2 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall2>(taken[2]);
      float given = call(this, axisIdentifier, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool
  //      Qt3DInput::QAbstractPhysicalDeviceBackendNode::isButtonPressed(in
  //      t buttonIdentifier) const
  bool isButtonPressed(int buttonIdentifier) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall3 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNodeCall3>(taken[3]);
      bool given = call(this, buttonIdentifier, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv(
    Qt3DInput::QAbstractPhysicalDeviceBackendNode *self) {
  self->cleanup();
}

//  float Qt3DInput::QAbstractPhysicalDeviceBackendNode::axisValue(int
//      axisIdentifier) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode9axisValueEi(
    const Qt3DInput::QAbstractPhysicalDeviceBackendNode *self,
    int axisIdentifier) {
  return self->axisValue(axisIdentifier);
}

//  bool Qt3DInput::QAbstractPhysicalDeviceBackendNode::isButtonPressed(int
//      buttonIdentifier) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode15isButtonPressedEi(
    const Qt3DInput::QAbstractPhysicalDeviceBackendNode *self,
    int buttonIdentifier) {
  return self->isButtonPressed(buttonIdentifier);
}

//  QAbstractPhysicalDeviceBackendNodePrivate
//      *Qt3DInput::QAbstractPhysicalDeviceBackendNode::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode6d_funcEv(
    Qt3DInput::QAbstractPhysicalDeviceBackendNode *self) {
  return self->d_func();
}

//  const QAbstractPhysicalDeviceBackendNodePrivate
//      *Qt3DInput::QAbstractPhysicalDeviceBackendNode::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate *ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode6d_funcEv(
    const Qt3DInput::QAbstractPhysicalDeviceBackendNode *self) {
  return self->d_func();
}

//  a Python function taken by a
//      CuteQt3DInput_QAbstractPhysicalDeviceBackendNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractPhysicalDeviceBackendNode(
    Qt3DInput::QAbstractPhysicalDeviceBackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractPhysicalDeviceBackendNode *>(self)->take(key, call);
}

//  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv(
    Qt3DInput::QAbstractPhysicalDeviceBackendNode *self) {
  self->Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup();
}

//  void
//      Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::QAbstractPhysicalDeviceBackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
