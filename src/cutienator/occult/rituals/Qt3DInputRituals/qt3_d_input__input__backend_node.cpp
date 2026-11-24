//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/backendnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/backendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::Input::BackendNode that Python can take functions over in. Every Qt3DInput::Input::BackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_Input_BackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DInput_Input_BackendNode : public Qt3DInput::Input::BackendNode {
public:
  using Qt3DInput::Input::BackendNode::BackendNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DInput::Input::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_BackendNodeCall0 call = reinterpret_cast<CuteQt3DInput_Input_BackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  a Python function taken by a CuteQt3DInput_Input_BackendNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_BackendNode(
    Qt3DInput::Input::BackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_BackendNode *>(self)->take(key, call);
}

//  void Qt3DInput::Input::BackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::BackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
}
