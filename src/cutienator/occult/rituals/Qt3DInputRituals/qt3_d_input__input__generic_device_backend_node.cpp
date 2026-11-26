//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/genericdevicebackendnode_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qgenericinputdevice_p.h>
#include <Qt3DInput/private/qabstractphysicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 28, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QGenericInputDevice *node = qobject_cast<const Qt3DInput::QGenericInputDevice *>(frontEnd);
    if (!node)
        return;

    auto *d = static_cast<Qt3DInput::QAbstractPhysicalDevicePrivate *>( Qt3DCore::QNodePrivate::get(const_cast<Qt3DCore::QNode *>(frontEnd)) );

    {
        const QMutexLocker lock(&m_mutex);
        for (const auto &val: std::as_const(d->m_pendingAxisEvents))
            m_axesValues[val.first] = val.second;
        for (const auto &val: std::as_const(d->m_pendingButtonsEvents))
            m_buttonsValues[val.first] = val.second;

        d->m_pendingAxisEvents.clear();
        d->m_pendingButtonsEvents.clear();
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 49, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::cleanup()
{
    const QMutexLocker lock(&m_mutex);
    m_axesValues.clear();
    m_buttonsValues.clear();
    QAbstractPhysicalDeviceBackendNode::cleanup();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 63, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool GenericDeviceBackendNode::isButtonPressed(int buttonIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_buttonsValues[buttonIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 57, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi
namespace Qt3DInput::Input {
inline float GenericDeviceBackendNode::axisValue(int axisIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_axesValues[axisIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 18, as _ZN9Qt3DInput5Input24GenericDeviceBackendNodeC1EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DInput::Input {
inline GenericDeviceBackendNode::GenericDeviceBackendNode(QBackendNode::Mode mode)
    : QAbstractPhysicalDeviceBackendNode(mode)
    , m_mutex()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 24, as _ZN9Qt3DInput5Input24GenericDeviceBackendNodeD1Ev
namespace Qt3DInput::Input {
inline GenericDeviceBackendNode::~GenericDeviceBackendNode()
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

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

//  Qt3DInput::Input::GenericDeviceBackendNode::GenericDeviceBackendNode(QBac
//      kendNode::Mode mode)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::GenericDeviceBackendNode *ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNodeC1EN8Qt3DCore12QBackendNode4ModeE(
    Qt3DCore::QBackendNode::Mode mode) {
  return new CuteQt3DInput_Input_GenericDeviceBackendNode(mode);
}

//  Qt3DInput::Input::GenericDeviceBackendNode::~GenericDeviceBackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNodeD1Ev(
    Qt3DInput::Input::GenericDeviceBackendNode *self) {
  delete self;
}

//  void Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::GenericDeviceBackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::GenericDeviceBackendNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv(
    Qt3DInput::Input::GenericDeviceBackendNode *self) {
  self->cleanup();
}

//  float Qt3DInput::Input::GenericDeviceBackendNode::axisValue(int
//      axisIdentifier) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi(
    const Qt3DInput::Input::GenericDeviceBackendNode *self,
    int axisIdentifier) {
  return self->axisValue(axisIdentifier);
}

//  bool Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(int
//      buttonIdentifier) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPressedEi(
    const Qt3DInput::Input::GenericDeviceBackendNode *self,
    int buttonIdentifier) {
  return self->isButtonPressed(buttonIdentifier);
}

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

//  void Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::GenericDeviceBackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  void Qt3DInput::Input::GenericDeviceBackendNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv(
    Qt3DInput::Input::GenericDeviceBackendNode *self) {
  self->Qt3DInput::Input::GenericDeviceBackendNode::cleanup();
}

//  float Qt3DInput::Input::GenericDeviceBackendNode::axisValue(int
//      axisIdentifier) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi(
    const Qt3DInput::Input::GenericDeviceBackendNode *self,
    int axisIdentifier) {
  return self->Qt3DInput::Input::GenericDeviceBackendNode::axisValue(
      axisIdentifier);
}

//  bool Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(int
//      buttonIdentifier) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPressedEi(
    const Qt3DInput::Input::GenericDeviceBackendNode *self,
    int buttonIdentifier) {
  return self->Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(
      buttonIdentifier);
}
