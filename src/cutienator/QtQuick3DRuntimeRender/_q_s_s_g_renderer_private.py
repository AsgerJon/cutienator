"""
QSSGRendererPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRendererPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRendererPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRendererPrivate: a plain Python object standing
  in front of one C++ QSSGRendererPrivate.

  C++ hands a QSSGRendererPrivate around as a copy, so every C++
  QSSGRendererPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGRendererPrivate yet. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::generateRhiShaderPipelineImpl(QSSGSubsetRenderable
    &renderable, QSSGShaderLibraryManager &shaderLibraryManager,
    QSSGShaderCache &shaderCache, QSSGProgramGenerator
    &shaderProgramGenerator, const QSSGShaderDefaultMaterialKeyProperties
    &shaderKeyProperties, const QSSGShaderFeatures &featureSet, const
    QSSGUserShaderAugmentation &shaderAugmentation, QByteArray
    &shaderString)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::generateRhiShaderPipeline(QSSGRenderer &renderer,
    QSSGSubsetRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::getShaderPipelineForDefaultMaterial(QSSGRenderer
    &renderer, QSSGSubsetRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRendererPrivate::getLayerHitObjectList(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &ray, bool inPickEverything, PickResultList
    &outIntersectionResult)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGRendererPrivate::intersectRayWithSubsetRenderable(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &inRay, const QSSGRenderNode &node, PickResultList
    &outIntersectionResultList)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGRendererPrivate::intersectRayWithItem2D(const
    QSSGRenderLayer &layer, const QSSGRenderRay &inRay, const
    QSSGRenderItem2D &item2D, PickResultList &outIntersectionResultList)':
    takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QSSGRenderPickResult>
    QSSGRendererPrivate::closestPointOnSubsetRenderable(const QSSGRenderLayer
    &layer, QSSGBufferManager &bufferManager, const QVector3D &center, float
    radiusSquared, const QSSGRenderNode &node)': takes a type Python has no
    way to hand over yet.
  - Qt's 'PickResultList QSSGRendererPrivate::syncPickAll(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QSSGRenderRay &ray)': takes a type Python has no way to hand over yet.
  - Qt's 'PickResultList QSSGRendererPrivate::syncPick(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QSSGRenderRay &ray, QSSGRenderNode *target)': takes a type Python has no
    way to hand over yet.
  - Qt's 'PickResultList QSSGRendererPrivate::syncPickSubset(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': takes a
    type Python has no way to hand over yet.
  - Qt's 'std::optional<QSSGRenderPickResult>
    QSSGRendererPrivate::syncPickClosestPoint(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QVector3D &center, const float radiusSquared, QSSGRenderNode *target)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<const QSSGRenderNode *>
    QSSGRendererPrivate::syncPickInFrustum(const QSSGRenderContextInterface
    &ctx, const QSSGRenderLayer &layer, const QSSGFrustum &frustum)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QSSGRendererPrivate::isGlobalPickingEnabled(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRendererPrivate::setGlobalPickingEnabled(QSSGRenderer
    &renderer, bool isEnabled)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGRendererPrivate::setRenderContextInterface(QSSGRenderer
    &renderer, QSSGRenderContextInterface *ctx)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSSGRendererPrivate::setSgRenderContext(QSSGRenderer
    &renderer, QSGRenderContext *sgRenderCtx)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGLayerRenderData
    *QSSGRendererPrivate::getCurrentRenderData(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
  - Qt's 'QSGRenderContext *QSSGRendererPrivate::getSgRenderContext(const
    QSSGRenderer &renderer)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSSGRendererPrivate::~QSSGRendererPrivate()': the destructor:
    Python removes its C++ QSSGRendererPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRendererPrivate is created at the first use, not by
    'QSSGRendererPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRendererPrivate back gives a copy the ritual made
    for Python, in a new cute QSSGRendererPrivate.
  - Each name of Qt's QSSGRendererPrivate that has no cute function yet,
    'closestPointOnSubsetRenderable', 'generateRhiShaderPipeline',
    'generateRhiShaderPipelineImpl', 'getCurrentRenderData',
    'getLayerHitObjectList', 'getSgRenderContext',
    'getShaderPipelineForDefaultMaterial', 'intersectRayWithItem2D',
    'intersectRayWithSubsetRenderable', 'isGlobalPickingEnabled',
    'setGlobalPickingEnabled', 'setRenderContextInterface',
    'setSgRenderContext', 'syncPick', 'syncPickAll', 'syncPickClosestPoint',
    'syncPickInFrustum', 'syncPickSubset', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRendererPrivate'

  #  Qt's '~QSSGRendererPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRendererPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRendererPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRendererPrivate::QSSGRendererPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendererprivate.html#QSSGRendererPrivate
    """
    #  QSSGRendererPrivate::QSSGRendererPrivate()
    self._noteCreation(QSSGRendererPrivate, lambda: Rituals.call(
        'ritual_ZN19QSSGRendererPrivateC1Ev',
    ))

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

  @staticmethod
  def closestPointOnSubsetRenderable(*__, **_) -> Never:
    """
    Qt's 'std::optional<QSSGRenderPickResult>
    QSSGRendererPrivate::closestPointOnSubsetRenderable(const QSSGRenderLayer
    &layer, QSSGBufferManager &bufferManager, const QVector3D &center, float
    radiusSquared, const QSSGRenderNode &node)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.closestPointOnSubsetRenderable' has no cute "
        "function yet. Qt's 'std::optional<QSSGRenderPickResult> "
        "QSSGRendererPrivate::closestPointOnSubsetRenderable(const "
        "QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const "
        "QVector3D &center, float radiusSquared, const QSSGRenderNode "
        "&node)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def generateRhiShaderPipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::generateRhiShaderPipeline(QSSGRenderer &renderer,
    QSSGSubsetRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.generateRhiShaderPipeline' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRendererPrivate::generateRhiShaderPipeline(QSSGRenderer "
        "&renderer, QSSGSubsetRenderable &inRenderable, const "
        "QSSGShaderFeatures &inFeatureSet, const QSSGUserShaderAugmentation "
        "&shaderAugmentation)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def generateRhiShaderPipelineImpl(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::generateRhiShaderPipelineImpl(QSSGSubsetRenderable
    &renderable, QSSGShaderLibraryManager &shaderLibraryManager,
    QSSGShaderCache &shaderCache, QSSGProgramGenerator
    &shaderProgramGenerator, const QSSGShaderDefaultMaterialKeyProperties
    &shaderKeyProperties, const QSSGShaderFeatures &featureSet, const
    QSSGUserShaderAugmentation &shaderAugmentation, QByteArray
    &shaderString)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.generateRhiShaderPipelineImpl' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRendererPrivate::generateRhiShaderPipelineImpl(QSSGSubsetRender"
        "able &renderable, QSSGShaderLibraryManager &shaderLibraryManager, "
        "QSSGShaderCache &shaderCache, QSSGProgramGenerator "
        "&shaderProgramGenerator, const "
        "QSSGShaderDefaultMaterialKeyProperties &shaderKeyProperties, const "
        "QSSGShaderFeatures &featureSet, const QSSGUserShaderAugmentation "
        "&shaderAugmentation, QByteArray &shaderString)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getCurrentRenderData(*__, **_) -> Never:
    """
    Qt's 'QSSGLayerRenderData
    *QSSGRendererPrivate::getCurrentRenderData(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.getCurrentRenderData' has no cute function "
        "yet. Qt's 'QSSGLayerRenderData "
        "*QSSGRendererPrivate::getCurrentRenderData(const QSSGRenderer "
        "&renderer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getLayerHitObjectList(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::getLayerHitObjectList(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &ray, bool inPickEverything, PickResultList
    &outIntersectionResult)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.getLayerHitObjectList' has no cute function "
        "yet. Qt's 'void QSSGRendererPrivate::getLayerHitObjectList(const "
        "QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const "
        "QSSGRenderRay &ray, bool inPickEverything, PickResultList "
        "&outIntersectionResult)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def getSgRenderContext(*__, **_) -> Never:
    """
    Qt's 'QSGRenderContext *QSSGRendererPrivate::getSgRenderContext(const
    QSSGRenderer &renderer)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.getSgRenderContext' has no cute function yet. "
        "Qt's 'QSGRenderContext "
        "*QSSGRendererPrivate::getSgRenderContext(const QSSGRenderer "
        "&renderer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getShaderPipelineForDefaultMaterial(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRendererPrivate::getShaderPipelineForDefaultMaterial(QSSGRenderer
    &renderer, QSSGSubsetRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.getShaderPipelineForDefaultMaterial' has no "
        "cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRendererPrivate::getShaderPipelineForDefaultMaterial(QSSGRender"
        "er &renderer, QSSGSubsetRenderable &inRenderable, const "
        "QSSGShaderFeatures &inFeatureSet, const QSSGUserShaderAugmentation "
        "&shaderAugmentation)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def intersectRayWithItem2D(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::intersectRayWithItem2D(const
    QSSGRenderLayer &layer, const QSSGRenderRay &inRay, const
    QSSGRenderItem2D &item2D, PickResultList &outIntersectionResultList)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.intersectRayWithItem2D' has no cute function "
        "yet. Qt's 'void QSSGRendererPrivate::intersectRayWithItem2D(const "
        "QSSGRenderLayer &layer, const QSSGRenderRay &inRay, const "
        "QSSGRenderItem2D &item2D, PickResultList "
        "&outIntersectionResultList)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def intersectRayWithSubsetRenderable(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::intersectRayWithSubsetRenderable(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &inRay, const QSSGRenderNode &node, PickResultList
    &outIntersectionResultList)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.intersectRayWithSubsetRenderable' has no cute "
        "function yet. Qt's 'void "
        "QSSGRendererPrivate::intersectRayWithSubsetRenderable(const "
        "QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const "
        "QSSGRenderRay &inRay, const QSSGRenderNode &node, PickResultList "
        "&outIntersectionResultList)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def isGlobalPickingEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRendererPrivate::isGlobalPickingEnabled(const QSSGRenderer
    &renderer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.isGlobalPickingEnabled' has no cute function "
        "yet. Qt's 'bool QSSGRendererPrivate::isGlobalPickingEnabled(const "
        "QSSGRenderer &renderer)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setGlobalPickingEnabled(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::setGlobalPickingEnabled(QSSGRenderer
    &renderer, bool isEnabled)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.setGlobalPickingEnabled' has no cute function "
        "yet. Qt's 'void "
        "QSSGRendererPrivate::setGlobalPickingEnabled(QSSGRenderer "
        "&renderer, bool isEnabled)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRenderContextInterface(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::setRenderContextInterface(QSSGRenderer
    &renderer, QSSGRenderContextInterface *ctx)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.setRenderContextInterface' has no cute "
        "function yet. Qt's 'void "
        "QSSGRendererPrivate::setRenderContextInterface(QSSGRenderer "
        "&renderer, QSSGRenderContextInterface *ctx)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setSgRenderContext(*__, **_) -> Never:
    """
    Qt's 'void QSSGRendererPrivate::setSgRenderContext(QSSGRenderer
    &renderer, QSGRenderContext *sgRenderCtx)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.setSgRenderContext' has no cute function yet. "
        "Qt's 'void QSSGRendererPrivate::setSgRenderContext(QSSGRenderer "
        "&renderer, QSGRenderContext *sgRenderCtx)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def syncPick(*__, **_) -> Never:
    """
    Qt's 'PickResultList QSSGRendererPrivate::syncPick(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QSSGRenderRay &ray, QSSGRenderNode *target)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.syncPick' has no cute function yet. Qt's "
        "'PickResultList QSSGRendererPrivate::syncPick(const "
        "QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, "
        "const QSSGRenderRay &ray, QSSGRenderNode *target)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def syncPickAll(*__, **_) -> Never:
    """
    Qt's 'PickResultList QSSGRendererPrivate::syncPickAll(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QSSGRenderRay &ray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.syncPickAll' has no cute function yet. Qt's "
        "'PickResultList QSSGRendererPrivate::syncPickAll(const "
        "QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, "
        "const QSSGRenderRay &ray)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def syncPickClosestPoint(*__, **_) -> Never:
    """
    Qt's 'std::optional<QSSGRenderPickResult>
    QSSGRendererPrivate::syncPickClosestPoint(const
    QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
    QVector3D &center, const float radiusSquared, QSSGRenderNode *target)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.syncPickClosestPoint' has no cute function "
        "yet. Qt's 'std::optional<QSSGRenderPickResult> "
        "QSSGRendererPrivate::syncPickClosestPoint(const "
        "QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, "
        "const QVector3D &center, const float radiusSquared, QSSGRenderNode "
        "*target)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def syncPickInFrustum(*__, **_) -> Never:
    """
    Qt's 'QList<const QSSGRenderNode *>
    QSSGRendererPrivate::syncPickInFrustum(const QSSGRenderContextInterface
    &ctx, const QSSGRenderLayer &layer, const QSSGFrustum &frustum)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.syncPickInFrustum' has no cute function yet. "
        "Qt's 'QList<const QSSGRenderNode *> "
        "QSSGRendererPrivate::syncPickInFrustum(const "
        "QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, "
        "const QSSGFrustum &frustum)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def syncPickSubset(*__, **_) -> Never:
    """
    Qt's 'PickResultList QSSGRendererPrivate::syncPickSubset(const
    QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
    QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRendererPrivate.syncPickSubset' has no cute function yet. "
        "Qt's 'PickResultList QSSGRendererPrivate::syncPickSubset(const "
        "QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const "
        "QSSGRenderRay &ray, QVarLengthArray<QSSGRenderNode *> subset)': "
        "takes a type Python has no way to hand over yet.")
