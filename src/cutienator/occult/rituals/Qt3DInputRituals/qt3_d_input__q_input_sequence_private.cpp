//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputsequence_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputsequence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qinputsequence.h>
#include <Qt3DInput/private/qinputsequence_p.h>
#include <Qt3DInput/qabstractactioninput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DCore/private/qnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qinputsequence.cpp, line 15, as _ZN9Qt3DInput21QInputSequencePrivateC1Ev
namespace Qt3DInput {
inline QInputSequencePrivate::QInputSequencePrivate()
    : QAbstractActionInputPrivate(),
      m_timeout(0),
      m_buttonInterval(0)
{
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QInputSequencePrivate that Python can take functions over in. Every Qt3DInput::QInputSequencePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QInputSequencePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QInputSequencePrivateCall1)(const void *, int *);
class CuteQt3DInput_QInputSequencePrivate : public Qt3DInput::QInputSequencePrivate {
public:
  using Qt3DInput::QInputSequencePrivate::QInputSequencePrivate;
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
      CuteQt3DInput_QInputSequencePrivateCall0 call = reinterpret_cast<CuteQt3DInput_QInputSequencePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QInputSequencePrivateCall1 call = reinterpret_cast<CuteQt3DInput_QInputSequencePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QInputSequencePrivate::QInputSequencePrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputSequencePrivate *ritual_ZN9Qt3DInput21QInputSequencePrivateC1Ev() {
  return new CuteQt3DInput_QInputSequencePrivate();
}

//  a Python function taken by a CuteQt3DInput_QInputSequencePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputSequencePrivate(
    Qt3DInput::QInputSequencePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputSequencePrivate *>(self)->take(key, call);
}
