//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/abstractactioninput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/abstractactioninput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/abstractactioninput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/abstractactioninput.cpp, line 12, as _ZN9Qt3DInput5Input19AbstractActionInputC1Ev
namespace Qt3DInput::Input {
inline AbstractActionInput::AbstractActionInput()
    : BackendNode()
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  A Qt3DInput::Input::AbstractActionInput that Python can take functions over in. Every Qt3DInput::Input::AbstractActionInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DInput_Input_AbstractActionInputCall0)(const void *, Qt3DInput::Input::InputHandler *, qint64, int *);
typedef void (*CuteQt3DInput_Input_AbstractActionInputCall1)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DInput_Input_AbstractActionInput : public Qt3DInput::Input::AbstractActionInput {
public:
  using Qt3DInput::Input::AbstractActionInput::AbstractActionInput;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9Qt3DInput5Input19AbstractActionInput7processEPNS0_12InputHandlerEx")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DInput::Input::AbstractActionInput::process(InputHandler
  //      *inputHandler, qint64 currentTime)
  bool process(
      Qt3DInput::Input::InputHandler *inputHandler,
      qint64 currentTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_AbstractActionInputCall0 call = reinterpret_cast<CuteQt3DInput_Input_AbstractActionInputCall0>(taken[0]);
      bool given = call(this, inputHandler, currentTime, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DInput::Input::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_Input_AbstractActionInputCall1 call = reinterpret_cast<CuteQt3DInput_Input_AbstractActionInputCall1>(taken[1]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DInput::Input::AbstractActionInput::AbstractActionInput()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AbstractActionInput *ritual_ZN9Qt3DInput5Input19AbstractActionInputC1Ev() {
  return new CuteQt3DInput_Input_AbstractActionInput();
}

//  qint64 Qt3DInput::Input::AbstractActionInput::milliToNano(qint64 milli)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9Qt3DInput5Input19AbstractActionInput11milliToNanoEx(
    qint64 milli) {
  return Qt3DInput::Input::AbstractActionInput::milliToNano(milli);
}

//  bool Qt3DInput::Input::AbstractActionInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input19AbstractActionInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::AbstractActionInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  a Python function taken by a CuteQt3DInput_Input_AbstractActionInput, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_AbstractActionInput(
    Qt3DInput::Input::AbstractActionInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_AbstractActionInput *>(self)->take(key, call);
}
