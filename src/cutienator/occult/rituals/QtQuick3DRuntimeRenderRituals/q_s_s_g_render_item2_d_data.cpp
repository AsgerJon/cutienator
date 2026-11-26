//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderitem2d_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#if QT_CONFIG(thread)
#include <QtCore/qthreadpool.h>
#endif
#include <QtCore/qtenvironmentvariables.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 695, as _ZN20QSSGRenderItem2DDataC1ERKSt10shared_ptrI24QSSGGlobalRenderNodeDataE
inline QSSGRenderItem2DData::QSSGRenderItem2DData(const QSSGGlobalRenderNodeDataPtr &globalNodeData)
{
    m_gnd = globalNodeData;
    m_version = globalNodeData->version();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 701, as _ZN20QSSGRenderItem2DDataD1Ev
inline QSSGRenderItem2DData::~QSSGRenderItem2DData()
{
    releaseAll();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 678, as _ZNK20QSSGRenderItem2DData22getModelViewProjectionE23QSSGRenderStorageHandleIL10HandleType1EE
inline QSSGRenderItem2DData::ModelViewProjections QSSGRenderItem2DData::getModelViewProjection(QSSGRenderNodeHandle h) const
{
    const bool hasId = h.hasId();
    const bool validVersion = hasId && (h.version() == m_version);
    const auto index = h.index();

    if (!validVersion || !(modelViewProjections.size() > index))
        return {};

    return modelViewProjections[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 690, as _ZNK20QSSGRenderItem2DData22getModelViewProjectionERK16QSSGRenderItem2D
inline QSSGRenderItem2DData::ModelViewProjections QSSGRenderItem2DData::getModelViewProjection(const QSSGRenderItem2D &item) const
{
    return getModelViewProjection(item.h);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 672, as _ZNK20QSSGRenderItem2DData17getItem2DRendererERK16QSSGRenderItem2D
inline QSSGRenderItem2DData::Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const QSSGRenderItem2D &item) const
{
    const auto foundIt = item2DRenderers.find(&item);
    return (foundIt != item2DRenderers.cend()) ? foundIt->second : Item2DRenderer{};
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 771, as _ZN20QSSGRenderItem2DData17releaseRenderDataERK16QSSGRenderItem2D
inline void QSSGRenderItem2DData::releaseRenderData(const QSSGRenderItem2D &item)
{
    const auto foundIt = item2DRenderers.find(&item);
    if (foundIt != item2DRenderers.cend()) {
        delete foundIt->second;
        item2DRenderers.erase(foundIt);

        // Removing an item should trigger a reindex of the remaining items
        ++m_version;
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 783, as _ZN20QSSGRenderItem2DData10releaseAllEv
inline void QSSGRenderItem2DData::releaseAll()
{
    for (auto &it : item2DRenderers)
        delete it.second;
    item2DRenderers.clear();
    item2DRenderContext = nullptr;
    modelViewProjections.clear();
    m_version = 0;
}
//  -----------------------------------------------------------------------

//  QSSGRenderItem2DData::QSSGRenderItem2DData(const
//      QSSGGlobalRenderNodeDataPtr &globalNodeData)
extern "C" Q_DECL_EXPORT
QSSGRenderItem2DData *ritual_ZN20QSSGRenderItem2DDataC1ERKSt10shared_ptrI24QSSGGlobalRenderNodeDataE(
    const QSSGGlobalRenderNodeDataPtr *globalNodeData) {
  return new QSSGRenderItem2DData(*globalNodeData);
}

//  QSSGRenderItem2DData::~QSSGRenderItem2DData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGRenderItem2DDataD1Ev(QSSGRenderItem2DData *self) {
  delete self;
}

//  ModelViewProjections
//      QSSGRenderItem2DData::getModelViewProjection(QSSGRenderNodeHandle h)
//      const
extern "C" Q_DECL_EXPORT
QSSGRenderItem2DData::ModelViewProjections *ritual_ZNK20QSSGRenderItem2DData22getModelViewProjectionE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGRenderItem2DData *self,
    const QSSGRenderNodeHandle *h) {
  return new QSSGRenderItem2DData::ModelViewProjections(
      self->getModelViewProjection(
          *h));
}

//  ModelViewProjections QSSGRenderItem2DData::getModelViewProjection(const
//      QSSGRenderItem2D &item) const
extern "C" Q_DECL_EXPORT
QSSGRenderItem2DData::ModelViewProjections *ritual_ZNK20QSSGRenderItem2DData22getModelViewProjectionERK16QSSGRenderItem2D(
    const QSSGRenderItem2DData *self,
    const QSSGRenderItem2D *item) {
  return new QSSGRenderItem2DData::ModelViewProjections(
      self->getModelViewProjection(
          *item));
}

//  Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const
//      QSSGRenderItem2D &item) const
extern "C" Q_DECL_EXPORT
QSSGRenderItem2DData::Item2DRenderer *ritual_ZNK20QSSGRenderItem2DData17getItem2DRendererERK16QSSGRenderItem2D(
    const QSSGRenderItem2DData *self,
    const QSSGRenderItem2D *item) {
  return new QSSGRenderItem2DData::Item2DRenderer(
      self->getItem2DRenderer(
          *item));
}

//  const QSSGGlobalRenderNodeDataPtr &QSSGRenderItem2DData::globalNodeData()
//      const
extern "C" Q_DECL_EXPORT
const QSSGGlobalRenderNodeDataPtr *ritual_ZNK20QSSGRenderItem2DData14globalNodeDataEv(
    const QSSGRenderItem2DData *self) {
  return &(self->globalNodeData());
}

//  void QSSGRenderItem2DData::releaseRenderData(const QSSGRenderItem2D
//      &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGRenderItem2DData17releaseRenderDataERK16QSSGRenderItem2D(
    QSSGRenderItem2DData *self,
    const QSSGRenderItem2D *item) {
  self->releaseRenderData(*item);
}

//  void QSSGRenderItem2DData::releaseAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGRenderItem2DData10releaseAllEv(
    QSSGRenderItem2DData *self) {
  self->releaseAll();
}

//  a QSSGRenderItem2DData::ModelViewProjections a ritual of
//      QSSGRenderItem2DData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderItem2DData__QSSGRenderItem2DData_ModelViewProjections(
    QSSGRenderItem2DData::ModelViewProjections *self) {
  delete self;
}

//  a QSSGRenderItem2DData::Item2DRenderer a ritual of QSSGRenderItem2DData
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderItem2DData__QSSGRenderItem2DData_Item2DRenderer(
    QSSGRenderItem2DData::Item2DRenderer *self) {
  delete self;
}
