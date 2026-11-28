"""
QSSGCustomMaterialSystem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGCustomMaterialSystem to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSSGRenderContextInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderContextInterface = WAIT['QSSGRenderContextInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGCustomMaterialSystem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGCustomMaterialSystem: a plain Python object
  standing in front of one C++ QSSGCustomMaterialSystem.

  What exists
  -----------

  Every function of Qt's QSSGCustomMaterialSystem that has a ritual and that
  Python can call so far, 2 names in all: 'setRenderContextInterface',
  'releaseCachedResources'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGCustomMaterialSystem::setShaderResources(char *ubufData,
    const QSSGRenderCustomMaterial &inMaterial, const QByteArray
    &inPropertyName, const QVariant &propertyValue,
    QSSGRenderShaderValue::Type inPropertyType, QSSGRhiShaderPipeline
    &shaderPipeline)': names 'char', which has no cute class yet.
  - Qt's 'QSSGCustomMaterialSystem::~QSSGCustomMaterialSystem()': the
    destructor: Python never removes a C++ QSSGCustomMaterialSystem.
  - Qt's 'bool QSSGCustomMaterialSystem::prepareForRender(const
    QSSGRenderModel &inModel, const QSSGRenderSubset &inSubset,
    QSSGRenderCustomMaterial &inMaterial)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGCustomMaterialSystem::shadersForCustomMaterial(
    QSSGRhiGraphicsPipelineState *ps, const QSSGRenderCustomMaterial
    &material, QSSGSubsetRenderable &renderable, const
    QSSGShaderDefaultMaterialKeyProperties
    &defaultMaterialShaderKeyProperties, const QSSGShaderFeatures
    &featureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGCustomMaterialSystem::updateUniformsForCustomMaterial(
    QSSGRhiShaderPipeline &shaderPipeline, QSSGRhiContext *rhiCtx, const
    QSSGLayerRenderData &inData, char *ubufData, QSSGRhiGraphicsPipelineState
    *ps, const QSSGRenderCustomMaterial &material, QSSGSubsetRenderable
    &renderable, const QSSGRenderCameraList &cameras, const QVector2D
    *depthAdjust, const QMatrix4x4 *alteredModelViewProjection)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSSGCustomMaterialSystem::rhiPrepareRenderable(
    QSSGRhiGraphicsPipelineState *ps, QSSGPassKey passKey,
    QSSGSubsetRenderable &renderable, const QSSGShaderFeatures &featureSet,
    const QSSGRenderCustomMaterial &material, const QSSGLayerRenderData
    &layerData, QRhiRenderPassDescriptor *renderPassDescriptor, int samples,
    int viewCount, bool screenMapPass, QSSGRenderCamera *camera,
    QSSGRenderTextureCubeFace cubeFace, QMatrix4x4 *modelViewProjection,
    QSSGReflectionMapEntry *entry, bool oit)': names 'void', which has no
    cute class yet.
  - Qt's 'void QSSGCustomMaterialSystem::applyRhiShaderPropertyValues(char
    *ubufData, const QSSGRenderCustomMaterial &inMaterial,
    QSSGRhiShaderPipeline &shaderPipeline)': names 'char', which has no cute
    class yet.
  - Qt's 'void QSSGCustomMaterialSystem::rhiRenderRenderable(QSSGRhiContext
    *rhiCtx, QSSGSubsetRenderable &renderable, bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace, const QSSGRhiGraphicsPipelineState
    &state, qsizetype userPassIndex)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGCustomMaterialSystem is created at the first use, not by
    'QSSGCustomMaterialSystem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGCustomMaterialSystem.
  - Each name of Qt's QSSGCustomMaterialSystem that has no cute function yet,
    'applyRhiShaderPropertyValues', 'prepareForRender',
    'rhiPrepareRenderable', 'rhiRenderRenderable', 'setShaderResources',
    'shadersForCustomMaterial', 'updateUniformsForCustomMaterial', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGCustomMaterialSystem'

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

  @overload(QSSGRenderContextInterface)
  @overload(NoneType)
  def setRenderContextInterface(
      self,
      inContext: Optional[QSSGRenderContextInterface],
  ) -> None:
    """
    Calls Qt's 'void QSSGCustomMaterialSystem::setRenderContextInterface(
    QSSGRenderContextInterface *inContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgcustommaterialsystem.html

    Parameters
    ----------

    inContext : Optional[QSSGRenderContextInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGCustomMaterialSystem::setRenderContextInterface(
    #      QSSGRenderContextInterface *inContext)
    self.uglySide.call(
        'ritual_ZN24QSSGCustomMaterialSystem25setRenderContextInterfaceEP26'
        'QSSGRenderContextInterface',
        self._addressOf(inContext),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGCustomMaterialSystem::QSSGCustomMaterialSystem()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgcustommaterialsystem.html
    """
    #  QSSGCustomMaterialSystem::QSSGCustomMaterialSystem()
    self._noteCreation(QSSGCustomMaterialSystem, lambda: Rituals.call(
        'ritual_ZN24QSSGCustomMaterialSystemC1Ev',
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

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGCustomMaterialSystem::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgcustommaterialsystem.html
    """
    #  void QSSGCustomMaterialSystem::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN24QSSGCustomMaterialSystem22releaseCachedResourcesEv',
    )

  @staticmethod
  def applyRhiShaderPropertyValues(*__, **_) -> Never:
    """
    Qt's 'void QSSGCustomMaterialSystem::applyRhiShaderPropertyValues(char
    *ubufData, const QSSGRenderCustomMaterial &inMaterial,
    QSSGRhiShaderPipeline &shaderPipeline)': names 'char', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.applyRhiShaderPropertyValues' has no "
        "cute function yet. Qt's 'void "
        "QSSGCustomMaterialSystem::applyRhiShaderPropertyValues(char "
        "*ubufData, const QSSGRenderCustomMaterial &inMaterial, "
        "QSSGRhiShaderPipeline &shaderPipeline)': names 'char', which has "
        "no cute class yet.")

  @staticmethod
  def prepareForRender(*__, **_) -> Never:
    """
    Qt's 'bool QSSGCustomMaterialSystem::prepareForRender(const
    QSSGRenderModel &inModel, const QSSGRenderSubset &inSubset,
    QSSGRenderCustomMaterial &inMaterial)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.prepareForRender' has no cute function "
        "yet. Qt's 'bool QSSGCustomMaterialSystem::prepareForRender(const "
        "QSSGRenderModel &inModel, const QSSGRenderSubset &inSubset, "
        "QSSGRenderCustomMaterial &inMaterial)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def rhiPrepareRenderable(*__, **_) -> Never:
    """
    Qt's 'void QSSGCustomMaterialSystem::rhiPrepareRenderable(
    QSSGRhiGraphicsPipelineState *ps, QSSGPassKey passKey,
    QSSGSubsetRenderable &renderable, const QSSGShaderFeatures &featureSet,
    const QSSGRenderCustomMaterial &material, const QSSGLayerRenderData
    &layerData, QRhiRenderPassDescriptor *renderPassDescriptor, int samples,
    int viewCount, bool screenMapPass, QSSGRenderCamera *camera,
    QSSGRenderTextureCubeFace cubeFace, QMatrix4x4 *modelViewProjection,
    QSSGReflectionMapEntry *entry, bool oit)': names 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.rhiPrepareRenderable' has no cute "
        "function yet. Qt's 'void "
        "QSSGCustomMaterialSystem::rhiPrepareRenderable(QSSGRhiGraphicsPipel"
        "ineState *ps, QSSGPassKey passKey, QSSGSubsetRenderable "
        "&renderable, const QSSGShaderFeatures &featureSet, const "
        "QSSGRenderCustomMaterial &material, const QSSGLayerRenderData "
        "&layerData, QRhiRenderPassDescriptor *renderPassDescriptor, int "
        "samples, int viewCount, bool screenMapPass, QSSGRenderCamera "
        "*camera, QSSGRenderTextureCubeFace cubeFace, QMatrix4x4 "
        "*modelViewProjection, QSSGReflectionMapEntry *entry, bool oit)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def rhiRenderRenderable(*__, **_) -> Never:
    """
    Qt's 'void QSSGCustomMaterialSystem::rhiRenderRenderable(QSSGRhiContext
    *rhiCtx, QSSGSubsetRenderable &renderable, bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace, const QSSGRhiGraphicsPipelineState
    &state, qsizetype userPassIndex)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.rhiRenderRenderable' has no cute "
        "function yet. Qt's 'void "
        "QSSGCustomMaterialSystem::rhiRenderRenderable(QSSGRhiContext "
        "*rhiCtx, QSSGSubsetRenderable &renderable, bool *needsSetViewport, "
        "QSSGRenderTextureCubeFace cubeFace, const "
        "QSSGRhiGraphicsPipelineState &state, qsizetype userPassIndex)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setShaderResources(*__, **_) -> Never:
    """
    Qt's 'void QSSGCustomMaterialSystem::setShaderResources(char *ubufData,
    const QSSGRenderCustomMaterial &inMaterial, const QByteArray
    &inPropertyName, const QVariant &propertyValue,
    QSSGRenderShaderValue::Type inPropertyType, QSSGRhiShaderPipeline
    &shaderPipeline)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.setShaderResources' has no cute function "
        "yet. Qt's 'void QSSGCustomMaterialSystem::setShaderResources(char "
        "*ubufData, const QSSGRenderCustomMaterial &inMaterial, const "
        "QByteArray &inPropertyName, const QVariant &propertyValue, "
        "QSSGRenderShaderValue::Type inPropertyType, QSSGRhiShaderPipeline "
        "&shaderPipeline)': names 'char', which has no cute class yet.")

  @staticmethod
  def shadersForCustomMaterial(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGCustomMaterialSystem::shadersForCustomMaterial(
    QSSGRhiGraphicsPipelineState *ps, const QSSGRenderCustomMaterial
    &material, QSSGSubsetRenderable &renderable, const
    QSSGShaderDefaultMaterialKeyProperties
    &defaultMaterialShaderKeyProperties, const QSSGShaderFeatures
    &featureSet, const QSSGUserShaderAugmentation &shaderAugmentation)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.shadersForCustomMaterial' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGCustomMaterialSystem::shadersForCustomMaterial(QSSGRhiGraphicsP"
        "ipelineState *ps, const QSSGRenderCustomMaterial &material, "
        "QSSGSubsetRenderable &renderable, const "
        "QSSGShaderDefaultMaterialKeyProperties "
        "&defaultMaterialShaderKeyProperties, const QSSGShaderFeatures "
        "&featureSet, const QSSGUserShaderAugmentation "
        "&shaderAugmentation)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateUniformsForCustomMaterial(*__, **_) -> Never:
    """
    Qt's 'void QSSGCustomMaterialSystem::updateUniformsForCustomMaterial(
    QSSGRhiShaderPipeline &shaderPipeline, QSSGRhiContext *rhiCtx, const
    QSSGLayerRenderData &inData, char *ubufData, QSSGRhiGraphicsPipelineState
    *ps, const QSSGRenderCustomMaterial &material, QSSGSubsetRenderable
    &renderable, const QSSGRenderCameraList &cameras, const QVector2D
    *depthAdjust, const QMatrix4x4 *alteredModelViewProjection)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGCustomMaterialSystem.updateUniformsForCustomMaterial' has no "
        "cute function yet. Qt's 'void "
        "QSSGCustomMaterialSystem::updateUniformsForCustomMaterial(QSSGRhiSh"
        "aderPipeline &shaderPipeline, QSSGRhiContext *rhiCtx, const "
        "QSSGLayerRenderData &inData, char *ubufData, "
        "QSSGRhiGraphicsPipelineState *ps, const QSSGRenderCustomMaterial "
        "&material, QSSGSubsetRenderable &renderable, const "
        "QSSGRenderCameraList &cameras, const QVector2D *depthAdjust, const "
        "QMatrix4x4 *alteredModelViewProjection)': takes a type Python has "
        "no way to hand over yet.")
