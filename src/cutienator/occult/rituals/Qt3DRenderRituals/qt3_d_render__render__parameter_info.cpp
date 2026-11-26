//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderviewjobutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderviewjobutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/renderviewjobutils_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/qshaderdata.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/effect_p.h>
#include <Qt3DRender/private/renderpassfilternode_p.h>
#include <Qt3DRender/private/techniquemanager_p.h>
#include <Qt3DRender/private/techniquefilternode_p.h>
#include <Qt3DRender/private/renderstatenode_p.h>
#include <Qt3DRender/private/renderstates_p.h>
#include <Qt3DRender/private/renderstateset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/jobs/renderviewjobutils.cpp, line 177, as _ZN10Qt3DRender6Render13ParameterInfoC1EiRKN8Qt3DCore7QHandleINS0_9ParameterEEE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline ParameterInfo::ParameterInfo(const int nameId, const HParameter &handle)
    : nameId(nameId)
    , handle(handle)
{}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/jobs/renderviewjobutils.cpp, line 187, as _ZNK10Qt3DRender6Render13ParameterInfoltEi
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline bool ParameterInfo::operator<(const int otherNameId) const noexcept
{
    return nameId < otherNameId;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/jobs/renderviewjobutils.cpp, line 182, as _ZNK10Qt3DRender6Render13ParameterInfoltERKS1_
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline bool ParameterInfo::operator<(const ParameterInfo &other) const noexcept
{
    return nameId < other.nameId;
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::ParameterInfo::ParameterInfo(const int nameId, const
//      HParameter &handle)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ParameterInfo *ritual_ZN10Qt3DRender6Render13ParameterInfoC1EiRKN8Qt3DCore7QHandleINS0_9ParameterEEE(
    int nameId,
    const Qt3DRender::Render::HParameter *handle) {
  return new Qt3DRender::Render::ParameterInfo(nameId, *handle);
}

//  bool Qt3DRender::Render::ParameterInfo::operator<(const int otherNameId)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13ParameterInfoltEi(
    const Qt3DRender::Render::ParameterInfo *self,
    int otherNameId) {
  return self->operator<(otherNameId);
}

//  bool Qt3DRender::Render::ParameterInfo::operator<(const ParameterInfo
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13ParameterInfoltERKS1_(
    const Qt3DRender::Render::ParameterInfo *self,
    const Qt3DRender::Render::ParameterInfo *other) {
  return self->operator<(*other);
}

//  Qt3DRender::Render::ParameterInfo::~ParameterInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ParameterInfoD1Ev(
    Qt3DRender::Render::ParameterInfo *self) {
  delete self;
}
