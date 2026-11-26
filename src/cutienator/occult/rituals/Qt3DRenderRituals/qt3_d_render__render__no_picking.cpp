//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/nopicking_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/nopicking_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/nopicking_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/nopicking.cpp, line 14, as _ZN10Qt3DRender6Render9NoPickingC1Ev
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline NoPicking::NoPicking()
    : FrameGraphNode(FrameGraphNode::NoPicking)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/framegraph/nopicking.cpp, line 19, as _ZN10Qt3DRender6Render9NoPickingD1Ev
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline NoPicking::~NoPicking()
{
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  A Qt3DRender::Render::NoPicking that Python can take functions over in. Every Qt3DRender::Render::NoPicking
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_NoPickingCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_NoPicking : public Qt3DRender::Render::NoPicking {
public:
  using Qt3DRender::Render::NoPicking::NoPicking;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_NoPickingCall0 call = reinterpret_cast<CuteQt3DRender_Render_NoPickingCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::NoPicking::NoPicking()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NoPicking *ritual_ZN10Qt3DRender6Render9NoPickingC1Ev() {
  return new CuteQt3DRender_Render_NoPicking();
}

//  Qt3DRender::Render::NoPicking::~NoPicking()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9NoPickingD1Ev(
    Qt3DRender::Render::NoPicking *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_Render_NoPicking, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_NoPicking(
    Qt3DRender::Render::NoPicking *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_NoPicking *>(self)->take(key, call);
}
