"""
QSSGRenderSkyMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderSkyMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderSkyMaterial(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderSkyMaterial: a plain Python object standing
  in front of one C++ QSSGRenderSkyMaterial.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderSkyMaterial is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QSSGRenderSkyMaterial yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderSkyMaterial::~QSSGRenderSkyMaterial()': the destructor:
    Python never removes a C++ QSSGRenderSkyMaterial.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRenderSkyMaterial::ensurePipeline(const QSSGRenderContextInterface
    &sgContext)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRenderSkyMaterial::ensureBackgroundPipeline(const
    QSSGRenderContextInterface &sgContext, const QSSGShaderFeatures
    &tonemapFeatures, quint32 tonemapKey, int viewCount)': takes a type
    Python has no way to hand over yet.
  - Qt's 'quint32 QSSGRenderSkyMaterial::updateUniforms(const
    QSSGRenderContextInterface &sgContext, const QMatrix4x4 &mvp, const
    QVarLengthArray<QMatrix4x4, 6> views)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGRenderSkyMaterial::updateBackgroundUniforms(const
    QSSGRenderContextInterface &sgContext, const QVarLengthArray<QMatrix4x4,
    2> &inverseProjections, const QVarLengthArray<QMatrix4x4, 2>
    &viewRotations, float adjustY, float exposure)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr QSSGRenderSkyMaterial::buildPipeline(const
    QSSGRenderContextInterface &sgContext, QByteArray vertexShader, const
    QSSGShaderCustomMaterialAdapter::StringPairList
    &vertexViewDependentUniforms, const
    QSSGShaderCustomMaterialAdapter::StringPairList &vertexUniforms, const
    QByteArray &fragmentMainSnippet, const
    QSSGShaderCustomMaterialAdapter::StringPairList &fragmentUniforms, const
    QSSGShaderFeatures &features, int viewCount, const QByteArray
    &cacheKeyTag)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGRenderSkyMaterial is created at the first use, not by
    'QSSGRenderSkyMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderSkyMaterial.
  - Each name of Qt's QSSGRenderSkyMaterial that has no cute function yet,
    'buildPipeline', 'ensureBackgroundPipeline', 'ensurePipeline',
    'updateBackgroundUniforms', 'updateUniforms', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderSkyMaterial, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class SkyboxMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderSkyMaterial::SkyboxMode' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Cubemap = Kee[int](0)
    ScreenSpaceFull = Kee[int](1)
    ScreenSpaceHalf = Kee[int](2)
    ScreenSpaceQuarter = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderSkyMaterial'

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
    'QSSGRenderSkyMaterial::QSSGRenderSkyMaterial()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderskymaterial.html#QSSGRenderSkyMaterial
    """
    #  QSSGRenderSkyMaterial::QSSGRenderSkyMaterial()
    self._noteCreation(QSSGRenderSkyMaterial, lambda: Rituals.call(
        'ritual_ZN21QSSGRenderSkyMaterialC1Ev',
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
  def buildPipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr QSSGRenderSkyMaterial::buildPipeline(const
    QSSGRenderContextInterface &sgContext, QByteArray vertexShader, const
    QSSGShaderCustomMaterialAdapter::StringPairList
    &vertexViewDependentUniforms, const
    QSSGShaderCustomMaterialAdapter::StringPairList &vertexUniforms, const
    QByteArray &fragmentMainSnippet, const
    QSSGShaderCustomMaterialAdapter::StringPairList &fragmentUniforms, const
    QSSGShaderFeatures &features, int viewCount, const QByteArray
    &cacheKeyTag)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterial.buildPipeline' has no cute function yet. "
        "Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRenderSkyMaterial::buildPipeline(const "
        "QSSGRenderContextInterface &sgContext, QByteArray vertexShader, "
        "const QSSGShaderCustomMaterialAdapter::StringPairList "
        "&vertexViewDependentUniforms, const "
        "QSSGShaderCustomMaterialAdapter::StringPairList &vertexUniforms, "
        "const QByteArray &fragmentMainSnippet, const "
        "QSSGShaderCustomMaterialAdapter::StringPairList &fragmentUniforms, "
        "const QSSGShaderFeatures &features, int viewCount, const "
        "QByteArray &cacheKeyTag)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def ensureBackgroundPipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRenderSkyMaterial::ensureBackgroundPipeline(const
    QSSGRenderContextInterface &sgContext, const QSSGShaderFeatures
    &tonemapFeatures, quint32 tonemapKey, int viewCount)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterial.ensureBackgroundPipeline' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRenderSkyMaterial::ensureBackgroundPipeline(const "
        "QSSGRenderContextInterface &sgContext, const QSSGShaderFeatures "
        "&tonemapFeatures, quint32 tonemapKey, int viewCount)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def ensurePipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGRenderSkyMaterial::ensurePipeline(const QSSGRenderContextInterface
    &sgContext)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterial.ensurePipeline' has no cute function yet. "
        "Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGRenderSkyMaterial::ensurePipeline(const "
        "QSSGRenderContextInterface &sgContext)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def updateBackgroundUniforms(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderSkyMaterial::updateBackgroundUniforms(const
    QSSGRenderContextInterface &sgContext, const QVarLengthArray<QMatrix4x4,
    2> &inverseProjections, const QVarLengthArray<QMatrix4x4, 2>
    &viewRotations, float adjustY, float exposure)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterial.updateBackgroundUniforms' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderSkyMaterial::updateBackgroundUniforms(const "
        "QSSGRenderContextInterface &sgContext, const "
        "QVarLengthArray<QMatrix4x4, 2> &inverseProjections, const "
        "QVarLengthArray<QMatrix4x4, 2> &viewRotations, float adjustY, "
        "float exposure)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateUniforms(*__, **_) -> Never:
    """
    Qt's 'quint32 QSSGRenderSkyMaterial::updateUniforms(const
    QSSGRenderContextInterface &sgContext, const QMatrix4x4 &mvp, const
    QVarLengthArray<QMatrix4x4, 6> views)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderSkyMaterial.updateUniforms' has no cute function yet. "
        "Qt's 'quint32 QSSGRenderSkyMaterial::updateUniforms(const "
        "QSSGRenderContextInterface &sgContext, const QMatrix4x4 &mvp, "
        "const QVarLengthArray<QMatrix4x4, 6> views)': takes a type Python "
        "has no way to hand over yet.")
