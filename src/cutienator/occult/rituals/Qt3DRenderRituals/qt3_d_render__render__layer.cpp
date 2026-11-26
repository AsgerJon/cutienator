//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/layer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/layer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/layer_p.h>
#include <Qt3DRender/qlayer.h>
#include <Qt3DRender/private/qlayer_p.h>
#include <Qt3DRender/private/stringtoint_p.h>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/layer.cpp, line 18, as _ZN10Qt3DRender6Render5LayerC1Ev
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Layer::Layer()
    : BackendNode()
    , m_recursive(false)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/layer.cpp, line 24, as _ZN10Qt3DRender6Render5LayerD1Ev
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Layer::~Layer()
{
    cleanup();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/layer.cpp, line 29, as _ZN10Qt3DRender6Render5Layer7cleanupEv
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void Layer::cleanup()
{
    QBackendNode::setEnabled(false);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/layer.cpp, line 52, as _ZNK10Qt3DRender6Render5Layer9recursiveEv
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline bool Layer::recursive() const
{
    return m_recursive;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/layer.cpp, line 57, as _ZN10Qt3DRender6Render5Layer12setRecursiveEb
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void Layer::setRecursive(bool recursive)
{
    m_recursive = recursive;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/layer.cpp, line 34, as _ZN10Qt3DRender6Render5Layer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void Layer::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    const QLayer *node = qobject_cast<const QLayer *>(frontEnd);
    if (!node)
        return;

    const bool oldEnabled = isEnabled();
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    if (isEnabled() != oldEnabled || firstTime)
        markDirty(AbstractRenderer::LayersDirty);

    if (node->recursive() != m_recursive) {
        m_recursive = node->recursive();
        markDirty(AbstractRenderer::LayersDirty);
    }
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  A Qt3DRender::Render::Layer that Python can take functions over in. Every Qt3DRender::Render::Layer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_LayerCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Layer : public Qt3DRender::Render::Layer {
public:
  using Qt3DRender::Render::Layer::Layer;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Layer::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_LayerCall0 call = reinterpret_cast<CuteQt3DRender_Render_LayerCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Layer::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Layer::Layer()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Layer *ritual_ZN10Qt3DRender6Render5LayerC1Ev() {
  return new CuteQt3DRender_Render_Layer();
}

//  Qt3DRender::Render::Layer::~Layer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5LayerD1Ev(
    Qt3DRender::Render::Layer *self) {
  delete self;
}

//  void Qt3DRender::Render::Layer::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Layer7cleanupEv(
    Qt3DRender::Render::Layer *self) {
  self->cleanup();
}

//  bool Qt3DRender::Render::Layer::recursive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render5Layer9recursiveEv(
    const Qt3DRender::Render::Layer *self) {
  return self->recursive();
}

//  void Qt3DRender::Render::Layer::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Layer12setRecursiveEb(
    Qt3DRender::Render::Layer *self,
    bool recursive) {
  self->setRecursive(recursive);
}

//  void Qt3DRender::Render::Layer::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Layer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Layer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  a Python function taken by a CuteQt3DRender_Render_Layer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Layer(
    Qt3DRender::Render::Layer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Layer *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Layer::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render5Layer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Layer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Layer::syncFromFrontEnd(frontEnd, firstTime);
}
