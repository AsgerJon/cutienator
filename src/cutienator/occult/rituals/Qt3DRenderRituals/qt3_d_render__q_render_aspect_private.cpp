//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrenderaspect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrenderaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobjectdefs.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::QRenderAspectPrivate that Python can take functions over in. Every Qt3DRender::QRenderAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall2)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall3)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
class CuteQt3DRender_QRenderAspectPrivate : public Qt3DRender::QRenderAspectPrivate {
public:
  using Qt3DRender::QRenderAspectPrivate::QRenderAspectPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::QRenderAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::jobsDone();
  }

  //  void Qt3DRender::QRenderAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::frameDone();
  }

  //  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall3 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall3>(taken[3]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }
};

//  Qt3DRender::QRenderAspectPrivate::QRenderAspectPrivate(QRenderAspect::Sub
//      missionType submissionType)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspectPrivate *ritual_ZN10Qt3DRender20QRenderAspectPrivateC1ENS_13QRenderAspect14SubmissionTypeE(
    Qt3DRender::QRenderAspect::SubmissionType submissionType) {
  return new CuteQt3DRender_QRenderAspectPrivate(submissionType);
}

//  Qt3DRender::QRenderAspectPrivate::~QRenderAspectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivateD1Ev(
    Qt3DRender::QRenderAspectPrivate *self) {
  delete self;
}

//  QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspect *ritual_ZN10Qt3DRender20QRenderAspectPrivate6q_funcEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  return self->q_func();
}

//  const QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderAspect *ritual_ZNK10Qt3DRender20QRenderAspectPrivate6q_funcEv(
    const Qt3DRender::QRenderAspectPrivate *self) {
  return self->q_func();
}

//  QRenderAspectPrivate
//      *Qt3DRender::QRenderAspectPrivate::findPrivate(Qt3DCore::QAspectEngin
//      e *engine)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspectPrivate *ritual_ZN10Qt3DRender20QRenderAspectPrivate11findPrivateEPN8Qt3DCore13QAspectEngineE(
    Qt3DCore::QAspectEngine *engine) {
  return Qt3DRender::QRenderAspectPrivate::findPrivate(engine);
}

//  QRenderAspectPrivate *Qt3DRender::QRenderAspectPrivate::get(QRenderAspect
//      *q)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspectPrivate *ritual_ZN10Qt3DRender20QRenderAspectPrivate3getEPNS_13QRenderAspectE(
    Qt3DRender::QRenderAspect *q) {
  return Qt3DRender::QRenderAspectPrivate::get(q);
}

//  void Qt3DRender::QRenderAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate8jobsDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->jobsDone();
}

//  void Qt3DRender::QRenderAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate9frameDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->frameDone();
}

//  void Qt3DRender::QRenderAspectPrivate::createNodeManagers()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate18createNodeManagersEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->createNodeManagers();
}

//  void Qt3DRender::QRenderAspectPrivate::onEngineStartup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate15onEngineStartupEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->onEngineStartup();
}

//  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->onEngineAboutToShutdown();
}

//  void Qt3DRender::QRenderAspectPrivate::registerBackendTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate20registerBackendTypesEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->registerBackendTypes();
}

//  void Qt3DRender::QRenderAspectPrivate::unregisterBackendTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate22unregisterBackendTypesEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->unregisterBackendTypes();
}

//  void Qt3DRender::QRenderAspectPrivate::loadSceneImporters()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate18loadSceneImportersEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->loadSceneImporters();
}

//  void Qt3DRender::QRenderAspectPrivate::loadRenderPlugin(const QString
//      &pluginName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate16loadRenderPluginERK7QString(
    Qt3DRender::QRenderAspectPrivate *self,
    const QString *pluginName) {
  self->loadRenderPlugin(*pluginName);
}

//  void Qt3DRender::QRenderAspectPrivate::registerBackendType(const
//      QMetaObject &a0, const Qt3DCore::QBackendNodeMapperPtr &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate19registerBackendTypeERK11QMetaObjectRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DRender::QRenderAspectPrivate *self,
    const QMetaObject *a0,
    const Qt3DCore::QBackendNodeMapperPtr *functor) {
  self->registerBackendType(*a0, *functor);
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DRender::QRenderAspectPrivate::createGeometryRendererJobs() const
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZNK10Qt3DRender20QRenderAspectPrivate26createGeometryRendererJobsEv(
    const Qt3DRender::QRenderAspectPrivate *self) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(
      self->createGeometryRendererJobs());
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DRender::QRenderAspectPrivate::createPreRendererJobs() const
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZNK10Qt3DRender20QRenderAspectPrivate21createPreRendererJobsEv(
    const Qt3DRender::QRenderAspectPrivate *self) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(
      self->createPreRendererJobs());
}

//  Render::AbstractRenderer
//      *Qt3DRender::QRenderAspectPrivate::loadRendererPlugin()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AbstractRenderer *ritual_ZN10Qt3DRender20QRenderAspectPrivate18loadRendererPluginEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  return self->loadRendererPlugin();
}

//  bool Qt3DRender::QRenderAspectPrivate::processMouseEvent(QObject *obj,
//      QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender20QRenderAspectPrivate17processMouseEventEP7QObjectP11QMouseEvent(
    Qt3DRender::QRenderAspectPrivate *self,
    QObject *obj,
    QMouseEvent *event) {
  return self->processMouseEvent(obj, event);
}

//  bool Qt3DRender::QRenderAspectPrivate::processKeyEvent(QObject *obj,
//      QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender20QRenderAspectPrivate15processKeyEventEP7QObjectP9QKeyEvent(
    Qt3DRender::QRenderAspectPrivate *self,
    QObject *obj,
    QKeyEvent *event) {
  return self->processKeyEvent(obj, event);
}

//  void Qt3DRender::QRenderAspectPrivate::configurePlugin(const QString
//      &plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QRenderAspectPrivate15configurePluginERK7QString(
    const QString *plugin) {
  Qt3DRender::QRenderAspectPrivate::configurePlugin(*plugin);
}

//  a Python function taken by a CuteQt3DRender_QRenderAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderAspectPrivate(
    Qt3DRender::QRenderAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderAspectPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QRenderAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate8jobsDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::jobsDone();
}

//  void Qt3DRender::QRenderAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate9frameDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::frameDone();
}

//  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown();
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DRender::QRenderAspectPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRenderAspectPrivate__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
