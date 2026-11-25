//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'qrhivulkan_p.h' is included only
//  where Vulkan's 'vulkan/vulkan.h' is there too, checked by
//  '__has_include' as Qt's 'qvulkaninstance.h' checks it, since
//  without it that header fails on 'VkBuffer', and 'qrhid3d12_p.h'
//  only where the 'D3D12MemAlloc.h' it includes is there, which Qt's
//  Windows kit does not carry; nothing here uses either. Kept as it
//  is when the generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 12088, as _ZNK23QRhiPassResourceTracker7isEmptyEv
inline bool QRhiPassResourceTracker::isEmpty() const
{
    return m_buffers.isEmpty() && m_textures.isEmpty();
}

//  from src/gui/rhi/qrhi.cpp, line 12093, as _ZN23QRhiPassResourceTracker5resetEv
inline void QRhiPassResourceTracker::reset()
{
    m_buffers.clear();
    m_textures.clear();
}

//  from src/gui/rhi/qrhi.cpp, line 12179, as _ZN23QRhiPassResourceTracker24toPassTrackerBufferStageE6QFlagsIN25QRhiShaderResourceBinding9StageFlagEE
inline QRhiPassResourceTracker::BufferStage QRhiPassResourceTracker::toPassTrackerBufferStage(QRhiShaderResourceBinding::StageFlags stages)
{
    // pick the earlier stage (as this is going to be dstAccessMask)
    if (stages.testFlag(QRhiShaderResourceBinding::VertexStage))
        return QRhiPassResourceTracker::BufVertexStage;
    if (stages.testFlag(QRhiShaderResourceBinding::TessellationControlStage))
        return QRhiPassResourceTracker::BufTCStage;
    if (stages.testFlag(QRhiShaderResourceBinding::TessellationEvaluationStage))
        return QRhiPassResourceTracker::BufTEStage;
    if (stages.testFlag(QRhiShaderResourceBinding::FragmentStage))
        return QRhiPassResourceTracker::BufFragmentStage;
    if (stages.testFlag(QRhiShaderResourceBinding::ComputeStage))
        return QRhiPassResourceTracker::BufComputeStage;
    if (stages.testFlag(QRhiShaderResourceBinding::GeometryStage))
        return QRhiPassResourceTracker::BufGeometryStage;

    Q_UNREACHABLE_RETURN(QRhiPassResourceTracker::BufVertexStage);
}

//  from src/gui/rhi/qrhi.cpp, line 12198, as _ZN23QRhiPassResourceTracker25toPassTrackerTextureStageE6QFlagsIN25QRhiShaderResourceBinding9StageFlagEE
inline QRhiPassResourceTracker::TextureStage QRhiPassResourceTracker::toPassTrackerTextureStage(QRhiShaderResourceBinding::StageFlags stages)
{
    // pick the earlier stage (as this is going to be dstAccessMask)
    if (stages.testFlag(QRhiShaderResourceBinding::VertexStage))
        return QRhiPassResourceTracker::TexVertexStage;
    if (stages.testFlag(QRhiShaderResourceBinding::TessellationControlStage))
        return QRhiPassResourceTracker::TexTCStage;
    if (stages.testFlag(QRhiShaderResourceBinding::TessellationEvaluationStage))
        return QRhiPassResourceTracker::TexTEStage;
    if (stages.testFlag(QRhiShaderResourceBinding::FragmentStage))
        return QRhiPassResourceTracker::TexFragmentStage;
    if (stages.testFlag(QRhiShaderResourceBinding::ComputeStage))
        return QRhiPassResourceTracker::TexComputeStage;
    if (stages.testFlag(QRhiShaderResourceBinding::GeometryStage))
        return QRhiPassResourceTracker::TexGeometryStage;

    Q_UNREACHABLE_RETURN(QRhiPassResourceTracker::TexVertexStage);
}
//  -----------------------------------------------------------------------

//  bool QRhiPassResourceTracker::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRhiPassResourceTracker7isEmptyEv(
    const QRhiPassResourceTracker *self) {
  return self->isEmpty();
}

//  void QRhiPassResourceTracker::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiPassResourceTracker5resetEv(
    QRhiPassResourceTracker *self) {
  self->reset();
}

//  BufferStage QRhiPassResourceTracker::toPassTrackerBufferStage(QRhiShaderR
//      esourceBinding::StageFlags stages)
extern "C" Q_DECL_EXPORT
QRhiPassResourceTracker::BufferStage ritual_ZN23QRhiPassResourceTracker24toPassTrackerBufferStageE6QFlagsIN25QRhiShaderResourceBinding9StageFlagEE(
    int stages) {
  return QRhiPassResourceTracker::toPassTrackerBufferStage(
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stages));
}

//  TextureStage QRhiPassResourceTracker::toPassTrackerTextureStage(QRhiShade
//      rResourceBinding::StageFlags stages)
extern "C" Q_DECL_EXPORT
QRhiPassResourceTracker::TextureStage ritual_ZN23QRhiPassResourceTracker25toPassTrackerTextureStageE6QFlagsIN25QRhiShaderResourceBinding9StageFlagEE(
    int stages) {
  return QRhiPassResourceTracker::toPassTrackerTextureStage(
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stages));
}

//  QRhiPassResourceTracker::~QRhiPassResourceTracker()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiPassResourceTrackerD1Ev(QRhiPassResourceTracker *self) {
  delete self;
}
