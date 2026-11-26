//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qmousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 132, as _ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void MouseDevice::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QMouseDevice *node = qobject_cast<const Qt3DInput::QMouseDevice *>(frontEnd);
    if (!node)
        return;

    m_sensitivity = node->sensitivity();
    m_updateAxesContinuously = node->updateAxesContinuously();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 59, as _ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool MouseDevice::isButtonPressed(int buttonIdentifier) const
{
    switch (buttonIdentifier) {
    case QMouseEvent::LeftButton:
        return m_mouseState.leftPressed;
    case QMouseEvent::MiddleButton:
        return m_mouseState.centerPressed;
    case QMouseEvent::RightButton:
        return m_mouseState.rightPressed;
    default:
        break;
    }
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 42, as _ZNK9Qt3DInput5Input11MouseDevice9axisValueEi
namespace Qt3DInput::Input {
inline float MouseDevice::axisValue(int axisIdentifier) const
{
    switch (axisIdentifier) {
    case QMouseDevice::X:
        return m_mouseState.xAxis;
    case QMouseDevice::Y:
        return m_mouseState.yAxis;
    case QMouseDevice::WheelX:
        return m_mouseState.wXAxis;
    case QMouseDevice::WheelY:
        return m_mouseState.wYAxis;
    default:
        break;
    }
    return 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 19, as _ZN9Qt3DInput5Input11MouseDeviceC1Ev
namespace Qt3DInput::Input {
inline MouseDevice::MouseDevice()
    : QAbstractPhysicalDeviceBackendNode(ReadOnly)
    , m_inputHandler(nullptr)
    , m_wasPressed(false)
    , m_sensitivity(0.1f)
    , m_updateAxesContinuously(false)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 28, as _ZN9Qt3DInput5Input11MouseDeviceD1Ev
namespace Qt3DInput::Input {
inline MouseDevice::~MouseDevice()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 32, as _ZN9Qt3DInput5Input11MouseDevice15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline void MouseDevice::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 37, as _ZNK9Qt3DInput5Input11MouseDevice12inputHandlerEv
namespace Qt3DInput::Input {
inline InputHandler *MouseDevice::inputHandler() const
{
    return m_inputHandler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 121, as _ZN9Qt3DInput5Input11MouseDevice19resetMouseAxisStateEv
namespace Qt3DInput::Input {
inline void MouseDevice::resetMouseAxisState()
{
    // Reset axis values before we accumulate new values for this frame
    m_mouseState.xAxis = 0.0f;
    m_mouseState.yAxis = 0.0f;
#if QT_CONFIG(wheelevent)
    m_mouseState.wXAxis = 0.0f;
    m_mouseState.wYAxis = 0.0f;
#endif
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 74, as _ZNK9Qt3DInput5Input11MouseDevice10mouseStateEv
namespace Qt3DInput::Input {
inline MouseDevice::MouseState MouseDevice::mouseState() const
{
    return m_mouseState;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 79, as _ZNK9Qt3DInput5Input11MouseDevice11previousPosEv
namespace Qt3DInput::Input {
inline QPointF MouseDevice::previousPos() const
{
    return m_previousPos;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 84, as _ZNK9Qt3DInput5Input11MouseDevice10wasPressedEv
namespace Qt3DInput::Input {
inline bool MouseDevice::wasPressed() const
{
    return m_wasPressed;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 89, as _ZNK9Qt3DInput5Input11MouseDevice11sensitivityEv
namespace Qt3DInput::Input {
inline float MouseDevice::sensitivity() const
{
    return m_sensitivity;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 94, as _ZNK9Qt3DInput5Input11MouseDevice22updateAxesContinuouslyEv
namespace Qt3DInput::Input {
inline bool MouseDevice::updateAxesContinuously() const
{
    return m_updateAxesContinuously;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

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

//  Qt3DInput::Input::MouseDevice::MouseDevice()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseDevice *ritual_ZN9Qt3DInput5Input11MouseDeviceC1Ev() {
  return new CuteQt3DInput_Input_MouseDevice();
}

//  Qt3DInput::Input::MouseDevice::~MouseDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11MouseDeviceD1Ev(
    Qt3DInput::Input::MouseDevice *self) {
  delete self;
}

//  void Qt3DInput::Input::MouseDevice::setInputHandler(InputHandler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11MouseDevice15setInputHandlerEPNS0_12InputHandlerE(
    Qt3DInput::Input::MouseDevice *self,
    Qt3DInput::Input::InputHandler *handler) {
  self->setInputHandler(handler);
}

//  InputHandler *Qt3DInput::Input::MouseDevice::inputHandler() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputHandler *ritual_ZNK9Qt3DInput5Input11MouseDevice12inputHandlerEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return self->inputHandler();
}

//  float Qt3DInput::Input::MouseDevice::axisValue(int axisIdentifier) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input11MouseDevice9axisValueEi(
    const Qt3DInput::Input::MouseDevice *self,
    int axisIdentifier) {
  return self->axisValue(axisIdentifier);
}

//  bool Qt3DInput::Input::MouseDevice::isButtonPressed(int buttonIdentifier)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi(
    const Qt3DInput::Input::MouseDevice *self,
    int buttonIdentifier) {
  return self->isButtonPressed(buttonIdentifier);
}

//  void Qt3DInput::Input::MouseDevice::resetMouseAxisState()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11MouseDevice19resetMouseAxisStateEv(
    Qt3DInput::Input::MouseDevice *self) {
  self->resetMouseAxisState();
}

//  MouseState Qt3DInput::Input::MouseDevice::mouseState() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseDevice::MouseState *ritual_ZNK9Qt3DInput5Input11MouseDevice10mouseStateEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return new Qt3DInput::Input::MouseDevice::MouseState(self->mouseState());
}

//  QPointF Qt3DInput::Input::MouseDevice::previousPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9Qt3DInput5Input11MouseDevice11previousPosEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return new QPointF(self->previousPos());
}

//  bool Qt3DInput::Input::MouseDevice::wasPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input11MouseDevice10wasPressedEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return self->wasPressed();
}

//  float Qt3DInput::Input::MouseDevice::sensitivity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input11MouseDevice11sensitivityEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return self->sensitivity();
}

//  bool Qt3DInput::Input::MouseDevice::updateAxesContinuously() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input11MouseDevice22updateAxesContinuouslyEv(
    const Qt3DInput::Input::MouseDevice *self) {
  return self->updateAxesContinuously();
}

//  void Qt3DInput::Input::MouseDevice::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::MouseDevice *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  a Python function taken by a CuteQt3DInput_Input_MouseDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_MouseDevice(
    Qt3DInput::Input::MouseDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_MouseDevice *>(self)->take(key, call);
}

//  float Qt3DInput::Input::MouseDevice::axisValue(int axisIdentifier) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK9Qt3DInput5Input11MouseDevice9axisValueEi(
    const Qt3DInput::Input::MouseDevice *self,
    int axisIdentifier) {
  return self->Qt3DInput::Input::MouseDevice::axisValue(axisIdentifier);
}

//  bool Qt3DInput::Input::MouseDevice::isButtonPressed(int buttonIdentifier)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi(
    const Qt3DInput::Input::MouseDevice *self,
    int buttonIdentifier) {
  return self->Qt3DInput::Input::MouseDevice::isButtonPressed(
      buttonIdentifier);
}

//  void Qt3DInput::Input::MouseDevice::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::MouseDevice *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::MouseDevice::syncFromFrontEnd(frontEnd, firstTime);
}
