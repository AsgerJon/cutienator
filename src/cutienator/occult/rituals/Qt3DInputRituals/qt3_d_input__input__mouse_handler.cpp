//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/mousehandler_p.h>
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 22, as _ZN9Qt3DInput5Input12MouseHandlerC1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandler::MouseHandler()
    : BackendNode(ReadWrite)
    , m_inputHandler(nullptr)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 28, as _ZN9Qt3DInput5Input12MouseHandlerD1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandler::~MouseHandler()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 32, as _ZNK9Qt3DInput5Input12MouseHandler11mouseDeviceEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline Qt3DCore::QNodeId MouseHandler::mouseDevice() const
{
    return m_mouseDevice;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 37, as _ZN9Qt3DInput5Input12MouseHandler15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 42, as _ZN9Qt3DInput5Input12MouseHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QMouseHandler *node = qobject_cast<const Qt3DInput::QMouseHandler *>(frontEnd);
    if (!node)
        return;

    const auto newId = Qt3DCore::qIdForNode(node->sourceDevice());
    if (m_mouseDevice != newId)
        setDevice(newId);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 54, as _ZN9Qt3DInput5Input12MouseHandler9setDeviceEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::setDevice(Qt3DCore::QNodeId device)
{
    m_mouseDevice = device;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Only a class built on Qt3DInput::Input::MouseHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQt3DInput_Input_MouseHandler : Qt3DInput::Input::MouseHandler {
  using Qt3DInput::Input::MouseHandler::syncFromFrontEnd;
};

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

//  Qt3DInput::Input::MouseHandler::MouseHandler()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseHandler *ritual_ZN9Qt3DInput5Input12MouseHandlerC1Ev() {
  return new CuteQt3DInput_Input_MouseHandler();
}

//  Qt3DInput::Input::MouseHandler::~MouseHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12MouseHandlerD1Ev(
    Qt3DInput::Input::MouseHandler *self) {
  delete self;
}

//  Qt3DCore::QNodeId Qt3DInput::Input::MouseHandler::mouseDevice() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input12MouseHandler11mouseDeviceEv(
    const Qt3DInput::Input::MouseHandler *self) {
  return new Qt3DCore::QNodeId(self->mouseDevice());
}

//  void Qt3DInput::Input::MouseHandler::setInputHandler(InputHandler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12MouseHandler15setInputHandlerEPNS0_12InputHandlerE(
    Qt3DInput::Input::MouseHandler *self,
    Qt3DInput::Input::InputHandler *handler) {
  self->setInputHandler(handler);
}

//  void Qt3DInput::Input::MouseHandler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12MouseHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::MouseHandler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::MouseHandler::setDevice(Qt3DCore::QNodeId device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12MouseHandler9setDeviceEN8Qt3DCore7QNodeIdE(
    Qt3DInput::Input::MouseHandler *self,
    const Qt3DCore::QNodeId *device) {
  self->setDevice(*device);
}

//  a Python function taken by a CuteQt3DInput_Input_MouseHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_MouseHandler(
    Qt3DInput::Input::MouseHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_MouseHandler *>(self)->take(key, call);
}

//  void Qt3DInput::Input::MouseHandler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input12MouseHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::MouseHandler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  static_cast<OwnQt3DInput_Input_MouseHandler *>(self)->OwnQt3DInput_Input_MouseHandler::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
