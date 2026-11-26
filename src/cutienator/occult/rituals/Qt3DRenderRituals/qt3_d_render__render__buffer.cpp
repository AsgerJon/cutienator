//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/buffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/buffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>

//  A Qt3DRender::Render::Buffer that Python can take functions over in. Every Qt3DRender::Render::Buffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_BufferCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Buffer : public Qt3DRender::Render::Buffer {
public:
  using Qt3DRender::Render::Buffer::Buffer;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Buffer::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_BufferCall0 call = reinterpret_cast<CuteQt3DRender_Render_BufferCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Buffer::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Buffer::Buffer()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Buffer *ritual_ZN10Qt3DRender6Render6BufferC1Ev() {
  return new CuteQt3DRender_Render_Buffer();
}

//  Qt3DRender::Render::Buffer::~Buffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6BufferD1Ev(
    Qt3DRender::Render::Buffer *self) {
  delete self;
}

//  void Qt3DRender::Render::Buffer::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer7cleanupEv(
    Qt3DRender::Render::Buffer *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Buffer::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Buffer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::Buffer::setManager(BufferManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer10setManagerEPNS0_13BufferManagerE(
    Qt3DRender::Render::Buffer *self,
    Qt3DRender::Render::BufferManager *manager) {
  self->setManager(manager);
}

//  void Qt3DRender::Render::Buffer::updateDataFromGPUToCPU(QByteArray data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer22updateDataFromGPUToCPUE10QByteArray(
    Qt3DRender::Render::Buffer *self,
    const QByteArray *data) {
  self->updateDataFromGPUToCPU(*data);
}

//  Qt3DCore::QBuffer::UsageType Qt3DRender::Render::Buffer::usage() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBuffer::UsageType ritual_ZNK10Qt3DRender6Render6Buffer5usageEv(
    const Qt3DRender::Render::Buffer *self) {
  return self->usage();
}

//  QByteArray Qt3DRender::Render::Buffer::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender6Render6Buffer4dataEv(
    const Qt3DRender::Render::Buffer *self) {
  return new QByteArray(self->data());
}

//  std::vector<Qt3DCore::QBufferUpdate>
//      &Qt3DRender::Render::Buffer::pendingBufferUpdates()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QBufferUpdate> *ritual_ZN10Qt3DRender6Render6Buffer20pendingBufferUpdatesEv(
    Qt3DRender::Render::Buffer *self) {
  return &(self->pendingBufferUpdates());
}

//  bool Qt3DRender::Render::Buffer::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Buffer7isDirtyEv(
    const Qt3DRender::Render::Buffer *self) {
  return self->isDirty();
}

//  Qt3DCore::QBuffer::AccessType Qt3DRender::Render::Buffer::access() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBuffer::AccessType ritual_ZNK10Qt3DRender6Render6Buffer6accessEv(
    const Qt3DRender::Render::Buffer *self) {
  return self->access();
}

//  void Qt3DRender::Render::Buffer::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer10unsetDirtyEv(
    Qt3DRender::Render::Buffer *self) {
  self->unsetDirty();
}

//  void Qt3DRender::Render::Buffer::forceDataUpload()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Buffer15forceDataUploadEv(
    Qt3DRender::Render::Buffer *self) {
  self->forceDataUpload();
}

//  a Python function taken by a CuteQt3DRender_Render_Buffer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Buffer(
    Qt3DRender::Render::Buffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Buffer *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Buffer::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render6Buffer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Buffer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Buffer::syncFromFrontEnd(frontEnd, firstTime);
}
