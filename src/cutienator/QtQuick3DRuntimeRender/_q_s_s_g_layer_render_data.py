"""
QSSGLayerRenderData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLayerRenderData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSSGRenderResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D
  from . import QSSGFrameData, QSSGOITRenderContext, QSSGRenderCamera
  from . import QSSGRenderCameraData, QSSGRenderContextInterface
  from . import QSSGRenderItem2D, QSSGRhiContext
  from . import QSSGRhiGraphicsPipelineState, QSSGRhiRenderableTexture
  from . import QSSGShaderDefaultMaterialKeyProperties, QSSGShaderFeatures
  from . import QSSGShaderParticleMaterialKeyProperties, QSSGSubsetRenderable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGFrameData = WAIT['QSSGFrameData']
  QSSGRenderCamera = WAIT['QSSGRenderCamera']
  QSSGRhiContext = WAIT['QSSGRhiContext']
  QSSGSubsetRenderable = WAIT['QSSGSubsetRenderable']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGLayerRenderData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLayerRenderData: a plain Python object standing
  in front of one C++ QSSGLayerRenderData.

  What exists
  -----------

  Every function of Qt's QSSGLayerRenderData that has a ritual and that
  Python can call so far, 23 names in all: 'prepareResourceLoaders',
  'prepareForRender', 'prepareReflectionProbesForRender',
  'getRenderableItem2Ds', 'resetForFrame', 'getShaderFeatures',
  'getPipelineState', 'maybeProcessLightmapBaking', 'activeCamera',
  'getCameraRenderData', 'contextInterface', 'isZPrePassActive',
  'setZPrePassPrepResult', 'getDefaultMaterialPropertyTable',
  'getParticleMaterialPropertyTable', 'getOitRenderContextConst',
  'prepareInstancing', 'getRenderResult', 'resolveLayerIblTexture',
  'getCameraDataImpl', 'getCurrent', 'updateFilteredLayerNodes',
  'ensureCachedCameraDatas'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLayerRenderData::QSSGLayerRenderData(QSSGRenderLayer &inLayer,
    QSSGRenderer &inRenderer)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGLayerRenderData::~QSSGLayerRenderData()': the destructor:
    Python never removes a C++ QSSGLayerRenderData.
  - Qt's 'void QSSGLayerRenderData::setVertexInputPresence(const
    QSSGRenderableObjectFlags &renderableFlags, QSSGShaderDefaultMaterialKey
    &key)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterface
    &ctx, const RenderableNodeEntries &renderableModels,
    QSSGLayerRenderPreparationResultFlags &ioFlags, const
    QSSGRenderCameraList &allCameras, const QSSGRenderCameraDataList
    &allCameraData, TModelContextPtrList &modelContexts,
    QSSGRenderableObjectList &opaqueObjects, QSSGRenderableObjectList
    &transparentObjects, QSSGRenderableObjectList &screenTextureObjects,
    float lodThreshold)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGLayerRenderData::prepareParticlesForRender(const
    RenderableNodeEntries &renderableParticles, const QSSGRenderCameraData
    &cameraData, QSSGLayerRenderPreparationResultFlags &ioFlags)': takes a
    type Python has no way to hand over yet.
  - Qt's 'qsizetype QSSGLayerRenderData::frustumCullingInline(const
    QSSGClippingFrustum &clipFrustum, QSSGRenderableObjectList
    &renderables)': takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype QSSGLayerRenderData::filterLayerMaskInline(quint32
    layerMask, QSSGRenderableObjectList &renderables)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedOpaqueRenderableObjects(const
    QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedTransparentRenderableObjects(const
    QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedScreenTextureRenderableObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const QVector<QSSGBakedLightingModel>
    &QSSGLayerRenderData::getSortedBakedLightingModels()': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedRenderedDepthWriteObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedrenderedOpaqueDepthPrepassObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QSSGLayerRenderData::getShadowCastingObjects(const
    QSSGRenderCamera &camera, QSSGRenderableObjectList &outObjects,
    QSSGBounds3 &outBoundsCasting, QSSGBounds3 &outBoundsReceiving)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGFrameData &QSSGLayerRenderData::getFrameData()': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QSSGLayerRenderData::initializeLightmapBaking(QSSGLightmapBaker::Context
    &ctx)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderGraphObject *QSSGLayerRenderData::getCamera(QSSGCameraId
    id) const': names the enum 'QSSGCameraId', whose class cannot be named
    here.
  - Qt's 'QSSGRenderCameraData QSSGLayerRenderData::getCameraRenderData(const
    QSSGRenderCamera *camera) const': takes in Python what
    'QSSGRenderCameraData QSSGLayerRenderData::getCameraRenderData(const
    QSSGRenderCamera *camera)' takes.
  - Qt's 'void QSSGLayerRenderData::setLightmapTexture(const QSSGModelContext
    &modelContext, QRhiTexture *lightmapTexture)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QRhiTexture *QSSGLayerRenderData::getLightmapTexture(const
    QSSGModelContext &modelContext) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGLayerRenderData::setBonemapTexture(const QSSGModelContext
    &modelContext, QRhiTexture *bonemapTexture)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QRhiTexture *QSSGLayerRenderData::getBonemapTexture(const
    QSSGModelContext &modelContext) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'GlobalRenderProperties
    QSSGLayerRenderData::globalRenderProperties(const
    QSSGRenderContextInterface &ctx)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QSSGRenderShadowMapPtr
    &QSSGLayerRenderData::requestShadowMapManager()': gives a type Python has
    no way to take yet.
  - Qt's 'const QSSGRenderReflectionMapPtr
    &QSSGLayerRenderData::requestReflectionMapManager()': gives a type Python
    has no way to take yet.
  - Qt's 'const QSSGRenderSkyMaterialManagerPtr
    &QSSGLayerRenderData::requestSkyMaterialManager()': gives a type Python
    has no way to take yet.
  - Qt's 'const QSSGUserRenderPassManagerPtr
    &QSSGLayerRenderData::requestUserRenderPassManager()': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGRenderMotionVectorMapPtr
    &QSSGLayerRenderData::requestMotionVectorMapManager()': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGRenderShadowMapPtr
    &QSSGLayerRenderData::getShadowMapManager() const': gives a type Python
    has no way to take yet.
  - Qt's 'const QSSGRenderReflectionMapPtr
    &QSSGLayerRenderData::getReflectionMapManager() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGRenderSkyMaterialManagerPtr
    &QSSGLayerRenderData::getSkyMaterialManager() const': gives a type Python
    has no way to take yet.
  - Qt's 'const QSSGUserRenderPassManagerPtr
    &QSSGLayerRenderData::getUserRenderPassManager() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QSSGRenderMotionVectorMapPtr
    &QSSGLayerRenderData::getMotionvectorMapManager() const': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGOITRenderContext &QSSGLayerRenderData::getOitRenderContext()':
    gives a type Python has no way to take yet.
  - Qt's 'const QSSGRhiRenderableTexture
    *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id) const':
    takes in Python what 'QSSGRhiRenderableTexture
    *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id)' takes.
  - Qt's 'const std::unique_ptr<QSSGPerFrameAllocator>
    &QSSGLayerRenderData::perFrameAllocator(QSSGRenderContextInterface
    &ctx)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const
    QSSGRenderer &renderer)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGLayerRenderData::saveRenderState(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGLayerRenderData::restoreRenderState(QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGLayerRenderData::setTonemapFeatures(QSSGShaderFeatures
    &features, QSSGRenderLayer::TonemapMode tonemapMode)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGPrepContextId
    QSSGLayerRenderData::getOrCreateExtensionContext(const
    QSSGRenderExtension &ext, QSSGRenderCamera *camera, quint32 slot)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderablesId
    QSSGLayerRenderData::createRenderables(QSSGPrepContextId prepId, const
    QSSGNodeIdList &nodes, QSSGRenderHelpers::CreateFlags createFlags)':
    names the enum 'QSSGPrepContextId', whose class cannot be named here.
  - Qt's 'void QSSGLayerRenderData::setGlobalTransform(QSSGRenderablesId
    renderablesId, const QSSGRenderModel &model, const QMatrix4x4 &mvp)':
    names the enum 'QSSGRenderablesId', whose class cannot be named here.
  - Qt's 'QMatrix4x4
    QSSGLayerRenderData::getGlobalTransform(QSSGPrepContextId prepId, const
    QSSGRenderModel &model)': names the enum 'QSSGPrepContextId', whose class
    cannot be named here.
  - Qt's 'void QSSGLayerRenderData::setGlobalOpacity(QSSGRenderablesId
    renderablesId, const QSSGRenderModel &model, float opacity)': names the
    enum 'QSSGRenderablesId', whose class cannot be named here.
  - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(QSSGPrepContextId
    prepId, const QSSGRenderModel &model)': names the enum
    'QSSGPrepContextId', whose class cannot be named here.
  - Qt's 'void QSSGLayerRenderData::setModelMaterials(QSSGRenderablesId
    renderablesId, const QSSGRenderModel &model, const QList<QSSGResourceId>
    &materials)': names the enum 'QSSGRenderablesId', whose class cannot be
    named here.
  - Qt's 'void QSSGLayerRenderData::setModelMaterials(const QSSGRenderablesId
    renderablesId, const QList<QSSGResourceId> &materials)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGPrepResultId
    QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterface
    &contextInterface, QSSGPrepContextId prepId, QSSGRenderablesId
    renderablesId, float lodThreshold)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QMatrix4x4
    QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h, const
    QMatrix4x4 &defaultValue) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QMatrix4x4
    QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(const
    QSSGRenderNode &node) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QMatrix3x3
    QSSGLayerRenderData::getNormalMatrix(QSSGRenderNodeHandle h) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMatrix3x3 QSSGLayerRenderData::getNormalMatrix(const
    QSSGRenderModel &model) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'InstanceTransforms
    QSSGLayerRenderData::getInstanceTransforms(QSSGRenderNodeHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'InstanceTransforms QSSGLayerRenderData::getInstanceTransforms(const
    QSSGRenderNode &node) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(QSSGRenderNodeHandle h,
    float defaultValue) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(const QSSGRenderNode
    &node) const': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderItem2DData::Item2DRenderer
    QSSGLayerRenderData::getItem2DRenderer(const QSSGRenderItem2D &item)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGLayerRenderData::prepareRenderables(QSSGRenderContextInterface &ctx,
    QSSGPrepResultId prepId, QRhiRenderPassDescriptor *renderPassDescriptor,
    const QSSGRhiGraphicsPipelineState &ps, QSSGRenderablesFilters filter)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGLayerRenderData::renderRenderables(QSSGRenderContextInterface &ctx,
    QSSGPrepResultId prepId)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGNodeIdList QSSGLayerRenderData::filter(const
    QSSGGlobalRenderNodeData::LayerNodeView &layerNodes, quint32 layerMask,
    quint32 typeMask)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGDefaultMaterialPreparationResult
    QSSGLayerRenderData::prepareDefaultMaterialForRender(
    QSSGRenderDefaultMaterial &inMaterial, QSSGRenderableObjectFlags
    &inExistingFlags, float inOpacity, bool hasAnyLights, bool
    anyLightHasShadows, QSSGLayerRenderPreparationResultFlags &ioFlags)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSSGDefaultMaterialPreparationResult
    QSSGLayerRenderData::prepareCustomMaterialForRender(
    QSSGRenderCustomMaterial &inMaterial, QSSGRenderableObjectFlags
    &inExistingFlags, float inOpacity, bool alreadyDirty, bool hasAnyLights,
    bool anyLightHasShadows, QSSGLayerRenderPreparationResultFlags
    &ioFlags)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGLayerRenderData::categorizeAndFilterNodes(const
    QSSGGlobalRenderNodeData::LayerNodeView &layerNodes,
    QSSGLayerRenderData::NodeCollection &nodeCollection, quint32 layerMask)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QSSGRenderCameraDataList
    &QSSGLayerRenderData::getCachedCameraDatas()': gives a type Python has no
    way to take yet.
  - Qt's 'void QSSGLayerRenderData::updateSortedDepthObjectsListImp(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  10 of the 100 functions Qt declares: 3 cannot be called and cannot be
  called through the meta-object and cannot be copied; 2 not a gap; 2 leans
  on 'QSSGRenderModelData; 2 leans on 'QSSGRenderItem2DData; 1 takes or gives
  a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QSSGLayerRenderData is created at the first use, not by
    'QSSGLayerRenderData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGLayerRenderData.
  - Each name of Qt's QSSGLayerRenderData that has no cute function yet,
    '__init__', 'calculateGlobalVariables', 'categorizeAndFilterNodes',
    'createRenderables', 'filter', 'filterLayerMaskInline',
    'frustumCullingInline', 'getBonemapTexture', 'getCachedCameraDatas',
    'getCamera', 'getFrameData', 'getGlobalOpacity', 'getGlobalTransform',
    'getInstanceTransforms', 'getItem2DMvps', 'getItem2DRenderer',
    'getLightmapTexture', 'getModelMvps', 'getMotionvectorMapManager',
    'getNormalMatrix', 'getOitRenderContext', 'getOrCreateExtensionContext',
    'getReflectionMapManager', 'getShadowCastingObjects',
    'getShadowMapManager', 'getSkyMaterialManager',
    'getSortedBakedLightingModels', 'getSortedOpaqueRenderableObjects',
    'getSortedRenderedDepthWriteObjects',
    'getSortedScreenTextureRenderableObjects',
    'getSortedTransparentRenderableObjects',
    'getSortedrenderedOpaqueDepthPrepassObjects', 'getUserRenderPassManager',
    'globalRenderProperties', 'initializeLightmapBaking',
    'perFrameAllocator', 'prepareCustomMaterialForRender',
    'prepareDefaultMaterialForRender', 'prepareImageForRender',
    'prepareModelBoneTextures', 'prepareModelsForRender',
    'prepareParticlesForRender', 'prepareRenderables', 'renderRenderables',
    'requestMotionVectorMapManager', 'requestReflectionMapManager',
    'requestShadowMapManager', 'requestSkyMaterialManager',
    'requestUserRenderPassManager', 'restoreRenderState', 'saveRenderState',
    'setBonemapTexture', 'setGlobalOpacity', 'setGlobalTransform',
    'setLightmapTexture', 'setModelMaterials', 'setTonemapFeatures',
    'setVertexInputPresence', 'updateSortedDepthObjectsListImp', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGLayerRenderData, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Enum(CuteNum):
    """
    The enum 'QSSGLayerRenderData::Enum' of Qt, with the 2 names Qt gives in
    it.
    """

    MAX_AA_LEVELS = Kee[int](8)
    MAX_TEMPORAL_AA_LEVELS = Kee[int](2)

  #  The classes Qt writes inside QSSGLayerRenderData, each a class in here
  #  as in C++.

  class GlobalRenderProperties(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGLayerRenderData::GlobalRenderProperties: a
    plain Python object standing in front of one C++
    QSSGLayerRenderData::GlobalRenderProperties.

    C++ hands a QSSGLayerRenderData::GlobalRenderProperties around as a copy,
    so every C++ QSSGLayerRenderData::GlobalRenderProperties behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGLayerRenderData::GlobalRenderProperties yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGLayerRenderData::GlobalRenderProperties::~GlobalRenderProperties(
      )': the destructor: Python removes its C++
      QSSGLayerRenderData::GlobalRenderProperties by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGLayerRenderData::GlobalRenderProperties is created at the
      first use, not by 'QSSGLayerRenderData::GlobalRenderProperties(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGLayerRenderData::GlobalRenderProperties back
      gives a copy the ritual made for Python, in a new cute
      QSSGLayerRenderData::GlobalRenderProperties.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGLayerRenderData::GlobalRenderProperties'

    #  Qt's '~QSSGLayerRenderData::GlobalRenderProperties()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGLayerRenderData::GlobalRenderProperties behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QSSGLayerRenderData22GlobalRenderPropertiesD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class NodeCollection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGLayerRenderData::NodeCollection: a plain Python
    object standing in front of one C++ QSSGLayerRenderData::NodeCollection.

    What exists
    -----------

    No function of Qt's QSSGLayerRenderData::NodeCollection yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has no ritual
    ------------------

    2 of the 3 functions Qt declares: 2 forbidden.

    What to expect
    --------------

    - The C++ QSSGLayerRenderData::NodeCollection is created at the first
      use, not by 'QSSGLayerRenderData::NodeCollection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QSSGLayerRenderData::NodeCollection.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGLayerRenderData::NodeCollection'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSSGLayerRenderData::NodeCollection::NodeCollection()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssglayerrenderdata-nodecollection.html
      """
      #  QSSGLayerRenderData::NodeCollection::NodeCollection()
      self._noteCreation(
          QSSGLayerRenderData.NodeCollection, lambda: Rituals.call(
              'ritual_ZN19QSSGLayerRenderData14NodeCollectionC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QSSGRhiContext, QSSGSubsetRenderable, QVector3D, QVector3D, float,
      float,
  )
  @overload(QSSGRhiContext, NoneType, QVector3D, QVector3D, float, float)
  @overload(
      NoneType, QSSGSubsetRenderable, QVector3D, QVector3D, float, float,
  )
  @overload(NoneType, NoneType, QVector3D, QVector3D, float, float)
  def prepareInstancing(
      rhiCtx: Optional[QSSGRhiContext],
      renderable: Optional[QSSGSubsetRenderable],
      cameraDirection: QVector3D,
      cameraPosition: QVector3D,
      minThreshold: float,
      maxThreshold: float,
  ) -> bool:
    """
    Calls Qt's 'bool QSSGLayerRenderData::prepareInstancing(QSSGRhiContext
    *rhiCtx, QSSGSubsetRenderable *renderable, const QVector3D
    &cameraDirection, const QVector3D &cameraPosition, float minThreshold,
    float maxThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#prepareInstancing

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderable : Optional[QSSGSubsetRenderable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cameraDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    cameraPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    minThreshold : float
      Passed on as it is.

    maxThreshold : float
      Passed on as it is.
    """
    #  bool QSSGLayerRenderData::prepareInstancing(QSSGRhiContext *rhiCtx,
    #      QSSGSubsetRenderable *renderable, const QVector3D
    #      &cameraDirection, const QVector3D &cameraPosition, float
    #      minThreshold, float maxThreshold)
    return Rituals.call(
        'ritual_ZN19QSSGLayerRenderData17prepareInstancingEP14QSSGRhiContex'
        'tP20QSSGSubsetRenderableRK9QVector3DS6_ff',
        CuteMixin._addressOf(rhiCtx), CuteMixin._addressOf(renderable),
        CuteMixin._valueOf(cameraDirection),
        CuteMixin._valueOf(cameraPosition), minThreshold, maxThreshold,
    )

  @staticmethod
  @overload(QSSGFrameData)
  def getCurrent(data: QSSGFrameData) -> Optional[QSSGLayerRenderData]:
    """
    Calls Qt's 'QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const
    QSSGFrameData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getCurrent

    Parameters
    ----------

    data : QSSGFrameData
      Passed on as a value: Qt reads the C++ QSSGFrameData, which stays
      Python's own.

    Returns
    -------

    Optional[QSSGLayerRenderData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const
    #      QSSGFrameData &data)
    address = Rituals.call(
        'ritual_ZN19QSSGLayerRenderData10getCurrentERK13QSSGFrameData',
        CuteMixin._valueOf(data),
    )
    return QSSGLayerRenderData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGLayerRenderData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getShaderFeatures(self) -> QSSGShaderFeatures:
    """
    Calls Qt's 'QSSGShaderFeatures QSSGLayerRenderData::getShaderFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getShaderFeatures

    Returns
    -------

    QSSGShaderFeatures
      A new cute QSSGShaderFeatures around the copy Qt gave back. Python owns
      it.
    """
    #  QSSGShaderFeatures QSSGLayerRenderData::getShaderFeatures() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData17getShaderFeaturesEv',
    )
    from . import QSSGShaderFeatures
    return QSSGShaderFeatures._cuteOwning(address)

  def getPipelineState(self) -> QSSGRhiGraphicsPipelineState:
    """
    Calls Qt's 'QSSGRhiGraphicsPipelineState
    QSSGLayerRenderData::getPipelineState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getPipelineState

    Returns
    -------

    QSSGRhiGraphicsPipelineState
      A new cute QSSGRhiGraphicsPipelineState around the copy Qt gave back.
      Python owns it.
    """
    #  QSSGRhiGraphicsPipelineState QSSGLayerRenderData::getPipelineState()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData16getPipelineStateEv',
    )
    from . import QSSGRhiGraphicsPipelineState
    return QSSGRhiGraphicsPipelineState._cuteOwning(address)

  def activeCamera(self) -> Optional[QSSGRenderCamera]:
    """
    Calls Qt's 'QSSGRenderCamera *QSSGLayerRenderData::activeCamera() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#activeCamera

    Returns
    -------

    Optional[QSSGRenderCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderCamera *QSSGLayerRenderData::activeCamera() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData12activeCameraEv',
    )
    from . import QSSGRenderCamera
    return QSSGRenderCamera._cuteAt(address)

  def contextInterface(self) -> Optional[QSSGRenderContextInterface]:
    """
    Calls Qt's 'QSSGRenderContextInterface
    *QSSGLayerRenderData::contextInterface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#contextInterface

    Returns
    -------

    Optional[QSSGRenderContextInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderContextInterface *QSSGLayerRenderData::contextInterface()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData16contextInterfaceEv',
    )
    from . import QSSGRenderContextInterface
    return QSSGRenderContextInterface._cuteAt(address)

  def isZPrePassActive(self) -> bool:
    """
    Calls Qt's 'bool QSSGLayerRenderData::isZPrePassActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#isZPrePassActive
    """
    #  bool QSSGLayerRenderData::isZPrePassActive() const
    return self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData16isZPrePassActiveEv',
    )

  def getDefaultMaterialPropertyTable(
      self,
  ) -> QSSGShaderDefaultMaterialKeyProperties:
    """
    Calls Qt's 'const QSSGShaderDefaultMaterialKeyProperties
    &QSSGLayerRenderData::getDefaultMaterialPropertyTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html

    Returns
    -------

    QSSGShaderDefaultMaterialKeyProperties
      A new cute QSSGShaderDefaultMaterialKeyProperties around the copy Qt
      gave back. Python owns it.
    """
    #  const QSSGShaderDefaultMaterialKeyProperties
    #      &QSSGLayerRenderData::getDefaultMaterialPropertyTable() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData31getDefaultMaterialPropertyTableEv',
    )
    from . import QSSGShaderDefaultMaterialKeyProperties
    return QSSGShaderDefaultMaterialKeyProperties._cuteOwning(address)

  def getParticleMaterialPropertyTable(
      self,
  ) -> QSSGShaderParticleMaterialKeyProperties:
    """
    Calls Qt's 'const QSSGShaderParticleMaterialKeyProperties
    &QSSGLayerRenderData::getParticleMaterialPropertyTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html

    Returns
    -------

    QSSGShaderParticleMaterialKeyProperties
      A new cute QSSGShaderParticleMaterialKeyProperties around the copy Qt
      gave back. Python owns it.
    """
    #  const QSSGShaderParticleMaterialKeyProperties
    #      &QSSGLayerRenderData::getParticleMaterialPropertyTable() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData32getParticleMaterialPropertyTableE'
        'v',
    )
    from . import QSSGShaderParticleMaterialKeyProperties
    return QSSGShaderParticleMaterialKeyProperties._cuteOwning(address)

  def getOitRenderContextConst(self) -> QSSGOITRenderContext:
    """
    Calls Qt's 'const QSSGOITRenderContext
    &QSSGLayerRenderData::getOitRenderContextConst() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getOitRenderContextConst

    Returns
    -------

    QSSGOITRenderContext
      A new cute QSSGOITRenderContext around the copy Qt gave back. Python
      owns it.
    """
    #  const QSSGOITRenderContext
    #      &QSSGLayerRenderData::getOitRenderContextConst() const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData24getOitRenderContextConstEv',
    )
    from . import QSSGOITRenderContext
    return QSSGOITRenderContext._cuteOwning(address)

  @overload(QSSGRenderCamera)
  @overload(NoneType)
  def getCameraDataImpl(
      self,
      camera: Optional[QSSGRenderCamera],
  ) -> QSSGRenderCameraData:
    """
    Calls Qt's 'QSSGRenderCameraData
    QSSGLayerRenderData::getCameraDataImpl(const QSSGRenderCamera *camera)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getCameraDataImpl

    Parameters
    ----------

    camera : Optional[QSSGRenderCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGRenderCameraData
      A new cute QSSGRenderCameraData around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderCameraData QSSGLayerRenderData::getCameraDataImpl(const
    #      QSSGRenderCamera *camera) const
    address = self.uglySide.call(
        'ritual_ZNK19QSSGLayerRenderData17getCameraDataImplEPK16QSSGRenderC'
        'amera',
        self._addressOf(camera),
    )
    from . import QSSGRenderCameraData
    return QSSGRenderCameraData._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setZPrePassPrepResult(self, res: bool) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::setZPrePassPrepResult(bool res)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#setZPrePassPrepResult

    Parameters
    ----------

    res : bool
      Passed on as it is.
    """
    #  void QSSGLayerRenderData::setZPrePassPrepResult(bool res)
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData21setZPrePassPrepResultEb', res,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGLayerRenderData::QSSGLayerRenderData(QSSGRenderLayer &inLayer,
    QSSGRenderer &inRenderer)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.__init__' has no cute function yet. Qt's "
        "'QSSGLayerRenderData::QSSGLayerRenderData(QSSGRenderLayer "
        "&inLayer, QSSGRenderer &inRenderer)': takes a type Python has no "
        "way to hand over yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def prepareResourceLoaders(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::prepareResourceLoaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#prepareResourceLoaders
    """
    #  void QSSGLayerRenderData::prepareResourceLoaders()
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData22prepareResourceLoadersEv',
    )

  def prepareForRender(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::prepareForRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#prepareForRender
    """
    #  void QSSGLayerRenderData::prepareForRender()
    self.uglySide.call('ritual_ZN19QSSGLayerRenderData16prepareForRenderEv')

  def prepareReflectionProbesForRender(self) -> None:
    """
    Calls Qt's 'void
    QSSGLayerRenderData::prepareReflectionProbesForRender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html
    """
    #  void QSSGLayerRenderData::prepareReflectionProbesForRender()
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData32prepareReflectionProbesForRenderEv',
    )

  def getRenderableItem2Ds(self) -> QList[QSSGRenderItem2D]:
    """
    Calls Qt's 'const RenderableItem2DEntries
    &QSSGLayerRenderData::getRenderableItem2Ds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getRenderableItem2Ds

    Returns
    -------

    QList[QSSGRenderItem2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const RenderableItem2DEntries
    #      &QSSGLayerRenderData::getRenderableItem2Ds()
    address = self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData20getRenderableItem2DsEv',
    )
    from . import QSSGRenderItem2D
    return QList[QSSGRenderItem2D]._cuteOwning(address)

  def resetForFrame(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::resetForFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#resetForFrame
    """
    #  void QSSGLayerRenderData::resetForFrame()
    self.uglySide.call('ritual_ZN19QSSGLayerRenderData13resetForFrameEv')

  def maybeProcessLightmapBaking(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::maybeProcessLightmapBaking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html
    """
    #  void QSSGLayerRenderData::maybeProcessLightmapBaking()
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData26maybeProcessLightmapBakingEv',
    )

  @overload(QSSGRenderCamera)
  @overload(NoneType)
  def getCameraRenderData(
      self,
      camera: Optional[QSSGRenderCamera],
  ) -> QSSGRenderCameraData:
    """
    Calls Qt's 'QSSGRenderCameraData
    QSSGLayerRenderData::getCameraRenderData(const QSSGRenderCamera
    *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getCameraRenderData

    Parameters
    ----------

    camera : Optional[QSSGRenderCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGRenderCameraData
      A new cute QSSGRenderCameraData around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderCameraData QSSGLayerRenderData::getCameraRenderData(const
    #      QSSGRenderCamera *camera)
    address = self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData19getCameraRenderDataEPK16QSSGRender'
        'Camera',
        self._addressOf(camera),
    )
    from . import QSSGRenderCameraData
    return QSSGRenderCameraData._cuteOwning(address)

  @overload(QSSGRenderResult.Key)
  def getRenderResult(
      self,
      id: QSSGRenderResult.Key,
  ) -> Optional[QSSGRhiRenderableTexture]:
    """
    Calls Qt's 'QSSGRhiRenderableTexture
    *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#getRenderResult

    Parameters
    ----------

    id : QSSGRenderResult.Key
      Passed on as its number.

    Returns
    -------

    Optional[QSSGRhiRenderableTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRhiRenderableTexture
    #      *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id)
    address = self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData15getRenderResultEN16QSSGRenderResul'
        't3KeyE',
        id.value,
    )
    from . import QSSGRhiRenderableTexture
    return QSSGRhiRenderableTexture._cuteAt(address)

  def resolveLayerIblTexture(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::resolveLayerIblTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#resolveLayerIblTexture
    """
    #  void QSSGLayerRenderData::resolveLayerIblTexture()
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData22resolveLayerIblTextureEv',
    )

  @overload(int)
  def updateFilteredLayerNodes(self, layerMask: int) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::updateFilteredLayerNodes(quint32
    layerMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#updateFilteredLayerNodes

    Parameters
    ----------

    layerMask : int
      Passed on as it is.
    """
    #  void QSSGLayerRenderData::updateFilteredLayerNodes(quint32 layerMask)
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData24updateFilteredLayerNodesEj',
        layerMask,
    )

  def ensureCachedCameraDatas(self) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderData::ensureCachedCameraDatas()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderdata.html#ensureCachedCameraDatas
    """
    #  void QSSGLayerRenderData::ensureCachedCameraDatas()
    self.uglySide.call(
        'ritual_ZN19QSSGLayerRenderData23ensureCachedCameraDatasEv',
    )

  @staticmethod
  def calculateGlobalVariables(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLayerRenderData::calculateGlobalVariables(QSSGRenderNode
    &node, std::vector<QMatrix4x4> &globalTransforms, std::vector<float>
    &globalOpacities)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.calculateGlobalVariables' has no cute "
        "function yet. Qt's 'bool "
        "QSSGLayerRenderData::calculateGlobalVariables(QSSGRenderNode "
        "&node, std::vector<QMatrix4x4> &globalTransforms, "
        "std::vector<float> &globalOpacities)': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def categorizeAndFilterNodes(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::categorizeAndFilterNodes(const
    QSSGGlobalRenderNodeData::LayerNodeView &layerNodes,
    QSSGLayerRenderData::NodeCollection &nodeCollection, quint32 layerMask)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.categorizeAndFilterNodes' has no cute "
        "function yet. Qt's 'void "
        "QSSGLayerRenderData::categorizeAndFilterNodes(const "
        "QSSGGlobalRenderNodeData::LayerNodeView &layerNodes, "
        "QSSGLayerRenderData::NodeCollection &nodeCollection, quint32 "
        "layerMask)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createRenderables(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderablesId
    QSSGLayerRenderData::createRenderables(QSSGPrepContextId prepId, const
    QSSGNodeIdList &nodes, QSSGRenderHelpers::CreateFlags createFlags)':
    names the enum 'QSSGPrepContextId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.createRenderables' has no cute function yet. "
        "Qt's 'QSSGRenderablesId "
        "QSSGLayerRenderData::createRenderables(QSSGPrepContextId prepId, "
        "const QSSGNodeIdList &nodes, QSSGRenderHelpers::CreateFlags "
        "createFlags)': names the enum 'QSSGPrepContextId', whose class "
        "cannot be named here.")

  @staticmethod
  def filter(*__, **_) -> Never:
    """
    Qt's 'QSSGNodeIdList QSSGLayerRenderData::filter(const
    QSSGGlobalRenderNodeData::LayerNodeView &layerNodes, quint32 layerMask,
    quint32 typeMask)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.filter' has no cute function yet. Qt's "
        "'QSSGNodeIdList QSSGLayerRenderData::filter(const "
        "QSSGGlobalRenderNodeData::LayerNodeView &layerNodes, quint32 "
        "layerMask, quint32 typeMask)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def filterLayerMaskInline(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSSGLayerRenderData::filterLayerMaskInline(quint32
    layerMask, QSSGRenderableObjectList &renderables)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.filterLayerMaskInline' has no cute function "
        "yet. Qt's 'qsizetype "
        "QSSGLayerRenderData::filterLayerMaskInline(quint32 layerMask, "
        "QSSGRenderableObjectList &renderables)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def frustumCullingInline(*__, **_) -> Never:
    """
    Qt's 'qsizetype QSSGLayerRenderData::frustumCullingInline(const
    QSSGClippingFrustum &clipFrustum, QSSGRenderableObjectList
    &renderables)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.frustumCullingInline' has no cute function "
        "yet. Qt's 'qsizetype "
        "QSSGLayerRenderData::frustumCullingInline(const "
        "QSSGClippingFrustum &clipFrustum, QSSGRenderableObjectList "
        "&renderables)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getBonemapTexture(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture *QSSGLayerRenderData::getBonemapTexture(const
    QSSGModelContext &modelContext) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getBonemapTexture' has no cute function yet. "
        "Qt's 'QRhiTexture *QSSGLayerRenderData::getBonemapTexture(const "
        "QSSGModelContext &modelContext) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def getCachedCameraDatas(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderCameraDataList
    &QSSGLayerRenderData::getCachedCameraDatas()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getCachedCameraDatas' has no cute function "
        "yet. Qt's 'const QSSGRenderCameraDataList "
        "&QSSGLayerRenderData::getCachedCameraDatas()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def getCamera(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderGraphObject *QSSGLayerRenderData::getCamera(QSSGCameraId
    id) const': names the enum 'QSSGCameraId', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getCamera' has no cute function yet. Qt's "
        "'QSSGRenderGraphObject "
        "*QSSGLayerRenderData::getCamera(QSSGCameraId id) const': names the "
        "enum 'QSSGCameraId', whose class cannot be named here.")

  @staticmethod
  def getFrameData(*__, **_) -> Never:
    """
    Qt's 'QSSGFrameData &QSSGLayerRenderData::getFrameData()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getFrameData' has no cute function yet. Qt's "
        "'QSSGFrameData &QSSGLayerRenderData::getFrameData()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getGlobalOpacity(*__, **_) -> Never:
    """
    - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(QSSGPrepContextId
      prepId, const QSSGRenderModel &model)': names the enum
      'QSSGPrepContextId', whose class cannot be named here.
    - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(QSSGRenderNodeHandle
      h, float defaultValue) const': takes a type Python has no way to hand
      over yet.
    - Qt's 'float QSSGLayerRenderData::getGlobalOpacity(const QSSGRenderNode
      &node) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getGlobalOpacity' has no cute function yet. "
        "Qt's 'float "
        "QSSGLayerRenderData::getGlobalOpacity(QSSGPrepContextId prepId, "
        "const QSSGRenderModel &model)': names the enum "
        "'QSSGPrepContextId', whose class cannot be named here. Qt's 'float "
        "QSSGLayerRenderData::getGlobalOpacity(QSSGRenderNodeHandle h, "
        "float defaultValue) const': takes a type Python has no way to hand "
        "over yet. Qt's 'float QSSGLayerRenderData::getGlobalOpacity(const "
        "QSSGRenderNode &node) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getGlobalTransform(*__, **_) -> Never:
    """
    - Qt's 'QMatrix4x4
      QSSGLayerRenderData::getGlobalTransform(QSSGPrepContextId prepId, const
      QSSGRenderModel &model)': names the enum 'QSSGPrepContextId', whose
      class cannot be named here.
    - Qt's 'QMatrix4x4
      QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h, const
      QMatrix4x4 &defaultValue) const': takes a type Python has no way to
      hand over yet.
    - Qt's 'QMatrix4x4
      QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h) const':
      takes a type Python has no way to hand over yet.
    - Qt's 'QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(const
      QSSGRenderNode &node) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getGlobalTransform' has no cute function yet. "
        "Qt's 'QMatrix4x4 "
        "QSSGLayerRenderData::getGlobalTransform(QSSGPrepContextId prepId, "
        "const QSSGRenderModel &model)': names the enum "
        "'QSSGPrepContextId', whose class cannot be named here. Qt's "
        "'QMatrix4x4 "
        "QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h, "
        "const QMatrix4x4 &defaultValue) const': takes a type Python has no "
        "way to hand over yet. Qt's 'QMatrix4x4 "
        "QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle h) "
        "const': takes a type Python has no way to hand over yet. Qt's "
        "'QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(const "
        "QSSGRenderNode &node) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getInstanceTransforms(*__, **_) -> Never:
    """
    - Qt's 'InstanceTransforms
      QSSGLayerRenderData::getInstanceTransforms(QSSGRenderNodeHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'InstanceTransforms
      QSSGLayerRenderData::getInstanceTransforms(const QSSGRenderNode &node)
      const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getInstanceTransforms' has no cute function "
        "yet. Qt's 'InstanceTransforms "
        "QSSGLayerRenderData::getInstanceTransforms(QSSGRenderNodeHandle h) "
        "const': takes a type Python has no way to hand over yet. Qt's "
        "'InstanceTransforms "
        "QSSGLayerRenderData::getInstanceTransforms(const QSSGRenderNode "
        "&node) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getItem2DMvps(*__, **_) -> Never:
    """
    - Qt's 'ModelViewProjections
      QSSGLayerRenderData::getItem2DMvps(QSSGRenderNodeHandle h) const':
      leans on
      'QSSGRenderItem2DData::getModelViewProjection(QSSGRenderStorageHandle<(
      HandleType)1>) const', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'ModelViewProjections QSSGLayerRenderData::getItem2DMvps(const
      QSSGRenderItem2D &item) const': leans on
      'QSSGRenderItem2DData::getModelViewProjection(QSSGRenderItem2D const&)
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getItem2DMvps' has no cute function yet. Qt's "
        "'ModelViewProjections "
        "QSSGLayerRenderData::getItem2DMvps(QSSGRenderNodeHandle h) const': "
        "leans on "
        "'QSSGRenderItem2DData::getModelViewProjection(QSSGRenderStorageHand"
        "le<(HandleType)1>) const', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'ModelViewProjections QSSGLayerRenderData::getItem2DMvps(const "
        "QSSGRenderItem2D &item) const': leans on "
        "'QSSGRenderItem2DData::getModelViewProjection(QSSGRenderItem2D "
        "const&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def getItem2DRenderer(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderItem2DData::Item2DRenderer
    QSSGLayerRenderData::getItem2DRenderer(const QSSGRenderItem2D &item)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getItem2DRenderer' has no cute function yet. "
        "Qt's 'QSSGRenderItem2DData::Item2DRenderer "
        "QSSGLayerRenderData::getItem2DRenderer(const QSSGRenderItem2D "
        "&item) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getLightmapTexture(*__, **_) -> Never:
    """
    Qt's 'QRhiTexture *QSSGLayerRenderData::getLightmapTexture(const
    QSSGModelContext &modelContext) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getLightmapTexture' has no cute function yet. "
        "Qt's 'QRhiTexture *QSSGLayerRenderData::getLightmapTexture(const "
        "QSSGModelContext &modelContext) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def getModelMvps(*__, **_) -> Never:
    """
    - Qt's 'QMatrix4x4 QSSGLayerRenderData::getModelMvps(QSSGPrepContextId
      prepId, const QSSGRenderModel &model) const': cannot be called and
      cannot be called through the meta-object and cannot be copied: no
      header file has its code, Qt's source does not mark it or its class for
      use from outside Qt or writes it 'inline' or nowhere, and it is no
      signal, slot or invokable function giving back nothing, of a class
      built on QObject, and Qt's source has no code for it that could be told
      from the rest.
    - Qt's 'ModelViewProjections
      QSSGLayerRenderData::getModelMvps(QSSGRenderNodeHandle h) const': leans
      on
      'QSSGRenderModelData::getModelViewProjection(QSSGRenderStorageHandle<(
      HandleType)1>) const', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'ModelViewProjections QSSGLayerRenderData::getModelMvps(const
      QSSGRenderModel &model) const': leans on
      'QSSGRenderModelData::getModelViewProjection(QSSGRenderModel const&)
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getModelMvps' has no cute function yet. Qt's "
        "'QMatrix4x4 QSSGLayerRenderData::getModelMvps(QSSGPrepContextId "
        "prepId, const QSSGRenderModel &model) const': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest. Qt's "
        "'ModelViewProjections "
        "QSSGLayerRenderData::getModelMvps(QSSGRenderNodeHandle h) const': "
        "leans on "
        "'QSSGRenderModelData::getModelViewProjection(QSSGRenderStorageHandl"
        "e<(HandleType)1>) const', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'ModelViewProjections QSSGLayerRenderData::getModelMvps(const "
        "QSSGRenderModel &model) const': leans on "
        "'QSSGRenderModelData::getModelViewProjection(QSSGRenderModel "
        "const&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def getMotionvectorMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderMotionVectorMapPtr
    &QSSGLayerRenderData::getMotionvectorMapManager() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getMotionvectorMapManager' has no cute "
        "function yet. Qt's 'const QSSGRenderMotionVectorMapPtr "
        "&QSSGLayerRenderData::getMotionvectorMapManager() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getNormalMatrix(*__, **_) -> Never:
    """
    - Qt's 'QMatrix3x3
      QSSGLayerRenderData::getNormalMatrix(QSSGRenderNodeHandle h) const':
      takes a type Python has no way to hand over yet.
    - Qt's 'QMatrix3x3 QSSGLayerRenderData::getNormalMatrix(const
      QSSGRenderModel &model) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getNormalMatrix' has no cute function yet. "
        "Qt's 'QMatrix3x3 "
        "QSSGLayerRenderData::getNormalMatrix(QSSGRenderNodeHandle h) "
        "const': takes a type Python has no way to hand over yet. Qt's "
        "'QMatrix3x3 QSSGLayerRenderData::getNormalMatrix(const "
        "QSSGRenderModel &model) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getOitRenderContext(*__, **_) -> Never:
    """
    Qt's 'QSSGOITRenderContext &QSSGLayerRenderData::getOitRenderContext()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getOitRenderContext' has no cute function "
        "yet. Qt's 'QSSGOITRenderContext "
        "&QSSGLayerRenderData::getOitRenderContext()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def getOrCreateExtensionContext(*__, **_) -> Never:
    """
    Qt's 'QSSGPrepContextId
    QSSGLayerRenderData::getOrCreateExtensionContext(const
    QSSGRenderExtension &ext, QSSGRenderCamera *camera, quint32 slot)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getOrCreateExtensionContext' has no cute "
        "function yet. Qt's 'QSSGPrepContextId "
        "QSSGLayerRenderData::getOrCreateExtensionContext(const "
        "QSSGRenderExtension &ext, QSSGRenderCamera *camera, quint32 "
        "slot)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getReflectionMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderReflectionMapPtr
    &QSSGLayerRenderData::getReflectionMapManager() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getReflectionMapManager' has no cute function "
        "yet. Qt's 'const QSSGRenderReflectionMapPtr "
        "&QSSGLayerRenderData::getReflectionMapManager() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getShadowCastingObjects(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::getShadowCastingObjects(const
    QSSGRenderCamera &camera, QSSGRenderableObjectList &outObjects,
    QSSGBounds3 &outBoundsCasting, QSSGBounds3 &outBoundsReceiving)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getShadowCastingObjects' has no cute function "
        "yet. Qt's 'void QSSGLayerRenderData::getShadowCastingObjects(const "
        "QSSGRenderCamera &camera, QSSGRenderableObjectList &outObjects, "
        "QSSGBounds3 &outBoundsCasting, QSSGBounds3 &outBoundsReceiving)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def getShadowMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderShadowMapPtr
    &QSSGLayerRenderData::getShadowMapManager() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getShadowMapManager' has no cute function "
        "yet. Qt's 'const QSSGRenderShadowMapPtr "
        "&QSSGLayerRenderData::getShadowMapManager() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getSkyMaterialManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderSkyMaterialManagerPtr
    &QSSGLayerRenderData::getSkyMaterialManager() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSkyMaterialManager' has no cute function "
        "yet. Qt's 'const QSSGRenderSkyMaterialManagerPtr "
        "&QSSGLayerRenderData::getSkyMaterialManager() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getSortedBakedLightingModels(*__, **_) -> Never:
    """
    Qt's 'const QVector<QSSGBakedLightingModel>
    &QSSGLayerRenderData::getSortedBakedLightingModels()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedBakedLightingModels' has no cute "
        "function yet. Qt's 'const QVector<QSSGBakedLightingModel> "
        "&QSSGLayerRenderData::getSortedBakedLightingModels()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getSortedOpaqueRenderableObjects(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedOpaqueRenderableObjects(const
    QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedOpaqueRenderableObjects' has no cute "
        "function yet. Qt's 'const QSSGRenderableObjectList "
        "&QSSGLayerRenderData::getSortedOpaqueRenderableObjects(const "
        "QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def getSortedRenderedDepthWriteObjects(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedRenderedDepthWriteObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedRenderedDepthWriteObjects' has no "
        "cute function yet. Qt's 'const QSSGRenderableObjectList "
        "&QSSGLayerRenderData::getSortedRenderedDepthWriteObjects(const "
        "QSSGRenderCamera &camera, size_t index)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def getSortedScreenTextureRenderableObjects(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedScreenTextureRenderableObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedScreenTextureRenderableObjects' has "
        "no cute function yet. Qt's 'const QSSGRenderableObjectList "
        "&QSSGLayerRenderData::getSortedScreenTextureRenderableObjects(const"
        " QSSGRenderCamera &camera, size_t index)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def getSortedTransparentRenderableObjects(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedTransparentRenderableObjects(const
    QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedTransparentRenderableObjects' has no "
        "cute function yet. Qt's 'const QSSGRenderableObjectList "
        "&QSSGLayerRenderData::getSortedTransparentRenderableObjects(const "
        "QSSGRenderCamera &camera, size_t index, quint32 layerMask)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def getSortedrenderedOpaqueDepthPrepassObjects(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderableObjectList
    &QSSGLayerRenderData::getSortedrenderedOpaqueDepthPrepassObjects(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getSortedrenderedOpaqueDepthPrepassObjects' "
        "has no cute function yet. Qt's 'const QSSGRenderableObjectList "
        "&QSSGLayerRenderData::getSortedrenderedOpaqueDepthPrepassObjects(co"
        "nst QSSGRenderCamera &camera, size_t index)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def getUserRenderPassManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGUserRenderPassManagerPtr
    &QSSGLayerRenderData::getUserRenderPassManager() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.getUserRenderPassManager' has no cute "
        "function yet. Qt's 'const QSSGUserRenderPassManagerPtr "
        "&QSSGLayerRenderData::getUserRenderPassManager() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def globalRenderProperties(*__, **_) -> Never:
    """
    Qt's 'GlobalRenderProperties
    QSSGLayerRenderData::globalRenderProperties(const
    QSSGRenderContextInterface &ctx)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.globalRenderProperties' has no cute function "
        "yet. Qt's 'GlobalRenderProperties "
        "QSSGLayerRenderData::globalRenderProperties(const "
        "QSSGRenderContextInterface &ctx)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def initializeLightmapBaking(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGLayerRenderData::initializeLightmapBaking(QSSGLightmapBaker::Context
    &ctx)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.initializeLightmapBaking' has no cute "
        "function yet. Qt's 'void "
        "QSSGLayerRenderData::initializeLightmapBaking(QSSGLightmapBaker::Co"
        "ntext &ctx)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def perFrameAllocator(*__, **_) -> Never:
    """
    Qt's 'const std::unique_ptr<QSSGPerFrameAllocator>
    &QSSGLayerRenderData::perFrameAllocator(QSSGRenderContextInterface
    &ctx)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.perFrameAllocator' has no cute function yet. "
        "Qt's 'const std::unique_ptr<QSSGPerFrameAllocator> "
        "&QSSGLayerRenderData::perFrameAllocator(QSSGRenderContextInterface "
        "&ctx)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def prepareCustomMaterialForRender(*__, **_) -> Never:
    """
    Qt's 'QSSGDefaultMaterialPreparationResult
    QSSGLayerRenderData::prepareCustomMaterialForRender(
    QSSGRenderCustomMaterial &inMaterial, QSSGRenderableObjectFlags
    &inExistingFlags, float inOpacity, bool alreadyDirty, bool hasAnyLights,
    bool anyLightHasShadows, QSSGLayerRenderPreparationResultFlags
    &ioFlags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareCustomMaterialForRender' has no cute "
        "function yet. Qt's 'QSSGDefaultMaterialPreparationResult "
        "QSSGLayerRenderData::prepareCustomMaterialForRender(QSSGRenderCusto"
        "mMaterial &inMaterial, QSSGRenderableObjectFlags &inExistingFlags, "
        "float inOpacity, bool alreadyDirty, bool hasAnyLights, bool "
        "anyLightHasShadows, QSSGLayerRenderPreparationResultFlags "
        "&ioFlags)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def prepareDefaultMaterialForRender(*__, **_) -> Never:
    """
    Qt's 'QSSGDefaultMaterialPreparationResult
    QSSGLayerRenderData::prepareDefaultMaterialForRender(
    QSSGRenderDefaultMaterial &inMaterial, QSSGRenderableObjectFlags
    &inExistingFlags, float inOpacity, bool hasAnyLights, bool
    anyLightHasShadows, QSSGLayerRenderPreparationResultFlags &ioFlags)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareDefaultMaterialForRender' has no cute "
        "function yet. Qt's 'QSSGDefaultMaterialPreparationResult "
        "QSSGLayerRenderData::prepareDefaultMaterialForRender(QSSGRenderDefa"
        "ultMaterial &inMaterial, QSSGRenderableObjectFlags "
        "&inExistingFlags, float inOpacity, bool hasAnyLights, bool "
        "anyLightHasShadows, QSSGLayerRenderPreparationResultFlags "
        "&ioFlags)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def prepareImageForRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::prepareImageForRender(QSSGRenderImage
    &inImage, QSSGRenderableImage::Type inMapType, QSSGRenderableImage
    *&ioFirstImage, QSSGRenderableImage *&ioNextImage,
    QSSGRenderableObjectFlags &ioFlags, QSSGShaderDefaultMaterialKey
    &ioGeneratedShaderKey, quint32 inImageIndex, QSSGRenderDefaultMaterial
    *inMaterial)': takes or gives a type that cannot be passed yet:
    QSSGRenderableImage *&.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareImageForRender' has no cute function "
        "yet. Qt's 'void "
        "QSSGLayerRenderData::prepareImageForRender(QSSGRenderImage "
        "&inImage, QSSGRenderableImage::Type inMapType, QSSGRenderableImage "
        "*&ioFirstImage, QSSGRenderableImage *&ioNextImage, "
        "QSSGRenderableObjectFlags &ioFlags, QSSGShaderDefaultMaterialKey "
        "&ioGeneratedShaderKey, quint32 inImageIndex, "
        "QSSGRenderDefaultMaterial *inMaterial)': takes or gives a type "
        "that cannot be passed yet: QSSGRenderableImage *&.")

  @staticmethod
  def prepareModelBoneTextures(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::prepareModelBoneTextures(const
    QSSGRenderContextInterface &contextInterface, const RenderableNodeEntries
    &renderableModels)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareModelBoneTextures' has no cute "
        "function yet. Qt's 'void "
        "QSSGLayerRenderData::prepareModelBoneTextures(const "
        "QSSGRenderContextInterface &contextInterface, const "
        "RenderableNodeEntries &renderableModels)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def prepareModelsForRender(*__, **_) -> Never:
    """
    - Qt's 'bool
      QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterface
      &ctx, const RenderableNodeEntries &renderableModels,
      QSSGLayerRenderPreparationResultFlags &ioFlags, const
      QSSGRenderCameraList &allCameras, const QSSGRenderCameraDataList
      &allCameraData, TModelContextPtrList &modelContexts,
      QSSGRenderableObjectList &opaqueObjects, QSSGRenderableObjectList
      &transparentObjects, QSSGRenderableObjectList &screenTextureObjects,
      float lodThreshold)': takes a type Python has no way to hand over yet.
    - Qt's 'QSSGPrepResultId
      QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterface
      &contextInterface, QSSGPrepContextId prepId, QSSGRenderablesId
      renderablesId, float lodThreshold)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareModelsForRender' has no cute function "
        "yet. Qt's 'bool "
        "QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterf"
        "ace &ctx, const RenderableNodeEntries &renderableModels, "
        "QSSGLayerRenderPreparationResultFlags &ioFlags, const "
        "QSSGRenderCameraList &allCameras, const QSSGRenderCameraDataList "
        "&allCameraData, TModelContextPtrList &modelContexts, "
        "QSSGRenderableObjectList &opaqueObjects, QSSGRenderableObjectList "
        "&transparentObjects, QSSGRenderableObjectList "
        "&screenTextureObjects, float lodThreshold)': takes a type Python "
        "has no way to hand over yet. Qt's 'QSSGPrepResultId "
        "QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterf"
        "ace &contextInterface, QSSGPrepContextId prepId, QSSGRenderablesId "
        "renderablesId, float lodThreshold)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def prepareParticlesForRender(*__, **_) -> Never:
    """
    Qt's 'bool QSSGLayerRenderData::prepareParticlesForRender(const
    RenderableNodeEntries &renderableParticles, const QSSGRenderCameraData
    &cameraData, QSSGLayerRenderPreparationResultFlags &ioFlags)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareParticlesForRender' has no cute "
        "function yet. Qt's 'bool "
        "QSSGLayerRenderData::prepareParticlesForRender(const "
        "RenderableNodeEntries &renderableParticles, const "
        "QSSGRenderCameraData &cameraData, "
        "QSSGLayerRenderPreparationResultFlags &ioFlags)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def prepareRenderables(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGLayerRenderData::prepareRenderables(QSSGRenderContextInterface &ctx,
    QSSGPrepResultId prepId, QRhiRenderPassDescriptor *renderPassDescriptor,
    const QSSGRhiGraphicsPipelineState &ps, QSSGRenderablesFilters filter)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.prepareRenderables' has no cute function yet. "
        "Qt's 'void "
        "QSSGLayerRenderData::prepareRenderables(QSSGRenderContextInterface "
        "&ctx, QSSGPrepResultId prepId, QRhiRenderPassDescriptor "
        "*renderPassDescriptor, const QSSGRhiGraphicsPipelineState &ps, "
        "QSSGRenderablesFilters filter)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def renderRenderables(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGLayerRenderData::renderRenderables(QSSGRenderContextInterface &ctx,
    QSSGPrepResultId prepId)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.renderRenderables' has no cute function yet. "
        "Qt's 'void "
        "QSSGLayerRenderData::renderRenderables(QSSGRenderContextInterface "
        "&ctx, QSSGPrepResultId prepId)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def requestMotionVectorMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderMotionVectorMapPtr
    &QSSGLayerRenderData::requestMotionVectorMapManager()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.requestMotionVectorMapManager' has no cute "
        "function yet. Qt's 'const QSSGRenderMotionVectorMapPtr "
        "&QSSGLayerRenderData::requestMotionVectorMapManager()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def requestReflectionMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderReflectionMapPtr
    &QSSGLayerRenderData::requestReflectionMapManager()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.requestReflectionMapManager' has no cute "
        "function yet. Qt's 'const QSSGRenderReflectionMapPtr "
        "&QSSGLayerRenderData::requestReflectionMapManager()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def requestShadowMapManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderShadowMapPtr
    &QSSGLayerRenderData::requestShadowMapManager()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.requestShadowMapManager' has no cute function "
        "yet. Qt's 'const QSSGRenderShadowMapPtr "
        "&QSSGLayerRenderData::requestShadowMapManager()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def requestSkyMaterialManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGRenderSkyMaterialManagerPtr
    &QSSGLayerRenderData::requestSkyMaterialManager()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.requestSkyMaterialManager' has no cute "
        "function yet. Qt's 'const QSSGRenderSkyMaterialManagerPtr "
        "&QSSGLayerRenderData::requestSkyMaterialManager()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def requestUserRenderPassManager(*__, **_) -> Never:
    """
    Qt's 'const QSSGUserRenderPassManagerPtr
    &QSSGLayerRenderData::requestUserRenderPassManager()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.requestUserRenderPassManager' has no cute "
        "function yet. Qt's 'const QSSGUserRenderPassManagerPtr "
        "&QSSGLayerRenderData::requestUserRenderPassManager()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def restoreRenderState(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::restoreRenderState(QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.restoreRenderState' has no cute function yet. "
        "Qt's 'void QSSGLayerRenderData::restoreRenderState(QSSGRenderer "
        "&renderer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def saveRenderState(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::saveRenderState(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.saveRenderState' has no cute function yet. "
        "Qt's 'void QSSGLayerRenderData::saveRenderState(const QSSGRenderer "
        "&renderer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setBonemapTexture(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setBonemapTexture(const QSSGModelContext
    &modelContext, QRhiTexture *bonemapTexture)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setBonemapTexture' has no cute function yet. "
        "Qt's 'void QSSGLayerRenderData::setBonemapTexture(const "
        "QSSGModelContext &modelContext, QRhiTexture *bonemapTexture)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setGlobalOpacity(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setGlobalOpacity(QSSGRenderablesId
    renderablesId, const QSSGRenderModel &model, float opacity)': names the
    enum 'QSSGRenderablesId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setGlobalOpacity' has no cute function yet. "
        "Qt's 'void QSSGLayerRenderData::setGlobalOpacity(QSSGRenderablesId "
        "renderablesId, const QSSGRenderModel &model, float opacity)': "
        "names the enum 'QSSGRenderablesId', whose class cannot be named "
        "here.")

  @staticmethod
  def setGlobalTransform(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setGlobalTransform(QSSGRenderablesId
    renderablesId, const QSSGRenderModel &model, const QMatrix4x4 &mvp)':
    names the enum 'QSSGRenderablesId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setGlobalTransform' has no cute function yet. "
        "Qt's 'void "
        "QSSGLayerRenderData::setGlobalTransform(QSSGRenderablesId "
        "renderablesId, const QSSGRenderModel &model, const QMatrix4x4 "
        "&mvp)': names the enum 'QSSGRenderablesId', whose class cannot be "
        "named here.")

  @staticmethod
  def setLightmapTexture(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setLightmapTexture(const QSSGModelContext
    &modelContext, QRhiTexture *lightmapTexture)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setLightmapTexture' has no cute function yet. "
        "Qt's 'void QSSGLayerRenderData::setLightmapTexture(const "
        "QSSGModelContext &modelContext, QRhiTexture *lightmapTexture)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setModelMaterials(*__, **_) -> Never:
    """
    - Qt's 'void QSSGLayerRenderData::setModelMaterials(QSSGRenderablesId
      renderablesId, const QSSGRenderModel &model, const
      QList<QSSGResourceId> &materials)': names the enum 'QSSGRenderablesId',
      whose class cannot be named here.
    - Qt's 'void QSSGLayerRenderData::setModelMaterials(const
      QSSGRenderablesId renderablesId, const QList<QSSGResourceId>
      &materials)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setModelMaterials' has no cute function yet. "
        "Qt's 'void "
        "QSSGLayerRenderData::setModelMaterials(QSSGRenderablesId "
        "renderablesId, const QSSGRenderModel &model, const "
        "QList<QSSGResourceId> &materials)': names the enum "
        "'QSSGRenderablesId', whose class cannot be named here. Qt's 'void "
        "QSSGLayerRenderData::setModelMaterials(const QSSGRenderablesId "
        "renderablesId, const QList<QSSGResourceId> &materials)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setTonemapFeatures(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setTonemapFeatures(QSSGShaderFeatures
    &features, QSSGRenderLayer::TonemapMode tonemapMode)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setTonemapFeatures' has no cute function yet. "
        "Qt's 'void "
        "QSSGLayerRenderData::setTonemapFeatures(QSSGShaderFeatures "
        "&features, QSSGRenderLayer::TonemapMode tonemapMode)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setVertexInputPresence(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::setVertexInputPresence(const
    QSSGRenderableObjectFlags &renderableFlags, QSSGShaderDefaultMaterialKey
    &key)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.setVertexInputPresence' has no cute function "
        "yet. Qt's 'void QSSGLayerRenderData::setVertexInputPresence(const "
        "QSSGRenderableObjectFlags &renderableFlags, "
        "QSSGShaderDefaultMaterialKey &key)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def updateSortedDepthObjectsListImp(*__, **_) -> Never:
    """
    Qt's 'void QSSGLayerRenderData::updateSortedDepthObjectsListImp(const
    QSSGRenderCamera &camera, size_t index)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLayerRenderData.updateSortedDepthObjectsListImp' has no cute "
        "function yet. Qt's 'void "
        "QSSGLayerRenderData::updateSortedDepthObjectsListImp(const "
        "QSSGRenderCamera &camera, size_t index)': takes a type Python has "
        "no way to hand over yet.")
