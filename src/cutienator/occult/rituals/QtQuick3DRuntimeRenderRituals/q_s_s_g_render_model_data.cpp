//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtGui/QMatrix3x3>
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 444, as _ZN19QSSGRenderModelDataC1ERKSt10shared_ptrI24QSSGGlobalRenderNodeDataE
inline QSSGRenderModelData::QSSGRenderModelData(const QSSGGlobalRenderNodeDataPtr &globalNodeData)
    : m_gnd(globalNodeData)
    , m_version(globalNodeData->version())
{

}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 496, as _ZNK19QSSGRenderModelData22getModelViewProjectionE23QSSGRenderStorageHandleIL10HandleType1EE
inline QSSGRenderModelData::ModelViewProjections QSSGRenderModelData::getModelViewProjection(QSSGRenderNodeHandle h) const
{
    const bool hasId = h.hasId();
    const bool validVersion = hasId && (h.version() == m_version);
    const auto index = h.index();

    if (!validVersion || !(modelViewProjections.size() > index))
        return {};

    return modelViewProjections[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 491, as _ZNK19QSSGRenderModelData22getModelViewProjectionERK15QSSGRenderModel
inline QSSGRenderModelData::ModelViewProjections QSSGRenderModelData::getModelViewProjection(const QSSGRenderModel &model) const
{
    return getModelViewProjection(model.h);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 451, as _ZNK19QSSGRenderModelData15getNormalMatrixE23QSSGRenderStorageHandleIL10HandleType1EE14QGenericMatrixILi3ELi3EfE
inline QMatrix3x3 QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h, QMatrix3x3 defaultValue) const
{
    const bool hasId = h.hasId();
    const bool validVersion = hasId && (h.version() == m_gnd->version());
    const auto index = h.index();
    if (!validVersion || !(m_gnd->normalMatrices.size() > index))
        return defaultValue;

    return m_gnd->normalMatrices[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 462, as _ZNK19QSSGRenderModelData15getNormalMatrixERK15QSSGRenderModel
inline QMatrix3x3 QSSGRenderModelData::getNormalMatrix(const QSSGRenderModel &model) const
{
    return getNormalMatrix(model.h, QMatrix3x3{ Qt::Uninitialized });
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 467, as _ZNK19QSSGRenderModelData7getMeshERK15QSSGRenderModel
inline QSSGRenderMesh *QSSGRenderModelData::getMesh(const QSSGRenderModel &model) const
{
    const bool hasId = model.h.hasId();
    const bool validVersion = hasId && (model.h.version() == m_gnd->version());
    const auto index = model.h.index();

    if (!validVersion || !(m_gnd->meshes.size() > index))
        return nullptr;

    return m_gnd->meshes[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 479, as _ZNK19QSSGRenderModelData12getMaterialsERK15QSSGRenderModel
inline QSSGRenderModelData::MaterialList QSSGRenderModelData::getMaterials(const QSSGRenderModel &model) const
{
    const bool hasId = model.h.hasId();
    const bool validVersion = hasId && (model.h.version() == m_gnd->version());
    const auto index = model.h.index();

    if (!validVersion || !(m_gnd->materials.size() > index))
        return {};

    return m_gnd->materials[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 655, as _ZN19QSSGRenderModelData22getThreadPoolThresholdEv
inline quint32 QSSGRenderModelData::getThreadPoolThreshold()
{
    // The threshold is the minimum number of models in a layer to consider using the thread pool for per-model calculations.
    const int ret = qEnvironmentVariableIntValue("QSSG_MODEL_DATA_THREAD_POOL_THRESHOLD");
    return (ret > 0) ? quint32(ret) : 32u;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 508, as _ZN19QSSGRenderModelData15prepareMeshDataERK12QSSGDataViewIP15QSSGRenderModelEP12QSSGRenderer
inline void QSSGRenderModelData::prepareMeshData(const QSSGModelsView &models, QSSGRenderer *renderer)
{
    const auto &bufferManager = renderer->contextInterface()->bufferManager();

    const bool globalPickingEnabled = QSSGRendererPrivate::isGlobalPickingEnabled(*renderer);

    for (auto *model : models) {
        // It's up to the BufferManager to employ the appropriate caching mechanisms, so
        // loadMesh() is expected to be fast if already loaded. Note that preparing
        // the same QSSGRenderModel in different QQuickWindows (possible when a
        // scene is shared between View3Ds where the View3Ds belong to different
        // windows) leads to a different QSSGRenderMesh since the BufferManager is,
        // very correctly, per window, and so per scenegraph render thread.

        // Ensure we have a mesh
        if (auto *theMesh = bufferManager->loadMesh(*model)) {
            m_gnd->meshes[model->h.index()] = theMesh;
            // Completely transparent models cannot be pickable.  But models with completely
            // transparent materials still are.  This allows the artist to control pickability
            // in a somewhat fine-grained style.
            const float modelGlobalOpacity = m_gnd->getGlobalOpacity(*model);
            const bool canModelBePickable = (modelGlobalOpacity > QSSGRendererPrivate::minimumRenderOpacity)
                    && (globalPickingEnabled
                        || model->getGlobalState(QSSGRenderModel::GlobalState::Pickable));
            if (canModelBePickable) {
                // Check if there is BVH data, if not generate it
                if (!theMesh->bvh) {
                    const QSSGMesh::Mesh mesh = bufferManager->loadLightmapMesh(*model);

                    if (mesh.isValid())
                        theMesh->bvh = bufferManager->loadMeshBVH(mesh);
                    else if (model->geometry)
                        theMesh->bvh = bufferManager->loadMeshBVH(model->geometry);
                    else if (!model->meshPath.isNull())
                        theMesh->bvh = bufferManager->loadMeshBVH(model->meshPath);

                    if (theMesh->bvh) {
                        const auto &roots = theMesh->bvh->roots();
                        for (qsizetype i = 0, end = qsizetype(roots.size()); i < end; ++i)
                            theMesh->subsets[i].bvhRoot = roots[i];
                    }
                }
            }
        } else {
            m_gnd->meshes[model->h.index()] = nullptr;
        }
    }

    // Now is the time to kick off the vertex/index buffer updates for all the
    // new meshes (and their submeshes). This here is the last possible place
    // to kick this off because the rest of the rendering pipeline will only
    // see the individual sub-objects as "renderable objects".
    bufferManager->commitBufferResourceUpdates();
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 563, as _ZN19QSSGRenderModelData16prepareMaterialsERK12QSSGDataViewIP15QSSGRenderModelE
inline void QSSGRenderModelData::prepareMaterials(const QSSGModelsView &models)
{
    for (auto *model : models)
        m_gnd->materials[model->h.index()] = model->materials;
}
//  -----------------------------------------------------------------------

//  QSSGRenderModelData::QSSGRenderModelData(const
//      QSSGGlobalRenderNodeDataPtr &globalNodeData)
extern "C" Q_DECL_EXPORT
QSSGRenderModelData *ritual_ZN19QSSGRenderModelDataC1ERKSt10shared_ptrI24QSSGGlobalRenderNodeDataE(
    const QSSGGlobalRenderNodeDataPtr *globalNodeData) {
  return new QSSGRenderModelData(*globalNodeData);
}

//  ModelViewProjections
//      QSSGRenderModelData::getModelViewProjection(QSSGRenderNodeHandle h)
//      const
extern "C" Q_DECL_EXPORT
QSSGRenderModelData::ModelViewProjections *ritual_ZNK19QSSGRenderModelData22getModelViewProjectionE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGRenderModelData *self,
    const QSSGRenderNodeHandle *h) {
  return new QSSGRenderModelData::ModelViewProjections(
      self->getModelViewProjection(
          *h));
}

//  ModelViewProjections QSSGRenderModelData::getModelViewProjection(const
//      QSSGRenderModel &model) const
extern "C" Q_DECL_EXPORT
QSSGRenderModelData::ModelViewProjections *ritual_ZNK19QSSGRenderModelData22getModelViewProjectionERK15QSSGRenderModel(
    const QSSGRenderModelData *self,
    const QSSGRenderModel *model) {
  return new QSSGRenderModelData::ModelViewProjections(
      self->getModelViewProjection(
          *model));
}

//  QMatrix3x3 QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h,
//      QMatrix3x3 defaultValue) const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK19QSSGRenderModelData15getNormalMatrixE23QSSGRenderStorageHandleIL10HandleType1EE14QGenericMatrixILi3ELi3EfE(
    const QSSGRenderModelData *self,
    const QSSGRenderNodeHandle *h,
    const QMatrix3x3 *defaultValue) {
  return new QMatrix3x3(self->getNormalMatrix(*h, *defaultValue));
}

//  QMatrix3x3 QSSGRenderModelData::getNormalMatrix(const QSSGRenderModel
//      &model) const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK19QSSGRenderModelData15getNormalMatrixERK15QSSGRenderModel(
    const QSSGRenderModelData *self,
    const QSSGRenderModel *model) {
  return new QMatrix3x3(self->getNormalMatrix(*model));
}

//  QSSGRenderMesh *QSSGRenderModelData::getMesh(const QSSGRenderModel
//      &model) const
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZNK19QSSGRenderModelData7getMeshERK15QSSGRenderModel(
    const QSSGRenderModelData *self,
    const QSSGRenderModel *model) {
  return self->getMesh(*model);
}

//  MaterialList QSSGRenderModelData::getMaterials(const QSSGRenderModel
//      &model) const
extern "C" Q_DECL_EXPORT
QList<QSSGRenderGraphObject *> *ritual_ZNK19QSSGRenderModelData12getMaterialsERK15QSSGRenderModel(
    const QSSGRenderModelData *self,
    const QSSGRenderModel *model) {
  return new QList<QSSGRenderGraphObject *>(self->getMaterials(*model));
}

//  const QSSGGlobalRenderNodeDataPtr &QSSGRenderModelData::globalNodeData()
//      const
extern "C" Q_DECL_EXPORT
const QSSGGlobalRenderNodeDataPtr *ritual_ZNK19QSSGRenderModelData14globalNodeDataEv(
    const QSSGRenderModelData *self) {
  return &(self->globalNodeData());
}

//  quint32 QSSGRenderModelData::getThreadPoolThreshold()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN19QSSGRenderModelData22getThreadPoolThresholdEv() {
  return QSSGRenderModelData::getThreadPoolThreshold();
}

//  void QSSGRenderModelData::prepareMeshData(const QSSGModelsView &models,
//      QSSGRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderModelData15prepareMeshDataERK12QSSGDataViewIP15QSSGRenderModelEP12QSSGRenderer(
    QSSGRenderModelData *self,
    const QSSGModelsView *models,
    QSSGRenderer *renderer) {
  self->prepareMeshData(*models, renderer);
}

//  void QSSGRenderModelData::prepareMaterials(const QSSGModelsView &models)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderModelData16prepareMaterialsERK12QSSGDataViewIP15QSSGRenderModelE(
    QSSGRenderModelData *self,
    const QSSGModelsView *models) {
  self->prepareMaterials(*models);
}

//  a QSSGRenderModelData::ModelViewProjections a ritual of
//      QSSGRenderModelData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderModelData__QSSGRenderModelData_ModelViewProjections(
    QSSGRenderModelData::ModelViewProjections *self) {
  delete self;
}

//  a QMatrix3x3 a ritual of QSSGRenderModelData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderModelData__QMatrix3x3(QMatrix3x3 *self) {
  delete self;
}
