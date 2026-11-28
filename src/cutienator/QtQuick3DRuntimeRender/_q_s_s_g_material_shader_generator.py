"""
QSSGMaterialShaderGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGMaterialShaderGenerator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSSGRenderableImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QSSGMaterialShaderGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMaterialShaderGenerator: a plain Python object
  standing in front of one C++ QSSGMaterialShaderGenerator.

  What exists
  -----------

  Every function of Qt's QSSGMaterialShaderGenerator that has a ritual and
  that Python can call so far, 11 names in all: 'getSamplerName',
  'directionalLightProcessorArgumentList', 'pointLightProcessorArgumentList',
  'spotLightProcessorArgumentList', 'ambientLightProcessorArgumentList',
  'specularLightProcessorArgumentList', 'shadedFragmentMainArgumentList',
  'postProcessorArgumentList', 'iblProbeProcessorArgumentList',
  'vertexMainArgumentList', 'vertexInstancedMainArgumentList'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMaterialShaderGenerator::~QSSGMaterialShaderGenerator()': the
    destructor: Python never removes a C++ QSSGMaterialShaderGenerator.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGMaterialShaderGenerator::generateMaterialRhiShader(const QByteArray
    &inShaderKeyPrefix, QSSGMaterialVertexPipeline &vertexGenerator, const
    QSSGShaderDefaultMaterialKey &key, const
    QSSGShaderDefaultMaterialKeyProperties &inProperties, const
    QSSGShaderFeatures &inFeatureSet, const QSSGRenderGraphObject
    &inMaterial, QSSGShaderLibraryManager &shaderLibraryManager,
    QSSGShaderCache &theCache, const QSSGUserShaderAugmentation
    &shaderAugmentation)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGMaterialShaderGenerator::setRhiMaterialProperties(const
    QSSGRenderContextInterface &a0, QSSGRhiShaderPipeline &shaders, char
    *ubufData, QSSGRhiGraphicsPipelineState *inPipelineState, const
    QSSGRenderGraphObject &inMaterial, const QSSGShaderDefaultMaterialKey
    &inKey, const QSSGShaderDefaultMaterialKeyProperties &inProperties, const
    QSSGRenderCameraList &inCameras, const QSSGRenderMvpArray
    &inModelViewProjections, const QMatrix3x3 &inNormalMatrix, const
    QMatrix4x4 &inGlobalTransform, const QMatrix4x4 &clipSpaceCorrMatrix,
    const QMatrix4x4 &localInstanceTransform, const QMatrix4x4
    &globalInstanceTransform, const QSSGDataView<float> &inMorphWeights,
    QSSGRenderableImage *inFirstImage, float inOpacity, const
    QSSGLayerRenderData &inRenderProperties, const QSSGShaderLightListView
    &inLights, const QSSGShaderReflectionProbe &reflectionProbe, bool
    receivesShadows, bool receivesReflections, const QVector2D
    *shadowDepthAdjust, QRhiTexture *lightmapTexture)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 forbidden.

  What to expect
  --------------

  - The C++ QSSGMaterialShaderGenerator is created at the first use, not by
    'QSSGMaterialShaderGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGMaterialShaderGenerator.
  - Each name of Qt's QSSGMaterialShaderGenerator that has no cute function
    yet, 'generateMaterialRhiShader', 'setRhiMaterialProperties', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRenderableImage.Type)
  def getSamplerName(type: QSSGRenderableImage.Type) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::getSamplerName(QSSGRenderableImage::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html#getSamplerName

    Parameters
    ----------

    type : QSSGRenderableImage.Type
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMaterialShaderGenerator::getSamplerName(
    #      QSSGRenderableImage::Type type)
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator14getSamplerNameEN19QSSGRend'
        'erableImage4TypeE',
        type.value,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def directionalLightProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMaterialShaderGenerator::
    #      directionalLightProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator37directionalLightProcessorA'
        'rgumentListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def pointLightProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::pointLightProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::pointLightProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator31pointLightProcessorArgumen'
        'tListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def spotLightProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::spotLightProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::spotLightProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator30spotLightProcessorArgument'
        'ListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def ambientLightProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator33ambientLightProcessorArgum'
        'entListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def specularLightProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::specularLightProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::specularLightProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator34specularLightProcessorArgu'
        'mentListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def shadedFragmentMainArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator30shadedFragmentMainArgument'
        'ListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def postProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::postProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMaterialShaderGenerator::postProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator25postProcessorArgumentListE'
        'v',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def iblProbeProcessorArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator29iblProbeProcessorArgumentL'
        'istEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def vertexMainArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::vertexMainArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGMaterialShaderGenerator::vertexMainArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator22vertexMainArgumentListEv',
    )
    return None if chars is None else chars.decode()

  @staticmethod
  def vertexInstancedMainArgumentList() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmaterialshadergenerator.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList()
    chars = Rituals.call(
        'ritual_ZN27QSSGMaterialShaderGenerator31vertexInstancedMainArgumen'
        'tListEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMaterialShaderGenerator'

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
  def generateMaterialRhiShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGMaterialShaderGenerator::generateMaterialRhiShader(const QByteArray
    &inShaderKeyPrefix, QSSGMaterialVertexPipeline &vertexGenerator, const
    QSSGShaderDefaultMaterialKey &key, const
    QSSGShaderDefaultMaterialKeyProperties &inProperties, const
    QSSGShaderFeatures &inFeatureSet, const QSSGRenderGraphObject
    &inMaterial, QSSGShaderLibraryManager &shaderLibraryManager,
    QSSGShaderCache &theCache, const QSSGUserShaderAugmentation
    &shaderAugmentation)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialShaderGenerator.generateMaterialRhiShader' has no "
        "cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGMaterialShaderGenerator::generateMaterialRhiShader(const "
        "QByteArray &inShaderKeyPrefix, QSSGMaterialVertexPipeline "
        "&vertexGenerator, const QSSGShaderDefaultMaterialKey &key, const "
        "QSSGShaderDefaultMaterialKeyProperties &inProperties, const "
        "QSSGShaderFeatures &inFeatureSet, const QSSGRenderGraphObject "
        "&inMaterial, QSSGShaderLibraryManager &shaderLibraryManager, "
        "QSSGShaderCache &theCache, const QSSGUserShaderAugmentation "
        "&shaderAugmentation)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setRhiMaterialProperties(*__, **_) -> Never:
    """
    Qt's 'void QSSGMaterialShaderGenerator::setRhiMaterialProperties(const
    QSSGRenderContextInterface &a0, QSSGRhiShaderPipeline &shaders, char
    *ubufData, QSSGRhiGraphicsPipelineState *inPipelineState, const
    QSSGRenderGraphObject &inMaterial, const QSSGShaderDefaultMaterialKey
    &inKey, const QSSGShaderDefaultMaterialKeyProperties &inProperties, const
    QSSGRenderCameraList &inCameras, const QSSGRenderMvpArray
    &inModelViewProjections, const QMatrix3x3 &inNormalMatrix, const
    QMatrix4x4 &inGlobalTransform, const QMatrix4x4 &clipSpaceCorrMatrix,
    const QMatrix4x4 &localInstanceTransform, const QMatrix4x4
    &globalInstanceTransform, const QSSGDataView<float> &inMorphWeights,
    QSSGRenderableImage *inFirstImage, float inOpacity, const
    QSSGLayerRenderData &inRenderProperties, const QSSGShaderLightListView
    &inLights, const QSSGShaderReflectionProbe &reflectionProbe, bool
    receivesShadows, bool receivesReflections, const QVector2D
    *shadowDepthAdjust, QRhiTexture *lightmapTexture)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMaterialShaderGenerator.setRhiMaterialProperties' has no cute "
        "function yet. Qt's 'void "
        "QSSGMaterialShaderGenerator::setRhiMaterialProperties(const "
        "QSSGRenderContextInterface &a0, QSSGRhiShaderPipeline &shaders, "
        "char *ubufData, QSSGRhiGraphicsPipelineState *inPipelineState, "
        "const QSSGRenderGraphObject &inMaterial, const "
        "QSSGShaderDefaultMaterialKey &inKey, const "
        "QSSGShaderDefaultMaterialKeyProperties &inProperties, const "
        "QSSGRenderCameraList &inCameras, const QSSGRenderMvpArray "
        "&inModelViewProjections, const QMatrix3x3 &inNormalMatrix, const "
        "QMatrix4x4 &inGlobalTransform, const QMatrix4x4 "
        "&clipSpaceCorrMatrix, const QMatrix4x4 &localInstanceTransform, "
        "const QMatrix4x4 &globalInstanceTransform, const "
        "QSSGDataView<float> &inMorphWeights, QSSGRenderableImage "
        "*inFirstImage, float inOpacity, const QSSGLayerRenderData "
        "&inRenderProperties, const QSSGShaderLightListView &inLights, "
        "const QSSGShaderReflectionProbe &reflectionProbe, bool "
        "receivesShadows, bool receivesReflections, const QVector2D "
        "*shadowDepthAdjust, QRhiTexture *lightmapTexture)': takes a type "
        "Python has no way to hand over yet.")
