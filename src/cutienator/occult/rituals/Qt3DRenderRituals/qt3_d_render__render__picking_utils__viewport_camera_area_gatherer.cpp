//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <vector>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/pickboundingvolumeutils_p.h>
#include <Qt3DRender/private/geometryrenderer_p.h>
#include <Qt3DRender/private/framegraphnode_p.h>
#include <Qt3DRender/private/cameralens_p.h>
#include <Qt3DRender/private/cameraselectornode_p.h>
#include <Qt3DRender/private/viewportnode_p.h>
#include <Qt3DRender/private/rendersurfaceselector_p.h>
#include <Qt3DRender/private/triangleboundingvolume_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/private/entity_p.h>
#include <Qt3DRender/private/trianglesvisitor_p.h>
#include <Qt3DRender/private/segmentsvisitor_p.h>
#include <Qt3DRender/private/pointsvisitor_p.h>
#include <Qt3DRender/private/layer_p.h>
#include <Qt3DRender/private/layerfilternode_p.h>
#include <Qt3DRender/private/rendersettings_p.h>
#include <Qt3DRender/private/filterlayerentityjob_p.h>
#include <vector>
#include <algorithm>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 114, as _ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer6gatherEPNS0_14FrameGraphNodeE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline std::vector<ViewportCameraAreaDetails> ViewportCameraAreaGatherer::gather(FrameGraphNode *root)
{
    // Retrieve all leaves
    visit(root);
    std::vector<ViewportCameraAreaDetails> vcaTriplets;
    vcaTriplets.reserve(m_leaves.size());

    // Find all viewport/camera pairs by traversing from leaf to root
    for (Render::FrameGraphNode *leaf : m_leaves) {
        ViewportCameraAreaDetails vcaDetails = gatherUpViewportCameraAreas(leaf);
        if (!m_targetCamera.isNull() && vcaDetails.cameraId != m_targetCamera)
            continue;
        if (!vcaDetails.cameraId.isNull() && isUnique(vcaTriplets, vcaDetails))
            vcaTriplets.push_back(vcaDetails);
    }
    return vcaTriplets;
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 61, as _ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer5visitEPNS0_14FrameGraphNodeE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline void ViewportCameraAreaGatherer::visit(FrameGraphNode *node)
{
    const auto children = node->children();
    for (Render::FrameGraphNode *n : children)
        visit(n);
    if (node->childrenIds().empty())
        m_leaves.push_back(node);
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 70, as _ZNK10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer27gatherUpViewportCameraAreasEPNS0_14FrameGraphNodeE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline ViewportCameraAreaDetails ViewportCameraAreaGatherer::gatherUpViewportCameraAreas(Render::FrameGraphNode *node) const
{
    ViewportCameraAreaDetails vca;
    vca.viewport = QRectF(0., 0., 1., 1.);

    while (node) {
        if (node->isEnabled()) {
            switch (node->nodeType()) {
            case FrameGraphNode::CameraSelector:
                vca.cameraId = static_cast<const CameraSelector *>(node)->cameraUuid();
                break;
            case FrameGraphNode::Viewport: {
                auto vnode = static_cast<const ViewportNode *>(node);
                // we want the leaf viewport so if we have a viewport node already don't override it with its parent
                if (!vca.viewportNodeId)
                    vca.viewportNodeId = vnode->peerId();
                vca.viewport = ViewportNode::computeViewport(vca.viewport, vnode);
                break;
            }
            case FrameGraphNode::Surface: {
                auto selector = static_cast<const RenderSurfaceSelector *>(node);
                vca.area = selector->renderTargetSize();
                vca.surface = selector->surface();
                break;
            }
            case FrameGraphNode::NoPicking: {
                // Return an empty/invalid ViewportCameraAreaDetails which will
                // prevent picking in the presence of a NoPicking node
                return {};
            }
            case FrameGraphNode::LayerFilter: {
                auto fnode = static_cast<const LayerFilterNode *>(node);
                vca.layersFilters.push_back(fnode->peerId());
                break;
            }
            default:
                break;
            }
        }
        node = node->parent();
    }
    return vca;
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 132, as _ZNK10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer8isUniqueERKSt6vectorINS1_25ViewportCameraAreaDetailsESaIS4_EERKS4_
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline bool ViewportCameraAreaGatherer::isUnique(const std::vector<ViewportCameraAreaDetails> &vcaList,
                                          const ViewportCameraAreaDetails &vca) const
{
    for (const ViewportCameraAreaDetails &listItem : vcaList) {
        if (vca.cameraId == listItem.cameraId &&
                vca.viewport == listItem.viewport &&
                vca.surface == listItem.surface &&
                vca.area == listItem.area &&
                vca.layersFilters == listItem.layersFilters)
            return false;
    }
    return true;
}
}  // namespace Qt3DRender::Render::PickingUtils
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::ViewportCam
//      eraAreaGatherer(const Qt3DCore::QNodeId &nodeId)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGathererC1ERKN8Qt3DCore7QNodeIdE(
    const Qt3DCore::QNodeId *nodeId) {
  return new Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer(
      *nodeId);
}

//  std::vector<ViewportCameraAreaDetails> Qt3DRender::Render::PickingUtils::
//      ViewportCameraAreaGatherer::gather(FrameGraphNode *root)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails> *ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer6gatherEPNS0_14FrameGraphNodeE(
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self,
    Qt3DRender::Render::FrameGraphNode *root) {
  return new std::vector<Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails>(
      self->gather(
          root));
}

//  void Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::visit(
//      FrameGraphNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer5visitEPNS0_14FrameGraphNodeE(
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self,
    Qt3DRender::Render::FrameGraphNode *node) {
  self->visit(node);
}

//  ViewportCameraAreaDetails Qt3DRender::Render::PickingUtils::ViewportCamer
//      aAreaGatherer::gatherUpViewportCameraAreas(Render::FrameGraphNode
//      *node) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails *ritual_ZNK10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer27gatherUpViewportCameraAreasEPNS0_14FrameGraphNodeE(
    const Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self,
    Qt3DRender::Render::FrameGraphNode *node) {
  return new Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails(
      self->gatherUpViewportCameraAreas(
          node));
}

//  bool Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::isUniq
//      ue(const std::vector<ViewportCameraAreaDetails> &vcaList, const
//      ViewportCameraAreaDetails &vca) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGatherer8isUniqueERKSt6vectorINS1_25ViewportCameraAreaDetailsESaIS4_EERKS4_(
    const Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self,
    const std::vector<Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails> *vcaList,
    const Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails *vca) {
  return self->isUnique(*vcaList, *vca);
}

//  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::~ViewportCa
//      meraAreaGatherer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGathererD1Ev(
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self) {
  delete self;
}

//  a
//      std::vector<Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetai
//      ls> a ritual of
//      Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_PickingUtils_ViewportCameraAreaGatherer__std_vector_Qt3DRender_Render_PickingUtils_ViewportCameraAreaDetails(
    std::vector<Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails> *self) {
  delete self;
}
