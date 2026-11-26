//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/subtreeenabler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/subtreeenabler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/subtreeenabler_p.h>
#include <Qt3DRender/private/qsubtreeenabler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/subtreeenabler.cpp, line 18, as _ZN10Qt3DRender6Render14SubtreeEnabler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DRender::Render {
inline void SubtreeEnabler::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    const QSubtreeEnabler *node = qobject_cast<const QSubtreeEnabler *>(frontEnd);
    if (!node)
        return;

    FrameGraphNode::syncFromFrontEnd(frontEnd, firstTime);

    const auto enablement = node->enablement();
    if (enablement != m_enablement) {
        m_enablement = enablement;
        markDirty(AbstractRenderer::FrameGraphDirty);
    }
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/framegraph/subtreeenabler.cpp, line 13, as _ZN10Qt3DRender6Render14SubtreeEnablerC1Ev
namespace Qt3DRender::Render {
inline SubtreeEnabler::SubtreeEnabler()
    : FrameGraphNode(FrameGraphNode::SubtreeEnabler, FrameGraphNode::ReadWrite)
{
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::SubtreeEnabler::SubtreeEnabler()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SubtreeEnabler *ritual_ZN10Qt3DRender6Render14SubtreeEnablerC1Ev() {
  return new Qt3DRender::Render::SubtreeEnabler();
}

//  QSubtreeEnabler::Enablement
//      Qt3DRender::Render::SubtreeEnabler::enablement() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QSubtreeEnabler::Enablement ritual_ZNK10Qt3DRender6Render14SubtreeEnabler10enablementEv(
    const Qt3DRender::Render::SubtreeEnabler *self) {
  return self->enablement();
}

//  void Qt3DRender::Render::SubtreeEnabler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14SubtreeEnabler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::SubtreeEnabler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::SubtreeEnabler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render14SubtreeEnabler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::SubtreeEnabler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::SubtreeEnabler::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
