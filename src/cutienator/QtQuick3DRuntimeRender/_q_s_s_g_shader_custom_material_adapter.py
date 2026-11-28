"""
QSSGShaderCustomMaterialAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderCustomMaterialAdapter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QSSGRenderDefaultMaterial, QSSGShaderCache
from . import QSSGShaderMaterialAdapter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D, QVector4D
  from . import QSSGRenderImage


class QSSGShaderCustomMaterialAdapter(QSSGShaderMaterialAdapter):
  """
  The cute side of Qt's QSSGShaderCustomMaterialAdapter: a plain Python
  object standing in front of one C++ QSSGShaderCustomMaterialAdapter.

  It is built on the cute 'QSSGShaderMaterialAdapter', as Qt's
  QSSGShaderCustomMaterialAdapter is built on Qt's QSSGShaderMaterialAdapter,
  and has everything that class has.

  C++ hands a QSSGShaderCustomMaterialAdapter around as a copy, so every C++
  QSSGShaderCustomMaterialAdapter behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderCustomMaterialAdapter that has a ritual
  and that Python can call so far, 57 names in all: 'isPrincipled',
  'isSpecularGlossy', 'isMetalnessEnabled', 'isSpecularEnabled',
  'isVertexColorsEnabled', 'isVertexColorsMaskEnabled',
  'isInvertOpacityMapValue', 'isBaseColorSingleChannelEnabled',
  'isSpecularAmountSingleChannelEnabled', 'isEmissiveSingleChannelEnabled',
  'isClearcoatEnabled', 'isTransmissionEnabled', 'isFresnelScaleBiasEnabled',
  'isClearcoatFresnelScaleBiasEnabled', 'hasLighting', 'usesCustomSkinning',
  'usesCustomMorphing', 'specularModel', 'alphaMode', 'vertexColorRedMask',
  'vertexColorGreenMask', 'vertexColorBlueMask', 'vertexColorAlphaMask',
  'iblProbe', 'emissiveColor', 'color', 'specularTint', 'ior',
  'fresnelScale', 'fresnelBias', 'fresnelPower', 'clearcoatFresnelScale',
  'clearcoatFresnelBias', 'clearcoatFresnelPower', 'metalnessAmount',
  'specularAmount', 'specularRoughness', 'bumpAmount', 'translucentFallOff',
  'diffuseLightWrap', 'occlusionAmount', 'alphaCutOff', 'pointSize',
  'lineWidth', 'heightAmount', 'minHeightSamples', 'maxHeightSamples',
  'clearcoatAmount', 'clearcoatRoughnessAmount', 'clearcoatNormalStrength',
  'transmissionFactor', 'thicknessFactor', 'attenuationDistance',
  'attenuationColor', 'isUnshaded', 'hasCustomShaderSnippet',
  'usesSharedVariables'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGShaderCustomMaterialAdapter::QSSGShaderCustomMaterialAdapter(const
    QSSGRenderCustomMaterial &material)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QByteArray
    QSSGShaderCustomMaterialAdapter::customShaderSnippet(QSSGShaderCache::
    ShaderType type, QSSGShaderLibraryManager &shaderLibraryManager, bool
    multiViewCompatible)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderCustomMaterialAdapter::hasCustomShaderFunction(
    QSSGShaderCache::ShaderType shaderType, const QByteArray &funcName,
    QSSGShaderLibraryManager &shaderLibraryManager)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QSSGShaderCustomMaterialAdapter::setCustomPropertyUniforms(char
    *ubufData, QSSGRhiShaderPipeline &shaderPipeline, const
    QSSGRenderContextInterface &context)': names 'char', which has no cute
    class yet.
  - Qt's 'void QSSGShaderCustomMaterialAdapter::beginPrepareCustomShader(
    CustomShaderPrepWorkData *workData, ShaderCodeAndMetaData
    *codeAndMetaData, const QByteArray &shaderCode,
    QSSGShaderCache::ShaderType type, bool multiViewCompatible)': names
    'QSSGShaderCustomMaterialAdapter::ShaderCodeAndMetaData', which has no
    cute class yet.
  - Qt's 'void
    QSSGShaderCustomMaterialAdapter::finishPrepareCustomShader(QByteArray
    *dst, const CustomShaderPrepWorkData &workData, const
    ShaderCodeAndMetaData &codeAndMetaData, QSSGShaderCache::ShaderType type,
    bool multiViewCompatible, const StringPairList &baseUniforms, const
    StringPairList &baseInputs, const StringPairList &baseOutputs, const
    StringPairList &multiViewDependentSamplers, const StringPairList
    &multiViewDependentUniforms)': takes a type Python has no way to hand
    over yet.
  - Qt's
    'QSSGShaderCustomMaterialAdapter::~QSSGShaderCustomMaterialAdapter()':
    the destructor: Python removes its C++ QSSGShaderCustomMaterialAdapter by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderCustomMaterialAdapter is created at the first use, not
    by 'QSSGShaderCustomMaterialAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderCustomMaterialAdapter back gives a copy the
    ritual made for Python, in a new cute QSSGShaderCustomMaterialAdapter.
  - Each name of Qt's QSSGShaderCustomMaterialAdapter that has no cute
    function yet, '__init__', 'beginPrepareCustomShader',
    'finishPrepareCustomShader', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGShaderCustomMaterialAdapter, each a
  #  class in here as in C++.

  class CustomShaderPrepWorkData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData: a plain Python
    object standing in front of one C++
    QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData.

    C++ hands a QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData
    around as a copy, so every C++
    QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData::
      ~CustomShaderPrepWorkData()': the destructor: Python removes its C++
      QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData is
      created at the first use, not by
      'QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData back gives a
      copy the ritual made for Python, in a new cute
      QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData'

    #  Qt's '~QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QSSGShaderCustomMaterialAdapter24CustomShaderPrepWorkDataD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderCustomMaterialAdapter'

  #  Qt's '~QSSGShaderCustomMaterialAdapter()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderCustomMaterialAdapter behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QSSGShaderCustomMaterialAdapterD1Ev'

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
    'QSSGShaderCustomMaterialAdapter::QSSGShaderCustomMaterialAdapter(const
    QSSGRenderCustomMaterial &material)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCustomMaterialAdapter.__init__' has no cute function "
        "yet. Qt's "
        "'QSSGShaderCustomMaterialAdapter::QSSGShaderCustomMaterialAdapter(c"
        "onst QSSGRenderCustomMaterial &material)': takes a type Python has "
        "no way to hand over yet.")

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

  def isPrincipled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isPrincipled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#isPrincipled
    """
    #  bool QSSGShaderCustomMaterialAdapter::isPrincipled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter12isPrincipledEv',
    )

  def isSpecularGlossy(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isSpecularGlossy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isSpecularGlossy()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter16isSpecularGlossyEv',
    )

  def isMetalnessEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isMetalnessEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isMetalnessEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18isMetalnessEnabledEv',
    )

  def isSpecularEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isSpecularEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isSpecularEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter17isSpecularEnabledEv',
    )

  def isVertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isVertexColorsEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isVertexColorsEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter21isVertexColorsEnabledE'
        'v',
    )

  def isVertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isVertexColorsMaskEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isVertexColorsMaskEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter25isVertexColorsMaskEnab'
        'ledEv',
    )

  def isInvertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isInvertOpacityMapValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isInvertOpacityMapValue()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter23isInvertOpacityMapValu'
        'eEv',
    )

  def isBaseColorSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isBaseColorSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool
    #      QSSGShaderCustomMaterialAdapter::isBaseColorSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter31isBaseColorSingleChann'
        'elEnabledEv',
    )

  def isSpecularAmountSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isSpecularAmountSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::
    #      isSpecularAmountSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter36isSpecularAmountSingle'
        'ChannelEnabledEv',
    )

  def isEmissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isEmissiveSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isEmissiveSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter30isEmissiveSingleChanne'
        'lEnabledEv',
    )

  def isClearcoatEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isClearcoatEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isClearcoatEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18isClearcoatEnabledEv',
    )

  def isTransmissionEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isTransmissionEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isTransmissionEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter21isTransmissionEnabledE'
        'v',
    )

  def isFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::isFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter25isFresnelScaleBiasEnab'
        'ledEv',
    )

  def isClearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderCustomMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::
    #      isClearcoatFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter34isClearcoatFresnelScal'
        'eBiasEnabledEv',
    )

  def hasLighting(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::hasLighting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#hasLighting
    """
    #  bool QSSGShaderCustomMaterialAdapter::hasLighting()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter11hasLightingEv',
    )

  def usesCustomSkinning(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::usesCustomSkinning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::usesCustomSkinning()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18usesCustomSkinningEv',
    )

  def usesCustomMorphing(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::usesCustomMorphing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::usesCustomMorphing()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18usesCustomMorphingEv',
    )

  def specularModel(self) -> QSSGRenderDefaultMaterial.MaterialSpecularModel:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialSpecularModel
    QSSGShaderCustomMaterialAdapter::specularModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#specularModel

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialSpecularModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialSpecularModel(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialSpecularModel
    #      QSSGShaderCustomMaterialAdapter::specularModel()
    return QSSGRenderDefaultMaterial.MaterialSpecularModel(
        self.uglySide.call(
            'ritual_ZN31QSSGShaderCustomMaterialAdapter13specularModelEv',
        ))

  def alphaMode(self) -> QSSGRenderDefaultMaterial.MaterialAlphaMode:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode
    QSSGShaderCustomMaterialAdapter::alphaMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#alphaMode

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialAlphaMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialAlphaMode(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialAlphaMode
    #      QSSGShaderCustomMaterialAdapter::alphaMode()
    return QSSGRenderDefaultMaterial.MaterialAlphaMode(self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter9alphaModeEv',
    ))

  def vertexColorRedMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderCustomMaterialAdapter::vertexColorRedMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderCustomMaterialAdapter::vertexColorRedMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18vertexColorRedMaskEv',
    ))

  def vertexColorGreenMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderCustomMaterialAdapter::vertexColorGreenMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderCustomMaterialAdapter::vertexColorGreenMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter20vertexColorGreenMaskEv',
    ))

  def vertexColorBlueMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderCustomMaterialAdapter::vertexColorBlueMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderCustomMaterialAdapter::vertexColorBlueMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter19vertexColorBlueMaskEv',
    ))

  def vertexColorAlphaMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderCustomMaterialAdapter::vertexColorAlphaMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderCustomMaterialAdapter::vertexColorAlphaMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter20vertexColorAlphaMaskEv',
    ))

  def iblProbe(self) -> Optional[QSSGRenderImage]:
    """
    Calls Qt's 'QSSGRenderImage
    *QSSGShaderCustomMaterialAdapter::iblProbe()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#iblProbe

    Returns
    -------

    Optional[QSSGRenderImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderImage *QSSGShaderCustomMaterialAdapter::iblProbe()
    address = self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter8iblProbeEv',
    )
    from . import QSSGRenderImage
    return QSSGRenderImage._cuteAt(address)

  def emissiveColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderCustomMaterialAdapter::emissiveColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#emissiveColor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderCustomMaterialAdapter::emissiveColor()
    address = self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter13emissiveColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def color(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QSSGShaderCustomMaterialAdapter::color()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#color

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QSSGShaderCustomMaterialAdapter::color()
    address = self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter5colorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def specularTint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderCustomMaterialAdapter::specularTint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#specularTint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderCustomMaterialAdapter::specularTint()
    address = self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter12specularTintEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def ior(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::ior()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#ior
    """
    #  float QSSGShaderCustomMaterialAdapter::ior()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter3iorEv',
    )

  def fresnelScale(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::fresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#fresnelScale
    """
    #  float QSSGShaderCustomMaterialAdapter::fresnelScale()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter12fresnelScaleEv',
    )

  def fresnelBias(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::fresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#fresnelBias
    """
    #  float QSSGShaderCustomMaterialAdapter::fresnelBias()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter11fresnelBiasEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::fresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#fresnelPower
    """
    #  float QSSGShaderCustomMaterialAdapter::fresnelPower()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter12fresnelPowerEv',
    )

  def clearcoatFresnelScale(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::clearcoatFresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelScale()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter21clearcoatFresnelScaleE'
        'v',
    )

  def clearcoatFresnelBias(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::clearcoatFresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelBias()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter20clearcoatFresnelBiasEv',
    )

  def clearcoatFresnelPower(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::clearcoatFresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelPower()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter21clearcoatFresnelPowerE'
        'v',
    )

  def metalnessAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::metalnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::metalnessAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter15metalnessAmountEv',
    )

  def specularAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::specularAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::specularAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter14specularAmountEv',
    )

  def specularRoughness(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::specularRoughness()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::specularRoughness()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter17specularRoughnessEv',
    )

  def bumpAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::bumpAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#bumpAmount
    """
    #  float QSSGShaderCustomMaterialAdapter::bumpAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter10bumpAmountEv',
    )

  def translucentFallOff(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::translucentFallOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::translucentFallOff()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18translucentFallOffEv',
    )

  def diffuseLightWrap(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::diffuseLightWrap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::diffuseLightWrap()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter16diffuseLightWrapEv',
    )

  def occlusionAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::occlusionAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::occlusionAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter15occlusionAmountEv',
    )

  def alphaCutOff(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::alphaCutOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#alphaCutOff
    """
    #  float QSSGShaderCustomMaterialAdapter::alphaCutOff()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter11alphaCutOffEv',
    )

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::pointSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#pointSize
    """
    #  float QSSGShaderCustomMaterialAdapter::pointSize()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::lineWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#lineWidth
    """
    #  float QSSGShaderCustomMaterialAdapter::lineWidth()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter9lineWidthEv',
    )

  def heightAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::heightAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#heightAmount
    """
    #  float QSSGShaderCustomMaterialAdapter::heightAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter12heightAmountEv',
    )

  def minHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::minHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::minHeightSamples()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter16minHeightSamplesEv',
    )

  def maxHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::maxHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::maxHeightSamples()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter16maxHeightSamplesEv',
    )

  def clearcoatAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::clearcoatAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter15clearcoatAmountEv',
    )

  def clearcoatRoughnessAmount(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::clearcoatRoughnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatRoughnessAmount()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter24clearcoatRoughnessAmou'
        'ntEv',
    )

  def clearcoatNormalStrength(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::clearcoatNormalStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::clearcoatNormalStrength()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter23clearcoatNormalStrengt'
        'hEv',
    )

  def transmissionFactor(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::transmissionFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::transmissionFactor()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter18transmissionFactorEv',
    )

  def thicknessFactor(self) -> float:
    """
    Calls Qt's 'float QSSGShaderCustomMaterialAdapter::thicknessFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::thicknessFactor()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter15thicknessFactorEv',
    )

  def attenuationDistance(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderCustomMaterialAdapter::attenuationDistance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  float QSSGShaderCustomMaterialAdapter::attenuationDistance()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter19attenuationDistanceEv',
    )

  def attenuationColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QSSGShaderCustomMaterialAdapter::attenuationColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderCustomMaterialAdapter::attenuationColor()
    address = self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter16attenuationColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isUnshaded(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::isUnshaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html#isUnshaded
    """
    #  bool QSSGShaderCustomMaterialAdapter::isUnshaded()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter10isUnshadedEv',
    )

  @overload(QSSGShaderCache.ShaderType)
  def hasCustomShaderSnippet(self, type: QSSGShaderCache.ShaderType) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::hasCustomShaderSnippet(
    QSSGShaderCache::ShaderType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html

    Parameters
    ----------

    type : QSSGShaderCache.ShaderType
      Passed on as its number.
    """
    #  bool QSSGShaderCustomMaterialAdapter::hasCustomShaderSnippet(
    #      QSSGShaderCache::ShaderType type)
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter22hasCustomShaderSnippet'
        'EN15QSSGShaderCache10ShaderTypeE',
        type.value,
    )

  def usesSharedVariables(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderCustomMaterialAdapter::usesSharedVariables()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercustommaterialadapter.html
    """
    #  bool QSSGShaderCustomMaterialAdapter::usesSharedVariables()
    return self.uglySide.call(
        'ritual_ZN31QSSGShaderCustomMaterialAdapter19usesSharedVariablesEv',
    )

  @staticmethod
  def beginPrepareCustomShader(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderCustomMaterialAdapter::beginPrepareCustomShader(
    CustomShaderPrepWorkData *workData, ShaderCodeAndMetaData
    *codeAndMetaData, const QByteArray &shaderCode,
    QSSGShaderCache::ShaderType type, bool multiViewCompatible)': names
    'QSSGShaderCustomMaterialAdapter::ShaderCodeAndMetaData', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCustomMaterialAdapter.beginPrepareCustomShader' has no "
        "cute function yet. Qt's 'void "
        "QSSGShaderCustomMaterialAdapter::beginPrepareCustomShader(CustomSha"
        "derPrepWorkData *workData, ShaderCodeAndMetaData *codeAndMetaData, "
        "const QByteArray &shaderCode, QSSGShaderCache::ShaderType type, "
        "bool multiViewCompatible)': names "
        "'QSSGShaderCustomMaterialAdapter::ShaderCodeAndMetaData', which "
        "has no cute class yet.")

  @staticmethod
  def finishPrepareCustomShader(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderCustomMaterialAdapter::finishPrepareCustomShader(QByteArray
    *dst, const CustomShaderPrepWorkData &workData, const
    ShaderCodeAndMetaData &codeAndMetaData, QSSGShaderCache::ShaderType type,
    bool multiViewCompatible, const StringPairList &baseUniforms, const
    StringPairList &baseInputs, const StringPairList &baseOutputs, const
    StringPairList &multiViewDependentSamplers, const StringPairList
    &multiViewDependentUniforms)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCustomMaterialAdapter.finishPrepareCustomShader' has no "
        "cute function yet. Qt's 'void "
        "QSSGShaderCustomMaterialAdapter::finishPrepareCustomShader(QByteArr"
        "ay *dst, const CustomShaderPrepWorkData &workData, const "
        "ShaderCodeAndMetaData &codeAndMetaData, "
        "QSSGShaderCache::ShaderType type, bool multiViewCompatible, const "
        "StringPairList &baseUniforms, const StringPairList &baseInputs, "
        "const StringPairList &baseOutputs, const StringPairList "
        "&multiViewDependentSamplers, const StringPairList "
        "&multiViewDependentUniforms)': takes a type Python has no way to "
        "hand over yet.")
