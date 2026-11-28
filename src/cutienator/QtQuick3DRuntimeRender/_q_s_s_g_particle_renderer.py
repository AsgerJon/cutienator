"""
QSSGParticleRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGParticleRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QSSGShaderFeatures
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGShaderFeatures = WAIT['QSSGShaderFeatures']


class QSSGParticleRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGParticleRenderer: a plain Python object standing
  in front of one C++ QSSGParticleRenderer.

  C++ hands a QSSGParticleRenderer around as a copy, so every C++
  QSSGParticleRenderer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGParticleRenderer that has a ritual and that
  Python can call so far, 2 names in all: 'particleShaderFeatures',
  'setShaderCacheEnabled'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGParticleRenderer::updateUniformsForParticles(const
    QSSGLayerRenderData &inData, QSSGRhiShaderPipeline &shaderPipeline,
    QSSGRhiContext *rhiCtx, char *ubufData, QSSGParticlesRenderable
    &renderable, const QSSGRenderCameraList &cameras)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QSSGParticleRenderer::updateUniformsForParticleModel(
    QSSGRhiShaderPipeline &shaderPipeline, char *ubufData, const
    QSSGRenderModel *model, quint32 offset)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGParticleRenderer::getShaderPipelineParticles(QSSGRenderer &renderer,
    QSSGParticlesRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGParticleRenderer::generateRhiShaderPipeline(QSSGRenderer &renderer,
    QSSGParticlesRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, QByteArray &shaderString, const
    QSSGShaderParticleMaterialKeyProperties &shaderKeyProperties)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void
    QSSGParticleRenderer::rhiPrepareRenderable(QSSGRhiShaderPipeline
    &shaderPipeline, QSSGPassKey passKey, QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps, QSSGParticlesRenderable &renderable,
    const QSSGLayerRenderData &inData, QRhiRenderPassDescriptor
    *renderPassDescriptor, int samples, int viewCount, QSSGRenderCamera
    *alteredCamera, QSSGRenderTextureCubeFace cubeFace,
    QSSGReflectionMapEntry *entry, bool oit)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QSSGParticleRenderer::rhiRenderRenderable(QSSGRhiContext
    *rhiCtx, QSSGParticlesRenderable &renderable, bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace, const QSSGRhiGraphicsPipelineState
    &state)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGParticleRenderer::prepareParticlesForModel(QSSGRhiShaderPipeline
    &shaderPipeline, QSSGRhiContext *rhiCtx, QSSGRhiShaderResourceBindingList
    &bindings, const QSSGRenderModel *model)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGParticleRenderer::~QSSGParticleRenderer()': the destructor:
    Python removes its C++ QSSGParticleRenderer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGParticleRenderer is created at the first use, not by
    'QSSGParticleRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGParticleRenderer back gives a copy the ritual
    made for Python, in a new cute QSSGParticleRenderer.
  - Each name of Qt's QSSGParticleRenderer that has no cute function yet,
    'generateRhiShaderPipeline', 'getShaderPipelineParticles',
    'prepareParticlesForModel', 'rhiPrepareRenderable',
    'rhiRenderRenderable', 'updateUniformsForParticleModel',
    'updateUniformsForParticles', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGShaderFeatures)
  def particleShaderFeatures(
      features: QSSGShaderFeatures,
  ) -> QSSGShaderFeatures:
    """
    Calls Qt's 'QSSGShaderFeatures
    QSSGParticleRenderer::particleShaderFeatures(const QSSGShaderFeatures
    &features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgparticlerenderer.html#particleShaderFeatures

    Parameters
    ----------

    features : QSSGShaderFeatures
      Passed on as a value: Qt reads the C++ QSSGShaderFeatures, which stays
      Python's own.

    Returns
    -------

    QSSGShaderFeatures
      A new cute QSSGShaderFeatures around the copy Qt gave back. Python owns
      it.
    """
    #  QSSGShaderFeatures QSSGParticleRenderer::particleShaderFeatures(const
    #      QSSGShaderFeatures &features)
    address = Rituals.call(
        'ritual_ZN20QSSGParticleRenderer22particleShaderFeaturesERK18QSSGSh'
        'aderFeatures',
        CuteMixin._valueOf(features),
    )
    from . import QSSGShaderFeatures
    return QSSGShaderFeatures._cuteOwning(address)

  @staticmethod
  @overload(bool)
  def setShaderCacheEnabled(enabled: bool) -> None:
    """
    Calls Qt's 'void QSSGParticleRenderer::setShaderCacheEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgparticlerenderer.html#setShaderCacheEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSSGParticleRenderer::setShaderCacheEnabled(bool enabled)
    Rituals.call(
        'ritual_ZN20QSSGParticleRenderer21setShaderCacheEnabledEb', enabled,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGParticleRenderer'

  #  Qt's '~QSSGParticleRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGParticleRenderer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSSGParticleRendererD1Ev'

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
  def generateRhiShaderPipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGParticleRenderer::generateRhiShaderPipeline(QSSGRenderer &renderer,
    QSSGParticlesRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet, QByteArray &shaderString, const
    QSSGShaderParticleMaterialKeyProperties &shaderKeyProperties)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.generateRhiShaderPipeline' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGParticleRenderer::generateRhiShaderPipeline(QSSGRenderer "
        "&renderer, QSSGParticlesRenderable &inRenderable, const "
        "QSSGShaderFeatures &inFeatureSet, QByteArray &shaderString, const "
        "QSSGShaderParticleMaterialKeyProperties &shaderKeyProperties)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def getShaderPipelineParticles(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGParticleRenderer::getShaderPipelineParticles(QSSGRenderer &renderer,
    QSSGParticlesRenderable &inRenderable, const QSSGShaderFeatures
    &inFeatureSet)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.getShaderPipelineParticles' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGParticleRenderer::getShaderPipelineParticles(QSSGRenderer "
        "&renderer, QSSGParticlesRenderable &inRenderable, const "
        "QSSGShaderFeatures &inFeatureSet)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def prepareParticlesForModel(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGParticleRenderer::prepareParticlesForModel(QSSGRhiShaderPipeline
    &shaderPipeline, QSSGRhiContext *rhiCtx, QSSGRhiShaderResourceBindingList
    &bindings, const QSSGRenderModel *model)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.prepareParticlesForModel' has no cute "
        "function yet. Qt's 'void "
        "QSSGParticleRenderer::prepareParticlesForModel(QSSGRhiShaderPipelin"
        "e &shaderPipeline, QSSGRhiContext *rhiCtx, "
        "QSSGRhiShaderResourceBindingList &bindings, const QSSGRenderModel "
        "*model)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def rhiPrepareRenderable(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGParticleRenderer::rhiPrepareRenderable(QSSGRhiShaderPipeline
    &shaderPipeline, QSSGPassKey passKey, QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps, QSSGParticlesRenderable &renderable,
    const QSSGLayerRenderData &inData, QRhiRenderPassDescriptor
    *renderPassDescriptor, int samples, int viewCount, QSSGRenderCamera
    *alteredCamera, QSSGRenderTextureCubeFace cubeFace,
    QSSGReflectionMapEntry *entry, bool oit)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.rhiPrepareRenderable' has no cute function "
        "yet. Qt's 'void "
        "QSSGParticleRenderer::rhiPrepareRenderable(QSSGRhiShaderPipeline "
        "&shaderPipeline, QSSGPassKey passKey, QSSGRhiContext *rhiCtx, "
        "QSSGRhiGraphicsPipelineState *ps, QSSGParticlesRenderable "
        "&renderable, const QSSGLayerRenderData &inData, "
        "QRhiRenderPassDescriptor *renderPassDescriptor, int samples, int "
        "viewCount, QSSGRenderCamera *alteredCamera, "
        "QSSGRenderTextureCubeFace cubeFace, QSSGReflectionMapEntry *entry, "
        "bool oit)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def rhiRenderRenderable(*__, **_) -> Never:
    """
    Qt's 'void QSSGParticleRenderer::rhiRenderRenderable(QSSGRhiContext
    *rhiCtx, QSSGParticlesRenderable &renderable, bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace, const QSSGRhiGraphicsPipelineState
    &state)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.rhiRenderRenderable' has no cute function "
        "yet. Qt's 'void "
        "QSSGParticleRenderer::rhiRenderRenderable(QSSGRhiContext *rhiCtx, "
        "QSSGParticlesRenderable &renderable, bool *needsSetViewport, "
        "QSSGRenderTextureCubeFace cubeFace, const "
        "QSSGRhiGraphicsPipelineState &state)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def updateUniformsForParticleModel(*__, **_) -> Never:
    """
    Qt's 'void QSSGParticleRenderer::updateUniformsForParticleModel(
    QSSGRhiShaderPipeline &shaderPipeline, char *ubufData, const
    QSSGRenderModel *model, quint32 offset)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.updateUniformsForParticleModel' has no cute "
        "function yet. Qt's 'void "
        "QSSGParticleRenderer::updateUniformsForParticleModel(QSSGRhiShaderP"
        "ipeline &shaderPipeline, char *ubufData, const QSSGRenderModel "
        "*model, quint32 offset)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def updateUniformsForParticles(*__, **_) -> Never:
    """
    Qt's 'void QSSGParticleRenderer::updateUniformsForParticles(const
    QSSGLayerRenderData &inData, QSSGRhiShaderPipeline &shaderPipeline,
    QSSGRhiContext *rhiCtx, char *ubufData, QSSGParticlesRenderable
    &renderable, const QSSGRenderCameraList &cameras)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGParticleRenderer.updateUniformsForParticles' has no cute "
        "function yet. Qt's 'void "
        "QSSGParticleRenderer::updateUniformsForParticles(const "
        "QSSGLayerRenderData &inData, QSSGRhiShaderPipeline "
        "&shaderPipeline, QSSGRhiContext *rhiCtx, char *ubufData, "
        "QSSGParticlesRenderable &renderable, const QSSGRenderCameraList "
        "&cameras)': takes a type Python has no way to hand over yet.")
