//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qkeyboardhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qkeyboardhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qkeyboardhandler.h>
#include <Qt3DInput/private/qkeyboardhandler_p.h>
#include <Qt3DInput/qkeyboarddevice.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qkeyboardhandler.cpp, line 20, as local:qkeyboardhandler.cpp:SigMap
namespace Qt3DInput {
using namespace Qt3DCore;
namespace {
struct SigMap {
    int key;
    const char *sig;
};
}  // namespace
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qkeyboardhandler.cpp, line 25, as local:qkeyboardhandler.cpp:sigMap
namespace Qt3DInput {
using namespace Qt3DCore;
namespace {
const SigMap sigMap[] = {
    { Qt::Key_Left, "leftPressed" },
    { Qt::Key_Right, "rightPressed" },
    { Qt::Key_Up, "upPressed" },
    { Qt::Key_Down, "downPressed" },
    { Qt::Key_Tab, "tabPressed" },
    { Qt::Key_Backtab, "backtabPressed" },
    { Qt::Key_Asterisk, "asteriskPressed" },
    { Qt::Key_NumberSign, "numberSignPressed" },
    { Qt::Key_Escape, "escapePressed" },
    { Qt::Key_Return, "returnPressed" },
    { Qt::Key_Enter, "enterPressed" },
    { Qt::Key_Delete, "deletePressed" },
    { Qt::Key_Space, "spacePressed" },
    { Qt::Key_Back, "backPressed" },
    { Qt::Key_Cancel, "cancelPressed" },
    { Qt::Key_Select, "selectPressed" },
    { Qt::Key_Yes, "yesPressed" },
    { Qt::Key_No, "noPressed" },
    { Qt::Key_Context1, "context1Pressed" },
    { Qt::Key_Context2, "context2Pressed" },
    { Qt::Key_Context3, "context3Pressed" },
    { Qt::Key_Context4, "context4Pressed" },
    { Qt::Key_Call, "callPressed" },
    { Qt::Key_Hangup, "hangupPressed" },
    { Qt::Key_Flip, "flipPressed" },
    { Qt::Key_Menu, "menuPressed" },
    { Qt::Key_VolumeUp, "volumeUpPressed" },
    { Qt::Key_VolumeDown, "volumeDownPressed" },
    { 0, 0 }
};
}  // namespace
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qkeyboardhandler.cpp, line 74, as _ZN9Qt3DInput23QKeyboardHandlerPrivateC1Ev
namespace Qt3DInput {
using namespace Qt3DCore;
inline QKeyboardHandlerPrivate::QKeyboardHandlerPrivate()
    : QComponentPrivate()
    , m_keyboardDevice(nullptr)
    , m_focus(false)
{
    m_shareable = false;
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qkeyboardhandler.cpp, line 82, as _ZN9Qt3DInput23QKeyboardHandlerPrivateD1Ev
namespace Qt3DInput {
using namespace Qt3DCore;
inline QKeyboardHandlerPrivate::~QKeyboardHandlerPrivate()
{
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QKeyboardHandlerPrivate that Python can take functions over in. Every Qt3DInput::QKeyboardHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QKeyboardHandlerPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QKeyboardHandlerPrivateCall1)(const void *, int *);
class CuteQt3DInput_QKeyboardHandlerPrivate : public Qt3DInput::QKeyboardHandlerPrivate {
public:
  using Qt3DInput::QKeyboardHandlerPrivate::QKeyboardHandlerPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QKeyboardHandlerPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QKeyboardHandlerPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QKeyboardHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QKeyboardHandlerPrivate::QKeyboardHandlerPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardHandlerPrivate *ritual_ZN9Qt3DInput23QKeyboardHandlerPrivateC1Ev() {
  return new CuteQt3DInput_QKeyboardHandlerPrivate();
}

//  Qt3DInput::QKeyboardHandlerPrivate::~QKeyboardHandlerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QKeyboardHandlerPrivateD1Ev(
    Qt3DInput::QKeyboardHandlerPrivate *self) {
  delete self;
}

//  QKeyboardHandler *Qt3DInput::QKeyboardHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardHandler *ritual_ZN9Qt3DInput23QKeyboardHandlerPrivate6q_funcEv(
    Qt3DInput::QKeyboardHandlerPrivate *self) {
  return self->q_func();
}

//  const QKeyboardHandler *Qt3DInput::QKeyboardHandlerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QKeyboardHandler *ritual_ZNK9Qt3DInput23QKeyboardHandlerPrivate6q_funcEv(
    const Qt3DInput::QKeyboardHandlerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QKeyboardHandlerPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QKeyboardHandlerPrivate(
    Qt3DInput::QKeyboardHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QKeyboardHandlerPrivate *>(self)->take(key, call);
}
