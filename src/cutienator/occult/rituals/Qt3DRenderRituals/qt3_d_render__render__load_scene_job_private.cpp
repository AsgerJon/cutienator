//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/loadscenejob_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/scenemanager_p.h>
#include <QtCore/QCoreApplication>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <Qt3DRender/private/job_common_p.h>
#include <Qt3DRender/private/qsceneimporter_p.h>
#include <Qt3DRender/qsceneloader.h>
#include <Qt3DRender/private/qsceneloader_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <QtCore/QFileInfo>
#if QT_CONFIG(mimetype)
#include <QtCore/QMimeDatabase>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/jobs/loadscenejob.cpp, line 154, as _ZN10Qt3DRender6Render19LoadSceneJobPrivate9postFrameEPN8Qt3DCore14QAspectManagerE
namespace Qt3DRender::Render {
inline void LoadSceneJobPrivate::postFrame(Qt3DCore::QAspectManager *manager)
{
    Q_Q(LoadSceneJob);
    QSceneLoader *node =
            qobject_cast<QSceneLoader *>(manager->lookupNode(q->sceneComponentId()));
    if (!node)
        return;
    Qt3DRender::QSceneLoaderPrivate *dNode =
            static_cast<decltype(dNode)>(Qt3DCore::QNodePrivate::get(node));

    // If the sceneSubTree is null it will trigger the frontend to unload
    // any subtree it may hold
    // Set clone of sceneTree in sceneComponent. This will move the sceneSubTree
    // to the QCoreApplication thread which is where the frontend object tree lives.
    dNode->setSceneRoot(m_sceneSubtree.release());

    // Note: the status is set after the subtree so that bindinds depending on the status
    // in the frontend will be consistent
    dNode->setStatus(m_status);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  A Qt3DRender::Render::LoadSceneJobPrivate that Python can take functions over in. Every Qt3DRender::Render::LoadSceneJobPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_LoadSceneJobPrivateCall0)(const void *, Qt3DCore::QAspectManager *, int *);
typedef bool (*CuteQt3DRender_Render_LoadSceneJobPrivateCall1)(const void *, int *);
class CuteQt3DRender_Render_LoadSceneJobPrivate : public Qt3DRender::Render::LoadSceneJobPrivate {
public:
  using Qt3DRender::Render::LoadSceneJobPrivate::LoadSceneJobPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::QAs
  //      pectManager *manager)
  void postFrame(Qt3DCore::QAspectManager *manager) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadSceneJobPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_LoadSceneJobPrivateCall0>(taken[0]);
      call(this, manager, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::LoadSceneJobPrivate::postFrame(manager);
  }

  //  bool Qt3DCore::QAspectJobPrivate::isRequired() const
  bool isRequired() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadSceneJobPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_LoadSceneJobPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJobPrivate::isRequired();
  }
};

//  Qt3DRender::Render::LoadSceneJobPrivate::LoadSceneJobPrivate(LoadSceneJob
//      *q)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LoadSceneJobPrivate *ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivateC1EPNS0_12LoadSceneJobE(
    Qt3DRender::Render::LoadSceneJob *q) {
  return new CuteQt3DRender_Render_LoadSceneJobPrivate(q);
}

//  Qt3DRender::Render::LoadSceneJobPrivate::~LoadSceneJobPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivateD1Ev(
    Qt3DRender::Render::LoadSceneJobPrivate *self) {
  delete self;
}

//  void Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::QAspect
//      Manager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivate9postFrameEPN8Qt3DCore14QAspectManagerE(
    Qt3DRender::Render::LoadSceneJobPrivate *self,
    Qt3DCore::QAspectManager *manager) {
  self->postFrame(manager);
}

//  LoadSceneJob *Qt3DRender::Render::LoadSceneJobPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LoadSceneJob *ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivate6q_funcEv(
    Qt3DRender::Render::LoadSceneJobPrivate *self) {
  return self->q_func();
}

//  const LoadSceneJob *Qt3DRender::Render::LoadSceneJobPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::LoadSceneJob *ritual_ZNK10Qt3DRender6Render19LoadSceneJobPrivate6q_funcEv(
    const Qt3DRender::Render::LoadSceneJobPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_Render_LoadSceneJobPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_LoadSceneJobPrivate(
    Qt3DRender::Render::LoadSceneJobPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_LoadSceneJobPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::QAspect
//      Manager *manager)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render19LoadSceneJobPrivate9postFrameEPN8Qt3DCore14QAspectManagerE(
    Qt3DRender::Render::LoadSceneJobPrivate *self,
    Qt3DCore::QAspectManager *manager) {
  self->Qt3DRender::Render::LoadSceneJobPrivate::postFrame(manager);
}
