//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qmousedevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qmousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/private/qmousedevice_p.h>
#include <Qt3DInput/qmouseevent.h>
#include <Qt3DCore/qentity.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qmousedevice.cpp, line 15, as _ZN9Qt3DInput19QMouseDevicePrivateC1Ev
namespace Qt3DInput {
inline QMouseDevicePrivate::QMouseDevicePrivate()
    : QAbstractPhysicalDevicePrivate()
    , m_sensitivity(0.1f)
    , m_updateContinuously(false)
{
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QMouseDevicePrivate that Python can take functions over in. Every Qt3DInput::QMouseDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QMouseDevicePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QMouseDevicePrivateCall1)(const void *, int *);
class CuteQt3DInput_QMouseDevicePrivate : public Qt3DInput::QMouseDevicePrivate {
public:
  using Qt3DInput::QMouseDevicePrivate::QMouseDevicePrivate;
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
      CuteQt3DInput_QMouseDevicePrivateCall0 call = reinterpret_cast<CuteQt3DInput_QMouseDevicePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QMouseDevicePrivateCall1 call = reinterpret_cast<CuteQt3DInput_QMouseDevicePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QMouseDevicePrivate::QMouseDevicePrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseDevicePrivate *ritual_ZN9Qt3DInput19QMouseDevicePrivateC1Ev() {
  return new CuteQt3DInput_QMouseDevicePrivate();
}

//  QMouseDevice *Qt3DInput::QMouseDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseDevice *ritual_ZN9Qt3DInput19QMouseDevicePrivate6q_funcEv(
    Qt3DInput::QMouseDevicePrivate *self) {
  return self->q_func();
}

//  const QMouseDevice *Qt3DInput::QMouseDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QMouseDevice *ritual_ZNK9Qt3DInput19QMouseDevicePrivate6q_funcEv(
    const Qt3DInput::QMouseDevicePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QMouseDevicePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QMouseDevicePrivate(
    Qt3DInput::QMouseDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QMouseDevicePrivate *>(self)->take(key, call);
}
