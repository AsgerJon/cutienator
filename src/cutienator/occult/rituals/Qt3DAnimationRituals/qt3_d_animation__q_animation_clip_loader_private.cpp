//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationcliploader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationcliploader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qabstractanimationclip.h>
#include <Qt3DAnimation/private/qabstractanimationclip_p.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qabstractanimationclip.cpp, line 11, as _ZN13Qt3DAnimation29QAbstractAnimationClipPrivateC2Ev
namespace Qt3DAnimation {
inline QAbstractAnimationClipPrivate::QAbstractAnimationClipPrivate()
    : Qt3DCore::QNodePrivate()
    , m_duration(0.0f)
{
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcliploader.cpp, line 11, as _ZN13Qt3DAnimation27QAnimationClipLoaderPrivateC1Ev
namespace Qt3DAnimation {
inline QAnimationClipLoaderPrivate::QAnimationClipLoaderPrivate()
    : QAbstractAnimationClipPrivate()
    , m_source()
    , m_status(QAnimationClipLoader::NotReady)
{
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcliploader.cpp, line 18, as _ZN13Qt3DAnimation27QAnimationClipLoaderPrivate9setStatusENS_20QAnimationClipLoader6StatusE
namespace Qt3DAnimation {
inline void QAnimationClipLoaderPrivate::setStatus(QAnimationClipLoader::Status status)
{
    Q_Q(QAnimationClipLoader);
    if (status != m_status) {
        m_status = status;
        const bool blocked = q->blockNotifications(true);
        emit q->statusChanged(m_status);
        q->blockNotifications(blocked);
    }
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::QAnimationClipLoaderPrivate that Python can take functions over in. Every Qt3DAnimation::QAnimationClipLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAnimationClipLoaderPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DAnimation_QAnimationClipLoaderPrivateCall1)(const void *, int *);
class CuteQt3DAnimation_QAnimationClipLoaderPrivate : public Qt3DAnimation::QAnimationClipLoaderPrivate {
public:
  using Qt3DAnimation::QAnimationClipLoaderPrivate::QAnimationClipLoaderPrivate;
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
      CuteQt3DAnimation_QAnimationClipLoaderPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QAnimationClipLoaderPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationClipLoaderPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QAnimationClipLoaderPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DAnimation::QAnimationClipLoaderPrivate::QAnimationClipLoaderPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipLoaderPrivate *ritual_ZN13Qt3DAnimation27QAnimationClipLoaderPrivateC1Ev() {
  return new CuteQt3DAnimation_QAnimationClipLoaderPrivate();
}

//  void Qt3DAnimation::QAnimationClipLoaderPrivate::setStatus(QAnimationClip
//      Loader::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation27QAnimationClipLoaderPrivate9setStatusENS_20QAnimationClipLoader6StatusE(
    Qt3DAnimation::QAnimationClipLoaderPrivate *self,
    Qt3DAnimation::QAnimationClipLoader::Status status) {
  self->setStatus(status);
}

//  QAnimationClipLoader
//      *Qt3DAnimation::QAnimationClipLoaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipLoader *ritual_ZN13Qt3DAnimation27QAnimationClipLoaderPrivate6q_funcEv(
    Qt3DAnimation::QAnimationClipLoaderPrivate *self) {
  return self->q_func();
}

//  const QAnimationClipLoader
//      *Qt3DAnimation::QAnimationClipLoaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationClipLoader *ritual_ZNK13Qt3DAnimation27QAnimationClipLoaderPrivate6q_funcEv(
    const Qt3DAnimation::QAnimationClipLoaderPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DAnimation_QAnimationClipLoaderPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAnimationClipLoaderPrivate(
    Qt3DAnimation::QAnimationClipLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAnimationClipLoaderPrivate *>(self)->take(key, call);
}
