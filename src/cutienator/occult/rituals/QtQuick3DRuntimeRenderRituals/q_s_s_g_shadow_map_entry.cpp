//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/qssgrendershadowmap.cpp, line 547, as _ZN18QSSGShadowMapEntryC1Ev
inline QSSGShadowMapEntry::QSSGShadowMapEntry()
    : m_lightIndex(std::numeric_limits<quint32>::max())
{
}

//  from ../qtquick3d/src/runtimerender/qssgrendershadowmap.cpp, line 552, as _ZN18QSSGShadowMapEntry9withAtlasEj
inline QSSGShadowMapEntry QSSGShadowMapEntry::withAtlas(quint32 lightIdx)
{
    QSSGShadowMapEntry e;
    e.m_lightIndex = lightIdx;
    return e;
}

//  from ../qtquick3d/src/runtimerender/qssgrendershadowmap.cpp, line 559, as _ZN18QSSGShadowMapEntry19destroyRhiResourcesEv
inline void QSSGShadowMapEntry::destroyRhiResources()
{
    delete m_rhiDepthCube;
    m_rhiDepthCube = nullptr;
    delete m_rhiDepthStencilCube;
    m_rhiDepthStencilCube = nullptr;
    qDeleteAll(m_rhiRenderTargetCube);
    m_rhiRenderTargetCube.fill(nullptr);
    delete m_rhiRenderPassDescCube;
    m_rhiRenderPassDescCube = nullptr;
    delete m_cubeToAtlasFrontSrb;
    m_cubeToAtlasFrontSrb = nullptr;
    delete m_cubeToAtlasBackSrb;
    m_cubeToAtlasBackSrb = nullptr;

    // un-owned references
    m_rhiRenderTargets.fill(nullptr);
    m_rhiRenderPassDesc.fill(nullptr);
}
//  -----------------------------------------------------------------------

//  QSSGShadowMapEntry::QSSGShadowMapEntry()
extern "C" Q_DECL_EXPORT
QSSGShadowMapEntry *ritual_ZN18QSSGShadowMapEntryC1Ev() {
  return new QSSGShadowMapEntry();
}

//  QSSGShadowMapEntry QSSGShadowMapEntry::withAtlas(quint32 lightIdx)
extern "C" Q_DECL_EXPORT
QSSGShadowMapEntry *ritual_ZN18QSSGShadowMapEntry9withAtlasEj(
    quint32 lightIdx) {
  return new QSSGShadowMapEntry(QSSGShadowMapEntry::withAtlas(lightIdx));
}

//  void QSSGShadowMapEntry::destroyRhiResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShadowMapEntry19destroyRhiResourcesEv(
    QSSGShadowMapEntry *self) {
  self->destroyRhiResources();
}

//  QSSGShadowMapEntry::~QSSGShadowMapEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSSGShadowMapEntryD1Ev(QSSGShadowMapEntry *self) {
  delete self;
}
