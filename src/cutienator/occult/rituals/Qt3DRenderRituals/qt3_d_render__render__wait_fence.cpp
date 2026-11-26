//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/waitfence_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/waitfence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/waitfence_p.h>
#include <Qt3DRender/private/qwaitfence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/waitfence.cpp, line 25, as _ZN10Qt3DRender6Render9WaitFenceC1Ev
namespace Qt3DRender::Render {
inline WaitFence::WaitFence()
    : FrameGraphNode(FrameGraphNode::WaitFence)
{
    m_data.handleType = QWaitFence::NoHandle;
    m_data.waitOnCPU = false;
    m_data.timeout = std::numeric_limits<quint64>::max();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/framegraph/waitfence.cpp, line 33, as _ZN10Qt3DRender6Render9WaitFenceD1Ev
namespace Qt3DRender::Render {
inline WaitFence::~WaitFence()
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/framegraph/waitfence.cpp, line 37, as _ZN10Qt3DRender6Render9WaitFence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DRender::Render {
inline void WaitFence::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    const QWaitFence *node = qobject_cast<const QWaitFence *>(frontEnd);
    if (!node)
        return;

    FrameGraphNode::syncFromFrontEnd(frontEnd, firstTime);

    if (node->handleType() != m_data.handleType) {
        m_data.handleType = node->handleType();
        markDirty(AbstractRenderer::FrameGraphDirty);
    }
    if (node->handle() != m_data.handle) {
        m_data.handle = node->handle();
        markDirty(AbstractRenderer::FrameGraphDirty);
    }
    if (node->timeout() != m_data.timeout) {
        m_data.timeout = node->timeout();
        markDirty(AbstractRenderer::FrameGraphDirty);
    }
    if (node->waitOnCPU() != m_data.waitOnCPU) {
        m_data.waitOnCPU = node->waitOnCPU();
        markDirty(AbstractRenderer::FrameGraphDirty);
    }
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  A Qt3DRender::Render::WaitFence that Python can take functions over in. Every Qt3DRender::Render::WaitFence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_WaitFenceCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_WaitFence : public Qt3DRender::Render::WaitFence {
public:
  using Qt3DRender::Render::WaitFence::WaitFence;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::WaitFence::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_WaitFenceCall0 call = reinterpret_cast<CuteQt3DRender_Render_WaitFenceCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::WaitFence::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::WaitFence::WaitFence()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::WaitFence *ritual_ZN10Qt3DRender6Render9WaitFenceC1Ev() {
  return new CuteQt3DRender_Render_WaitFence();
}

//  Qt3DRender::Render::WaitFence::~WaitFence()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9WaitFenceD1Ev(
    Qt3DRender::Render::WaitFence *self) {
  delete self;
}

//  Data Qt3DRender::Render::WaitFence::data() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::WaitFence::Data *ritual_ZNK10Qt3DRender6Render9WaitFence4dataEv(
    const Qt3DRender::Render::WaitFence *self) {
  return new Qt3DRender::Render::WaitFence::Data(self->data());
}

//  void Qt3DRender::Render::WaitFence::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9WaitFence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::WaitFence *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  a Python function taken by a CuteQt3DRender_Render_WaitFence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_WaitFence(
    Qt3DRender::Render::WaitFence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_WaitFence *>(self)->take(key, call);
}

//  void Qt3DRender::Render::WaitFence::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9WaitFence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::WaitFence *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::WaitFence::syncFromFrontEnd(frontEnd, firstTime);
}
