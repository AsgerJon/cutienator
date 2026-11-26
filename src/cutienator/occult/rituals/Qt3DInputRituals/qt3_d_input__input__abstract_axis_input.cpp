//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/abstractaxisinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/abstractaxisinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qabstractaxisinput.h>
#include <Qt3DInput/private/qabstractaxisinput_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/abstractaxisinput_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputdeviceintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 30, as _ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AbstractAxisInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAbstractAxisInput *node = qobject_cast<const QAbstractAxisInput *>(frontEnd);
    if (!node)
        return;

    m_sourceDevice = Qt3DCore::qIdForNode(node->sourceDevice());
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 24, as _ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv
namespace Qt3DInput::Input {
inline void AbstractAxisInput::cleanup()
{
    QBackendNode::setEnabled(false);
    m_sourceDevice = Qt3DCore::QNodeId();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 19, as _ZN9Qt3DInput5Input17AbstractAxisInputC1Ev
namespace Qt3DInput::Input {
inline AbstractAxisInput::AbstractAxisInput()
    : BackendNode()
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  A Qt3DInput::Input::AbstractAxisInput that Python can take functions over in. Every Qt3DInput::Input::AbstractAxisInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_Input_AbstractAxisInputCall0)(const void *, int *);
typedef void (*CuteQt3DInput_Input_AbstractAxisInputCall1)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef float (*CuteQt3DInput_Input_AbstractAxisInputCall2)(const void *, Qt3DInput::Input::InputHandler *, qint64, int *);
class CuteQt3DInput_Input_AbstractAxisInput : public Qt3DInput::Input::AbstractAxisInput {
public:
  using Qt3DInput::Input::AbstractAxisInput::AbstractAxisInput;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9Qt3DInput5Input17AbstractAxisInput7processEPNS0_12InputHandlerEx")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DInput::Input::AbstractAxisInput::cleanup()
  void cleanup() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_AbstractAxisInputCall0 call = reinterpret_cast<CuteQt3DInput_Input_AbstractAxisInputCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::AbstractAxisInput::cleanup();
  }

  //  void Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_Input_AbstractAxisInputCall1 call = reinterpret_cast<CuteQt3DInput_Input_AbstractAxisInputCall1>(taken[1]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  float Qt3DInput::Input::AbstractAxisInput::process(InputHandler
  //      *inputHandler, qint64 currentTime)
  float process(
      Qt3DInput::Input::InputHandler *inputHandler,
      qint64 currentTime) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_Input_AbstractAxisInputCall2 call = reinterpret_cast<CuteQt3DInput_Input_AbstractAxisInputCall2>(taken[2]);
      float given = call(this, inputHandler, currentTime, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  void Qt3DInput::Input::AbstractAxisInput::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv(
    Qt3DInput::Input::AbstractAxisInput *self) {
  self->cleanup();
}

//  Qt3DCore::QNodeId Qt3DInput::Input::AbstractAxisInput::sourceDevice()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input17AbstractAxisInput12sourceDeviceEv(
    const Qt3DInput::Input::AbstractAxisInput *self) {
  return new Qt3DCore::QNodeId(self->sourceDevice());
}

//  void Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AbstractAxisInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  float Qt3DInput::Input::AbstractAxisInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
float ritual_ZN9Qt3DInput5Input17AbstractAxisInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::AbstractAxisInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  Qt3DInput::Input::AbstractAxisInput::AbstractAxisInput()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AbstractAxisInput *ritual_ZN9Qt3DInput5Input17AbstractAxisInputC1Ev() {
  return new CuteQt3DInput_Input_AbstractAxisInput();
}

//  a Python function taken by a CuteQt3DInput_Input_AbstractAxisInput, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_AbstractAxisInput(
    Qt3DInput::Input::AbstractAxisInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_AbstractAxisInput *>(self)->take(key, call);
}

//  void Qt3DInput::Input::AbstractAxisInput::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv(
    Qt3DInput::Input::AbstractAxisInput *self) {
  self->Qt3DInput::Input::AbstractAxisInput::cleanup();
}

//  void Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AbstractAxisInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::AbstractAxisInput::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
