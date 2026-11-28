"""
QSSGBuiltInRhiShaderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGBuiltInRhiShaderCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from . import QSSGRenderLayer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGBuiltInRhiShaderCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGBuiltInRhiShaderCache: a plain Python object
  standing in front of one C++ QSSGBuiltInRhiShaderCache.

  C++ hands a QSSGBuiltInRhiShaderCache around as a copy, so every C++
  QSSGBuiltInRhiShaderCache behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGBuiltInRhiShaderCache that has a ritual and that
  Python can call so far, 1 name in all: 'releaseCachedResources'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGBuiltInRhiShaderCache::QSSGBuiltInRhiShaderCache(QSSGShaderCache
    &shaderCache)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiGridShader(int viewCount)': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSsaoShader(int viewCount)': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyBoxCubeShader(QSSGRenderLayer::
    TonemapMode tonemapMode, bool isLinear, int viewCount)': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyBoxShader(QSSGRenderLayer::
    TonemapMode tonemapMode, bool isRGBE, int viewCount)': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSupersampleResolveShader(int
    viewCount)': gives a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiProgressiveAAShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiMotionVectorShader(bool skin, bool
    instance, bool morph)': gives a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiTemporalAAShader()': gives a type Python
    has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSimpleQuadShader(int viewCount,
    QSSGRenderLayer::TonemapMode tonemapMode)': gives a type Python has no
    way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiLightmapUVRasterizationShader(
    LightmapUVRasterizationShaderMode mode)': gives a type Python has no way
    to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiLightmapDilateShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiDebugObjectShader(int viewCount)': gives
    a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiReflectionprobePreFilterShader()': gives
    a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterNormalizeShader()': gives
    a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhienvironmentmapPreFilterShader(bool
    isRGBE)': gives a type Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiEnvironmentmapShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearMRTShader()': gives a type Python
    has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiOitCompositeShader(QSSGRenderLayer::
    OITMethod method, bool multisample, bool use_buffers)': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiCubeMapToAtlasShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearShadowMapShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearImageShader()': gives a type Python
    has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearBufferShader()': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getBuiltinRhiShader(const QByteArray &name,
    BuiltinShader &storage, int viewCount, QSSGRhiShaderPipeline::StageFlags
    vertexStageFlags)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGBuiltInRhiShaderCache::~QSSGBuiltInRhiShaderCache()': the
    destructor: Python removes its C++ QSSGBuiltInRhiShaderCache by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGBuiltInRhiShaderCache is created at the first use, not by
    'QSSGBuiltInRhiShaderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGBuiltInRhiShaderCache back gives a copy the
    ritual made for Python, in a new cute QSSGBuiltInRhiShaderCache.
  - Each name of Qt's QSSGBuiltInRhiShaderCache that has no cute function
    yet, '__init__', 'getBuiltinRhiShader', 'getRhiClearBufferShader',
    'getRhiClearImageShader', 'getRhiClearMRTShader',
    'getRhiClearShadowMapShader', 'getRhiCubeMapToAtlasShader',
    'getRhiDebugObjectShader', 'getRhiEnvironmentmapShader',
    'getRhiGridShader', 'getRhiLightmapDilateShader',
    'getRhiLightmapUVRasterizationShader', 'getRhiMotionVectorShader',
    'getRhiOitCompositeShader', 'getRhiProgressiveAAShader',
    'getRhiReflectionprobePreFilterShader', 'getRhiSimpleQuadShader',
    'getRhiSkyBoxCubeShader', 'getRhiSkyBoxShader',
    'getRhiSkyIblPreFilterNormalizeShader', 'getRhiSkyIblPreFilterShader',
    'getRhiSsaoShader', 'getRhiSupersampleResolveShader',
    'getRhiTemporalAAShader', 'getRhienvironmentmapPreFilterShader', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGBuiltInRhiShaderCache, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class LightmapUVRasterizationShaderMode(CuteNum, scoped=True):
    """
    The enum 'QSSGBuiltInRhiShaderCache::LightmapUVRasterizationShaderMode'
    of Qt, with the 3 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Default = Kee[int](0)
    Uv = Kee[int](1)
    UvTangent = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBuiltInRhiShaderCache'

  #  Qt's '~QSSGBuiltInRhiShaderCache()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGBuiltInRhiShaderCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QSSGBuiltInRhiShaderCacheD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QSSGBuiltInRhiShaderCache::QSSGBuiltInRhiShaderCache(QSSGShaderCache
    &shaderCache)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.__init__' has no cute function yet. "
        "Qt's "
        "'QSSGBuiltInRhiShaderCache::QSSGBuiltInRhiShaderCache(QSSGShaderCac"
        "he &shaderCache)': takes a type Python has no way to hand over yet."
    )

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
    Calls Qt's 'void QSSGBuiltInRhiShaderCache::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbuiltinrhishadercache.html
    """
    #  void QSSGBuiltInRhiShaderCache::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN25QSSGBuiltInRhiShaderCache22releaseCachedResourcesEv',
    )

  @staticmethod
  def getBuiltinRhiShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getBuiltinRhiShader(const QByteArray &name,
    BuiltinShader &storage, int viewCount, QSSGRhiShaderPipeline::StageFlags
    vertexStageFlags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getBuiltinRhiShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getBuiltinRhiShader(const QByteArray "
        "&name, BuiltinShader &storage, int viewCount, "
        "QSSGRhiShaderPipeline::StageFlags vertexStageFlags)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def getRhiClearBufferShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearBufferShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiClearBufferShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiClearBufferShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiClearImageShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearImageShader()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiClearImageShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiClearImageShader()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getRhiClearMRTShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearMRTShader()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiClearMRTShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiClearMRTShader()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getRhiClearShadowMapShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiClearShadowMapShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiClearShadowMapShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiClearShadowMapShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiCubeMapToAtlasShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiCubeMapToAtlasShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiCubeMapToAtlasShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiCubeMapToAtlasShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiDebugObjectShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiDebugObjectShader(int viewCount)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiDebugObjectShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiDebugObjectShader(int "
        "viewCount)': gives a type Python has no way to take yet.")

  @staticmethod
  def getRhiEnvironmentmapShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiEnvironmentmapShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiEnvironmentmapShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiEnvironmentmapShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiGridShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiGridShader(int viewCount)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiGridShader' has no cute function "
        "yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiGridShader(int viewCount)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def getRhiLightmapDilateShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiLightmapDilateShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiLightmapDilateShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiLightmapDilateShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiLightmapUVRasterizationShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiLightmapUVRasterizationShader(
    LightmapUVRasterizationShaderMode mode)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiLightmapUVRasterizationShader' "
        "has no cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiLightmapUVRasterizationShader(Ligh"
        "tmapUVRasterizationShaderMode mode)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def getRhiMotionVectorShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiMotionVectorShader(bool skin, bool
    instance, bool morph)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiMotionVectorShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiMotionVectorShader(bool skin, "
        "bool instance, bool morph)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def getRhiOitCompositeShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiOitCompositeShader(QSSGRenderLayer::
    OITMethod method, bool multisample, bool use_buffers)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiOitCompositeShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiOitCompositeShader(QSSGRenderLayer"
        "::OITMethod method, bool multisample, bool use_buffers)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiProgressiveAAShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiProgressiveAAShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiProgressiveAAShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiProgressiveAAShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiReflectionprobePreFilterShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiReflectionprobePreFilterShader()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiReflectionprobePreFilterShader' "
        "has no cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiReflectionprobePreFilterShader()':"
        " gives a type Python has no way to take yet.")

  @staticmethod
  def getRhiSimpleQuadShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSimpleQuadShader(int viewCount,
    QSSGRenderLayer::TonemapMode tonemapMode)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSimpleQuadShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSimpleQuadShader(int viewCount, "
        "QSSGRenderLayer::TonemapMode tonemapMode)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def getRhiSkyBoxCubeShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyBoxCubeShader(QSSGRenderLayer::
    TonemapMode tonemapMode, bool isLinear, int viewCount)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSkyBoxCubeShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSkyBoxCubeShader(QSSGRenderLayer::"
        "TonemapMode tonemapMode, bool isLinear, int viewCount)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiSkyBoxShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyBoxShader(QSSGRenderLayer::
    TonemapMode tonemapMode, bool isRGBE, int viewCount)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSkyBoxShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSkyBoxShader(QSSGRenderLayer::Tone"
        "mapMode tonemapMode, bool isRGBE, int viewCount)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getRhiSkyIblPreFilterNormalizeShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterNormalizeShader()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSkyIblPreFilterNormalizeShader' "
        "has no cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterNormalizeShader()':"
        " gives a type Python has no way to take yet.")

  @staticmethod
  def getRhiSkyIblPreFilterShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterShader()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSkyIblPreFilterShader' has no "
        "cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterShader()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getRhiSsaoShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSsaoShader(int viewCount)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSsaoShader' has no cute function "
        "yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSsaoShader(int viewCount)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def getRhiSupersampleResolveShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiSupersampleResolveShader(int
    viewCount)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiSupersampleResolveShader' has no "
        "cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiSupersampleResolveShader(int "
        "viewCount)': gives a type Python has no way to take yet.")

  @staticmethod
  def getRhiTemporalAAShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhiTemporalAAShader()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhiTemporalAAShader' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhiTemporalAAShader()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def getRhienvironmentmapPreFilterShader(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGBuiltInRhiShaderCache::getRhienvironmentmapPreFilterShader(bool
    isRGBE)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGBuiltInRhiShaderCache.getRhienvironmentmapPreFilterShader' "
        "has no cute function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGBuiltInRhiShaderCache::getRhienvironmentmapPreFilterShader(bool"
        " isRGBE)': gives a type Python has no way to take yet.")
