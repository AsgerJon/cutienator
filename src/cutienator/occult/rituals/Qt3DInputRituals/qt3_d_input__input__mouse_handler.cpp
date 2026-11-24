//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::Input::MouseHandler that Python can take functions over in. Every Qt3DInput::Input::MouseHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_Input_MouseHandlerCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DInput_Input_MouseHandler : public Qt3DInput::Input::MouseHandler {
public:
  using Qt3DInput::Input::MouseHandler::MouseHandler;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DInput::Input::MouseHandler::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_MouseHandlerCall0 call = reinterpret_cast<CuteQt3DInput_Input_MouseHandlerCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::MouseHandler::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  a Python function taken by a CuteQt3DInput_Input_MouseHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_MouseHandler(
    Qt3DInput::Input::MouseHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_MouseHandler *>(self)->take(key, call);
}
