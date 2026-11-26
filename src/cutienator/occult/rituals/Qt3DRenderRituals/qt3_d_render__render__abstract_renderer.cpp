//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/abstractrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/abstractrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QSharedPointer>

//  A Qt3DRender::Render::AbstractRenderer that Python can take functions over in. Every Qt3DRender::Render::AbstractRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_AbstractRendererCall0)(const void *, int *);
typedef int (*CuteQt3DRender_Render_AbstractRendererCall1)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall2)(const void *, int, int *);
typedef int (*CuteQt3DRender_Render_AbstractRendererCall3)(const void *, int *);
typedef qint64 (*CuteQt3DRender_Render_AbstractRendererCall4)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall5)(const void *, qint64, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall6)(const void *, int, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall7)(const void *, Qt3DRender::QRenderAspect *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall8)(const void *, Qt3DRender::Render::NodeManagers *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall9)(const void *, Qt3DCore::QServiceLocator *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall10)(const void *, bool, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall11)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall12)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall13)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall14)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall15)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall16)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall17)(const void *, bool, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall18)(const void *, int *);
typedef bool (*CuteQt3DRender_Render_AbstractRendererCall19)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall20)(const void *, int, Qt3DRender::Render::BackendNode *, int *);
typedef int (*CuteQt3DRender_Render_AbstractRendererCall21)(const void *, int *);
typedef bool (*CuteQt3DRender_Render_AbstractRendererCall22)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall23)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall24)(const void *, Qt3DCore::QAspectManager *, int *);
typedef bool (*CuteQt3DRender_Render_AbstractRendererCall25)(const void *, QObject *, QMouseEvent *, int *);
typedef bool (*CuteQt3DRender_Render_AbstractRendererCall26)(const void *, QObject *, QKeyEvent *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall27)(const void *, Qt3DRender::Render::Entity *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall28)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall29)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall30)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall31)(const void *, Qt3DRender::Render::RenderSettings *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall32)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall33)(const void *, QOpenGLContext *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall34)(const void *, QRhi *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall35)(const void *, QRhiRenderTarget *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall36)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall37)(const void *, QScreen *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall38)(const void *, int *);
typedef void (*CuteQt3DRender_Render_AbstractRendererCall39)(const void *, Qt3DRender::Render::OffscreenSurfaceHelper *, int *);
typedef const QSurfaceFormat * (*CuteQt3DRender_Render_AbstractRendererCall40)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall41)(const void *, int *);
typedef void * (*CuteQt3DRender_Render_AbstractRendererCall42)(const void *, int *);
class CuteQt3DRender_Render_AbstractRenderer : public Qt3DRender::Render::AbstractRenderer {
public:
  using Qt3DRender::Render::AbstractRenderer::AbstractRenderer;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer8dumpInfoEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer3apiEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer15setRenderDriverENS1_12RenderDriverE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer12renderDriverEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer4timeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer7setTimeEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer18setJobsInLastFrameEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer9setAspectEPNS_13QRenderAspectE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer15setNodeManagersEPNS0_12NodeManagersE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer11setServicesEPN8Qt3DCore15QServiceLocatorE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer17setSurfaceExposedEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer6aspectEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer12nodeManagersEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer8servicesEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer10initializeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer8shutdownEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer24releaseGraphicsResourcesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer6renderEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer22cleanGraphicsResourcesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer9isRunningEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer9markDirtyE6QFlagsINS1_20BackendNodeDirtyFlagEEPNS0_11BackendNodeE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer9dirtyBitsEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer12shouldRenderEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer13skipNextFrameEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer8jobsDoneEPN8Qt3DCore14QAspectManagerE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer17processMouseEventEP7QObjectP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer15processKeyEventEP7QObjectP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer12setSceneRootEPNS0_6EntityE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer9sceneRootEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer14frameGraphRootEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer19frameAdvanceServiceEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer11setSettingsEPNS0_14RenderSettingsE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer8settingsEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer16setOpenGLContextEP14QOpenGLContext")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer13setRHIContextEP4QRhi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer25setDefaultRHIRenderTargetEP16QRhiRenderTarget")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer19setRHICommandBufferEP17QRhiCommandBuffer")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7QScreen")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer25setOffscreenSurfaceHelperEPNS0_22OffscreenSurfaceHelperE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render16AbstractRenderer6formatEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer12shareContextEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render16AbstractRenderer11contextInfoEv")) {
      taken[42] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::AbstractRenderer::dumpInfo() const
  void dumpInfo() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall0 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  API Qt3DRender::Render::AbstractRenderer::api() const
  Qt3DRender::API api() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall1 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::API>(given);
    }
    return {};
  }

  //  void
  //      Qt3DRender::Render::AbstractRenderer::setRenderDriver(RenderDrive
  //      r driver)
  void setRenderDriver(
      Qt3DRender::Render::AbstractRenderer::RenderDriver driver) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall2 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall2>(taken[2]);
      call(this, static_cast<int>(driver), &handled);
      if (handled) return;
    }
  }

  //  RenderDriver Qt3DRender::Render::AbstractRenderer::renderDriver()
  //      const
  Qt3DRender::Render::AbstractRenderer::RenderDriver renderDriver() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall3 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::AbstractRenderer::RenderDriver>(given);
    }
    return {};
  }

  //  qint64 Qt3DRender::Render::AbstractRenderer::time() const
  qint64 time() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall4 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DRender::Render::AbstractRenderer::setTime(qint64 time)
  void setTime(qint64 time) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall5 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall5>(taken[5]);
      call(this, time, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setJobsInLastFrame(int
  //      jobsInLastFrame)
  void setJobsInLastFrame(int jobsInLastFrame) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall6 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall6>(taken[6]);
      call(this, jobsInLastFrame, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setAspect(QRenderAspect
  //      *aspect)
  void setAspect(Qt3DRender::QRenderAspect *aspect) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall7 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall7>(taken[7]);
      call(this, aspect, &handled);
      if (handled) return;
    }
  }

  //  void
  //      Qt3DRender::Render::AbstractRenderer::setNodeManagers(NodeManager
  //      s *managers)
  void setNodeManagers(Qt3DRender::Render::NodeManagers *managers) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall8 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall8>(taken[8]);
      call(this, managers, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setServices(Qt3DCore::QSer
  //      viceLocator *services)
  void setServices(Qt3DCore::QServiceLocator *services) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall9 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall9>(taken[9]);
      call(this, services, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setSurfaceExposed(bool
  //      exposed)
  void setSurfaceExposed(bool exposed) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall10 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall10>(taken[10]);
      call(this, exposed, &handled);
      if (handled) return;
    }
  }

  //  QRenderAspect *Qt3DRender::Render::AbstractRenderer::aspect() const
  Qt3DRender::QRenderAspect *aspect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall11 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::QRenderAspect *>(given);
    }
    return {};
  }

  //  NodeManagers *Qt3DRender::Render::AbstractRenderer::nodeManagers()
  //      const
  Qt3DRender::Render::NodeManagers *nodeManagers() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall12 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::NodeManagers *>(given);
    }
    return {};
  }

  //  Qt3DCore::QServiceLocator
  //      *Qt3DRender::Render::AbstractRenderer::services() const
  Qt3DCore::QServiceLocator *services() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall13 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::QServiceLocator *>(given);
    }
    return {};
  }

  //  void Qt3DRender::Render::AbstractRenderer::initialize()
  void initialize() override {
    if (taken[14]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall14 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::shutdown()
  void shutdown() override {
    if (taken[15]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall15 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::releaseGraphicsResources()
  void releaseGraphicsResources() override {
    if (taken[16]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall16 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::render(bool swapBuffers)
  void render(bool swapBuffers) override {
    if (taken[17]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall17 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall17>(taken[17]);
      call(this, swapBuffers, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::cleanGraphicsResources()
  void cleanGraphicsResources() override {
    if (taken[18]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall18 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool Qt3DRender::Render::AbstractRenderer::isRunning() const
  bool isRunning() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall19 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void
  //      Qt3DRender::Render::AbstractRenderer::markDirty(BackendNodeDirtyS
  //      et changes, BackendNode *node)
  void markDirty(
      Qt3DRender::Render::AbstractRenderer::BackendNodeDirtySet changes,
      Qt3DRender::Render::BackendNode *node) override {
    if (taken[20]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall20 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall20>(taken[20]);
      call(this, static_cast<int>(changes.toInt()), node, &handled);
      if (handled) return;
    }
  }

  //  BackendNodeDirtySet Qt3DRender::Render::AbstractRenderer::dirtyBits()
  Qt3DRender::Render::AbstractRenderer::BackendNodeDirtySet dirtyBits() override {
    if (taken[21]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall21 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt3DRender::Render::AbstractRenderer::BackendNodeDirtyFlag>::fromInt(given);
    }
    return {};
  }

  //  bool Qt3DRender::Render::AbstractRenderer::shouldRender() const
  bool shouldRender() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall22 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DRender::Render::AbstractRenderer::skipNextFrame()
  void skipNextFrame() override {
    if (taken[23]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall23 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::jobsDone(Qt3DCore::QAspect
  //      Manager *manager)
  void jobsDone(Qt3DCore::QAspectManager *manager) override {
    if (taken[24]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall24 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall24>(taken[24]);
      call(this, manager, &handled);
      if (handled) return;
    }
  }

  //  bool Qt3DRender::Render::AbstractRenderer::processMouseEvent(QObject
  //      *object, QMouseEvent *event)
  bool processMouseEvent(QObject *object, QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall25 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall25>(taken[25]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool Qt3DRender::Render::AbstractRenderer::processKeyEvent(QObject
  //      *object, QKeyEvent *event)
  bool processKeyEvent(QObject *object, QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall26 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall26>(taken[26]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DRender::Render::AbstractRenderer::setSceneRoot(Entity *root)
  void setSceneRoot(Qt3DRender::Render::Entity *root) override {
    if (taken[27]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall27 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall27>(taken[27]);
      call(this, root, &handled);
      if (handled) return;
    }
  }

  //  Entity *Qt3DRender::Render::AbstractRenderer::sceneRoot() const
  Qt3DRender::Render::Entity *sceneRoot() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall28 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::Entity *>(given);
    }
    return {};
  }

  //  FrameGraphNode
  //      *Qt3DRender::Render::AbstractRenderer::frameGraphRoot() const
  Qt3DRender::Render::FrameGraphNode *frameGraphRoot() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall29 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::FrameGraphNode *>(given);
    }
    return {};
  }

  //  Qt3DCore::QAbstractFrameAdvanceService
  //      *Qt3DRender::Render::AbstractRenderer::frameAdvanceService()
  //      const
  Qt3DCore::QAbstractFrameAdvanceService *frameAdvanceService() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall30 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::QAbstractFrameAdvanceService *>(given);
    }
    return {};
  }

  //  void Qt3DRender::Render::AbstractRenderer::setSettings(RenderSettings
  //      *settings)
  void setSettings(Qt3DRender::Render::RenderSettings *settings) override {
    if (taken[31]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall31 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall31>(taken[31]);
      call(this, settings, &handled);
      if (handled) return;
    }
  }

  //  RenderSettings *Qt3DRender::Render::AbstractRenderer::settings()
  //      const
  Qt3DRender::Render::RenderSettings *settings() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall32 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::RenderSettings *>(given);
    }
    return {};
  }

  //  void
  //      Qt3DRender::Render::AbstractRenderer::setOpenGLContext(QOpenGLCon
  //      text *ctx)
  void setOpenGLContext(QOpenGLContext *ctx) override {
    if (taken[33]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall33 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall33>(taken[33]);
      call(this, ctx, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setRHIContext(QRhi *ctx)
  void setRHIContext(QRhi *ctx) override {
    if (taken[34]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall34 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall34>(taken[34]);
      call(this, ctx, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setDefaultRHIRenderTarget(
  //      QRhiRenderTarget *defaultTarget)
  void setDefaultRHIRenderTarget(QRhiRenderTarget *defaultTarget) override {
    if (taken[35]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall35 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall35>(taken[35]);
      call(this, defaultTarget, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setRHICommandBuffer(QRhiCo
  //      mmandBuffer *commandBuffer)
  void setRHICommandBuffer(QRhiCommandBuffer *commandBuffer) override {
    if (taken[36]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall36 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall36>(taken[36]);
      call(this, commandBuffer, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DRender::Render::AbstractRenderer::setScreen(QScreen *a0)
  void setScreen(QScreen *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall37 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::AbstractRenderer::setScreen(a0);
  }

  //  QScreen *Qt3DRender::Render::AbstractRenderer::screen() const
  QScreen *screen() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall38 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QScreen *>(given);
    }
    return Qt3DRender::Render::AbstractRenderer::screen();
  }

  //  void Qt3DRender::Render::AbstractRenderer::setOffscreenSurfaceHelper(
  //      OffscreenSurfaceHelper *helper)
  void setOffscreenSurfaceHelper(
      Qt3DRender::Render::OffscreenSurfaceHelper *helper) override {
    if (taken[39]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall39 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall39>(taken[39]);
      call(this, helper, &handled);
      if (handled) return;
    }
  }

  //  QSurfaceFormat Qt3DRender::Render::AbstractRenderer::format()
  QSurfaceFormat format() override {
    if (taken[40]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall40 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall40>(taken[40]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QOpenGLContext *Qt3DRender::Render::AbstractRenderer::shareContext()
  //      const
  QOpenGLContext *shareContext() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall41 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QOpenGLContext *>(given);
    }
    return {};
  }

  //  const GraphicsApiFilterData
  //      *Qt3DRender::Render::AbstractRenderer::contextInfo() const
  const Qt3DRender::GraphicsApiFilterData *contextInfo() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQt3DRender_Render_AbstractRendererCall42 call = reinterpret_cast<CuteQt3DRender_Render_AbstractRendererCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const Qt3DRender::GraphicsApiFilterData *>(given);
    }
    return {};
  }
};

//  Qt3DRender::Render::AbstractRenderer::~AbstractRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRendererD1Ev(
    Qt3DRender::Render::AbstractRenderer *self) {
  delete self;
}

//  void Qt3DRender::Render::AbstractRenderer::dumpInfo() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render16AbstractRenderer8dumpInfoEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  self->dumpInfo();
}

//  API Qt3DRender::Render::AbstractRenderer::api() const
extern "C" Q_DECL_EXPORT
Qt3DRender::API ritual_ZNK10Qt3DRender6Render16AbstractRenderer3apiEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->api();
}

//  void Qt3DRender::Render::AbstractRenderer::setRenderDriver(RenderDriver
//      driver)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer15setRenderDriverENS1_12RenderDriverE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::Render::AbstractRenderer::RenderDriver driver) {
  self->setRenderDriver(driver);
}

//  RenderDriver Qt3DRender::Render::AbstractRenderer::renderDriver() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AbstractRenderer::RenderDriver ritual_ZNK10Qt3DRender6Render16AbstractRenderer12renderDriverEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->renderDriver();
}

//  qint64 Qt3DRender::Render::AbstractRenderer::time() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10Qt3DRender6Render16AbstractRenderer4timeEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->time();
}

//  void Qt3DRender::Render::AbstractRenderer::setTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer7setTimeEx(
    Qt3DRender::Render::AbstractRenderer *self,
    qint64 time) {
  self->setTime(time);
}

//  void Qt3DRender::Render::AbstractRenderer::setJobsInLastFrame(int
//      jobsInLastFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer18setJobsInLastFrameEi(
    Qt3DRender::Render::AbstractRenderer *self,
    int jobsInLastFrame) {
  self->setJobsInLastFrame(jobsInLastFrame);
}

//  void Qt3DRender::Render::AbstractRenderer::setAspect(QRenderAspect
//      *aspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer9setAspectEPNS_13QRenderAspectE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::QRenderAspect *aspect) {
  self->setAspect(aspect);
}

//  void Qt3DRender::Render::AbstractRenderer::setNodeManagers(NodeManagers
//      *managers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::Render::NodeManagers *managers) {
  self->setNodeManagers(managers);
}

//  void Qt3DRender::Render::AbstractRenderer::setServices(Qt3DCore::QService
//      Locator *services)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer11setServicesEPN8Qt3DCore15QServiceLocatorE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DCore::QServiceLocator *services) {
  self->setServices(services);
}

//  void Qt3DRender::Render::AbstractRenderer::setSurfaceExposed(bool
//      exposed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer17setSurfaceExposedEb(
    Qt3DRender::Render::AbstractRenderer *self,
    bool exposed) {
  self->setSurfaceExposed(exposed);
}

//  QRenderAspect *Qt3DRender::Render::AbstractRenderer::aspect() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspect *ritual_ZNK10Qt3DRender6Render16AbstractRenderer6aspectEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->aspect();
}

//  NodeManagers *Qt3DRender::Render::AbstractRenderer::nodeManagers() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render16AbstractRenderer12nodeManagersEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->nodeManagers();
}

//  Qt3DCore::QServiceLocator
//      *Qt3DRender::Render::AbstractRenderer::services() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QServiceLocator *ritual_ZNK10Qt3DRender6Render16AbstractRenderer8servicesEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->services();
}

//  void Qt3DRender::Render::AbstractRenderer::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer10initializeEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  self->initialize();
}

//  void Qt3DRender::Render::AbstractRenderer::shutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer8shutdownEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  self->shutdown();
}

//  void Qt3DRender::Render::AbstractRenderer::releaseGraphicsResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer24releaseGraphicsResourcesEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  self->releaseGraphicsResources();
}

//  void Qt3DRender::Render::AbstractRenderer::render(bool swapBuffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer6renderEb(
    Qt3DRender::Render::AbstractRenderer *self,
    bool swapBuffers) {
  self->render(swapBuffers);
}

//  void Qt3DRender::Render::AbstractRenderer::cleanGraphicsResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer22cleanGraphicsResourcesEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  self->cleanGraphicsResources();
}

//  bool Qt3DRender::Render::AbstractRenderer::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16AbstractRenderer9isRunningEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->isRunning();
}

//  void Qt3DRender::Render::AbstractRenderer::markDirty(BackendNodeDirtySet
//      changes, BackendNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer9markDirtyE6QFlagsINS1_20BackendNodeDirtyFlagEEPNS0_11BackendNodeE(
    Qt3DRender::Render::AbstractRenderer *self,
    int changes,
    Qt3DRender::Render::BackendNode *node) {
  self->markDirty(
      QFlags<Qt3DRender::Render::AbstractRenderer::BackendNodeDirtyFlag>::fromInt(changes),
      node);
}

//  BackendNodeDirtySet Qt3DRender::Render::AbstractRenderer::dirtyBits()
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render16AbstractRenderer9dirtyBitsEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  return static_cast<int>(self->dirtyBits().toInt());
}

//  bool Qt3DRender::Render::AbstractRenderer::shouldRender() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16AbstractRenderer12shouldRenderEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->shouldRender();
}

//  void Qt3DRender::Render::AbstractRenderer::skipNextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer13skipNextFrameEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  self->skipNextFrame();
}

//  void
//      Qt3DRender::Render::AbstractRenderer::jobsDone(Qt3DCore::QAspectManag
//      er *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer8jobsDoneEPN8Qt3DCore14QAspectManagerE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DCore::QAspectManager *manager) {
  self->jobsDone(manager);
}

//  bool Qt3DRender::Render::AbstractRenderer::processMouseEvent(QObject
//      *object, QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render16AbstractRenderer17processMouseEventEP7QObjectP11QMouseEvent(
    Qt3DRender::Render::AbstractRenderer *self,
    QObject *object,
    QMouseEvent *event) {
  return self->processMouseEvent(object, event);
}

//  bool Qt3DRender::Render::AbstractRenderer::processKeyEvent(QObject
//      *object, QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render16AbstractRenderer15processKeyEventEP7QObjectP9QKeyEvent(
    Qt3DRender::Render::AbstractRenderer *self,
    QObject *object,
    QKeyEvent *event) {
  return self->processKeyEvent(object, event);
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DRender::Render::AbstractRenderer::preRenderingJobs()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN10Qt3DRender6Render16AbstractRenderer16preRenderingJobsEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->preRenderingJobs());
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DRender::Render::AbstractRenderer::renderBinJobs()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN10Qt3DRender6Render16AbstractRenderer13renderBinJobsEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->renderBinJobs());
}

//  void Qt3DRender::Render::AbstractRenderer::setSceneRoot(Entity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer12setSceneRootEPNS0_6EntityE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::Render::Entity *root) {
  self->setSceneRoot(root);
}

//  Entity *Qt3DRender::Render::AbstractRenderer::sceneRoot() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity *ritual_ZNK10Qt3DRender6Render16AbstractRenderer9sceneRootEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->sceneRoot();
}

//  FrameGraphNode *Qt3DRender::Render::AbstractRenderer::frameGraphRoot()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphNode *ritual_ZNK10Qt3DRender6Render16AbstractRenderer14frameGraphRootEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->frameGraphRoot();
}

//  Qt3DCore::QAbstractFrameAdvanceService
//      *Qt3DRender::Render::AbstractRenderer::frameAdvanceService() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrameAdvanceService *ritual_ZNK10Qt3DRender6Render16AbstractRenderer19frameAdvanceServiceEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->frameAdvanceService();
}

//  void Qt3DRender::Render::AbstractRenderer::setSettings(RenderSettings
//      *settings)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer11setSettingsEPNS0_14RenderSettingsE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::Render::RenderSettings *settings) {
  self->setSettings(settings);
}

//  RenderSettings *Qt3DRender::Render::AbstractRenderer::settings() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderSettings *ritual_ZNK10Qt3DRender6Render16AbstractRenderer8settingsEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->settings();
}

//  QVariant Qt3DRender::Render::AbstractRenderer::executeCommand(const
//      QStringList &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10Qt3DRender6Render16AbstractRenderer14executeCommandERK5QListI7QStringE(
    Qt3DRender::Render::AbstractRenderer *self,
    const QList<QString> *args) {
  return new QVariant(self->executeCommand(*args));
}

//  void
//      Qt3DRender::Render::AbstractRenderer::setOpenGLContext(QOpenGLContext
//      *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer16setOpenGLContextEP14QOpenGLContext(
    Qt3DRender::Render::AbstractRenderer *self,
    QOpenGLContext *ctx) {
  self->setOpenGLContext(ctx);
}

//  void Qt3DRender::Render::AbstractRenderer::setRHIContext(QRhi *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer13setRHIContextEP4QRhi(
    Qt3DRender::Render::AbstractRenderer *self,
    QRhi *ctx) {
  self->setRHIContext(ctx);
}

//  void Qt3DRender::Render::AbstractRenderer::setDefaultRHIRenderTarget(QRhi
//      RenderTarget *defaultTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer25setDefaultRHIRenderTargetEP16QRhiRenderTarget(
    Qt3DRender::Render::AbstractRenderer *self,
    QRhiRenderTarget *defaultTarget) {
  self->setDefaultRHIRenderTarget(defaultTarget);
}

//  void Qt3DRender::Render::AbstractRenderer::setRHICommandBuffer(QRhiComman
//      dBuffer *commandBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer19setRHICommandBufferEP17QRhiCommandBuffer(
    Qt3DRender::Render::AbstractRenderer *self,
    QRhiCommandBuffer *commandBuffer) {
  self->setRHICommandBuffer(commandBuffer);
}

//  void Qt3DRender::Render::AbstractRenderer::setScreen(QScreen *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7QScreen(
    Qt3DRender::Render::AbstractRenderer *self,
    QScreen *a0) {
  self->setScreen(a0);
}

//  QScreen *Qt3DRender::Render::AbstractRenderer::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->screen();
}

//  bool Qt3DRender::Render::AbstractRenderer::accessOpenGLTexture(Qt3DCore::
//      QNodeId nodeId, QOpenGLTexture **texture, QMutex **lock, bool
//      readonly)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render16AbstractRenderer19accessOpenGLTextureEN8Qt3DCore7QNodeIdEPP14QOpenGLTexturePP6QMutexb(
    Qt3DRender::Render::AbstractRenderer *self,
    const Qt3DCore::QNodeId *nodeId,
    QOpenGLTexture **texture,
    QMutex **lock,
    bool readonly) {
  return self->accessOpenGLTexture(*nodeId, texture, lock, readonly);
}

//  QSharedPointer<RenderBackendResourceAccessor>
//      Qt3DRender::Render::AbstractRenderer::resourceAccessor() const
extern "C" Q_DECL_EXPORT
QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> *ritual_ZNK10Qt3DRender6Render16AbstractRenderer16resourceAccessorEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return new QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor>(
      self->resourceAccessor());
}

//  void Qt3DRender::Render::AbstractRenderer::setOffscreenSurfaceHelper(Offs
//      creenSurfaceHelper *helper)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer25setOffscreenSurfaceHelperEPNS0_22OffscreenSurfaceHelperE(
    Qt3DRender::Render::AbstractRenderer *self,
    Qt3DRender::Render::OffscreenSurfaceHelper *helper) {
  self->setOffscreenSurfaceHelper(helper);
}

//  QSurfaceFormat Qt3DRender::Render::AbstractRenderer::format()
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN10Qt3DRender6Render16AbstractRenderer6formatEv(
    Qt3DRender::Render::AbstractRenderer *self) {
  return new QSurfaceFormat(self->format());
}

//  QOpenGLContext *Qt3DRender::Render::AbstractRenderer::shareContext()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK10Qt3DRender6Render16AbstractRenderer12shareContextEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->shareContext();
}

//  const GraphicsApiFilterData
//      *Qt3DRender::Render::AbstractRenderer::contextInfo() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::GraphicsApiFilterData *ritual_ZNK10Qt3DRender6Render16AbstractRenderer11contextInfoEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->contextInfo();
}

//  bool
//      Qt3DRender::Render::AbstractRenderer::containsGeneratedShaderGraph(co
//      nst QByteArray &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16AbstractRenderer28containsGeneratedShaderGraphERK10QByteArray(
    const Qt3DRender::Render::AbstractRenderer *self,
    const QByteArray *key) {
  return self->containsGeneratedShaderGraph(*key);
}

//  QByteArray
//      Qt3DRender::Render::AbstractRenderer::cachedGeneratedShaderGraph(cons
//      t QByteArray &key) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender6Render16AbstractRenderer26cachedGeneratedShaderGraphERK10QByteArray(
    const Qt3DRender::Render::AbstractRenderer *self,
    const QByteArray *key) {
  return new QByteArray(self->cachedGeneratedShaderGraph(*key));
}

//  void
//      Qt3DRender::Render::AbstractRenderer::insertGeneratedShaderGraph(cons
//      t QByteArray &key, const QByteArray shaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer26insertGeneratedShaderGraphERK10QByteArrayS2_(
    Qt3DRender::Render::AbstractRenderer *self,
    const QByteArray *key,
    const QByteArray *shaderCode) {
  self->insertGeneratedShaderGraph(*key, *shaderCode);
}

//  void
//      Qt3DRender::Render::AbstractRenderer::removeGeneratedShaderGraph(cons
//      t QByteArray &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16AbstractRenderer26removeGeneratedShaderGraphERK10QByteArray(
    Qt3DRender::Render::AbstractRenderer *self,
    const QByteArray *key) {
  self->removeGeneratedShaderGraph(*key);
}

//  a Python function taken by a CuteQt3DRender_Render_AbstractRenderer, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_AbstractRenderer(
    Qt3DRender::Render::AbstractRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_AbstractRenderer *>(self)->take(key, call);
}

//  void Qt3DRender::Render::AbstractRenderer::setScreen(QScreen *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render16AbstractRenderer9setScreenEP7QScreen(
    Qt3DRender::Render::AbstractRenderer *self,
    QScreen *a0) {
  self->Qt3DRender::Render::AbstractRenderer::setScreen(a0);
}

//  QScreen *Qt3DRender::Render::AbstractRenderer::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_own_ZNK10Qt3DRender6Render16AbstractRenderer6screenEv(
    const Qt3DRender::Render::AbstractRenderer *self) {
  return self->Qt3DRender::Render::AbstractRenderer::screen();
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DRender::Render::AbstractRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_AbstractRenderer__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}

//  a QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> a
//      ritual of Qt3DRender::Render::AbstractRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_AbstractRenderer__QSharedPointer_Qt3DRender_Render_RenderBackendResourceAccessor(
    QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> *self) {
  delete self;
}
