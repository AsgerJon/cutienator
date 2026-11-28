"""
QSSGShaderMaterialAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderMaterialAdapter to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QSSGRenderDefaultMaterial, QSSGShaderCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D, QVector4D
  from . import QSSGRenderImage


class QSSGShaderMaterialAdapter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderMaterialAdapter: a plain Python object
  standing in front of one C++ QSSGShaderMaterialAdapter.

  What exists
  -----------

  Every function of Qt's QSSGShaderMaterialAdapter that has a ritual and that
  Python can call so far, 57 names in all: 'isPrincipled',
  'isSpecularGlossy', 'isMetalnessEnabled', 'isSpecularEnabled',
  'isVertexColorsEnabled', 'isVertexColorsMaskEnabled',
  'isInvertOpacityMapValue', 'isBaseColorSingleChannelEnabled',
  'isSpecularAmountSingleChannelEnabled', 'isEmissiveSingleChannelEnabled',
  'isFresnelScaleBiasEnabled', 'isClearcoatFresnelScaleBiasEnabled',
  'isClearcoatEnabled', 'isTransmissionEnabled', 'hasLighting',
  'usesCustomSkinning', 'usesCustomMorphing', 'specularModel', 'alphaMode',
  'vertexColorRedMask', 'vertexColorGreenMask', 'vertexColorBlueMask',
  'vertexColorAlphaMask', 'iblProbe', 'emissiveColor', 'color',
  'specularTint', 'ior', 'fresnelScale', 'fresnelBias', 'fresnelPower',
  'clearcoatFresnelScale', 'clearcoatFresnelBias', 'clearcoatFresnelPower',
  'metalnessAmount', 'specularAmount', 'specularRoughness', 'bumpAmount',
  'translucentFallOff', 'diffuseLightWrap', 'occlusionAmount', 'alphaCutOff',
  'pointSize', 'lineWidth', 'heightAmount', 'minHeightSamples',
  'maxHeightSamples', 'clearcoatAmount', 'clearcoatRoughnessAmount',
  'clearcoatNormalStrength', 'transmissionFactor', 'thicknessFactor',
  'attenuationDistance', 'attenuationColor', 'isUnshaded',
  'hasCustomShaderSnippet', 'usesSharedVariables'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderMaterialAdapter *QSSGShaderMaterialAdapter::create(const
    QSSGRenderGraphObject &materialNode)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSSGShaderMaterialAdapter::~QSSGShaderMaterialAdapter()': the
    destructor: Python never removes a C++ QSSGShaderMaterialAdapter.
  - Qt's 'QByteArray
    QSSGShaderMaterialAdapter::customShaderSnippet(QSSGShaderCache::
    ShaderType type, QSSGShaderLibraryManager &shaderLibraryManager, bool
    multiViewCompatible)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGShaderMaterialAdapter::hasCustomShaderFunction(QSSGShaderCache::
    ShaderType shaderType, const QByteArray &funcName,
    QSSGShaderLibraryManager &shaderLibraryManager)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QSSGShaderMaterialAdapter::setCustomPropertyUniforms(char
    *ubufData, QSSGRhiShaderPipeline &shaderPipeline, const
    QSSGRenderContextInterface &context)': names 'char', which has no cute
    class yet.

  What to expect
  --------------

  - The C++ QSSGShaderMaterialAdapter is created at the first use, not by
    'QSSGShaderMaterialAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGShaderMaterialAdapter.
  - Each name of Qt's QSSGShaderMaterialAdapter that has no cute function
    yet, 'create', 'customShaderSnippet', 'hasCustomShaderFunction',
    'setCustomPropertyUniforms', holds a function that raises
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
  __qt_class__ = 'QSSGShaderMaterialAdapter'

  #  A C++ QSSGShaderMaterialAdapter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGShaderMaterialAdapter'

  #  The functions Qt calls itself that QSSGShaderMaterialAdapter is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'customShaderSnippet': (
          'QByteArray '
          'QSSGShaderMaterialAdapter::customShaderSnippet(QSSGShaderCache::'
          'ShaderType, QSSGShaderLibraryManager &, bool)',
      ),
      'hasCustomShaderFunction': (
          'bool '
          'QSSGShaderMaterialAdapter::hasCustomShaderFunction(QSSGShaderCac'
          'he::ShaderType, const QByteArray &, QSSGShaderLibraryManager &)',
      ),
      'setCustomPropertyUniforms': (
          'void QSSGShaderMaterialAdapter::setCustomPropertyUniforms(char '
          '*, QSSGRhiShaderPipeline &, const QSSGRenderContextInterface &)',
      ),
  }

  #  The functions Qt calls itself that QSSGShaderMaterialAdapter is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isPrincipled': (
          ('_ZN25QSSGShaderMaterialAdapter12isPrincipledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSpecularGlossy': (
          ('_ZN25QSSGShaderMaterialAdapter16isSpecularGlossyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isMetalnessEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter18isMetalnessEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSpecularEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter17isSpecularEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isVertexColorsEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter21isVertexColorsEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isVertexColorsMaskEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter25isVertexColorsMaskEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isInvertOpacityMapValue': (
          ('_ZN25QSSGShaderMaterialAdapter23isInvertOpacityMapValueEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isBaseColorSingleChannelEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter31isBaseColorSingleChannelEnabled'
           'Ev',
           ('bool', 'number', ''),
           ()),
      ),
      'isSpecularAmountSingleChannelEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter36isSpecularAmountSingleChannelEn'
           'abledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isEmissiveSingleChannelEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter30isEmissiveSingleChannelEnabledE'
           'v',
           ('bool', 'number', ''),
           ()),
      ),
      'isFresnelScaleBiasEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter25isFresnelScaleBiasEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isClearcoatFresnelScaleBiasEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter34isClearcoatFresnelScaleBiasEnab'
           'ledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isClearcoatEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter18isClearcoatEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isTransmissionEnabled': (
          ('_ZN25QSSGShaderMaterialAdapter21isTransmissionEnabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasLighting': (
          ('_ZN25QSSGShaderMaterialAdapter11hasLightingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'usesCustomSkinning': (
          ('_ZN25QSSGShaderMaterialAdapter18usesCustomSkinningEv',
           ('bool', 'number', ''),
           ()),
      ),
      'usesCustomMorphing': (
          ('_ZN25QSSGShaderMaterialAdapter18usesCustomMorphingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'specularModel': (
          ('_ZN25QSSGShaderMaterialAdapter13specularModelEv',
           ('int', 'enum',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.MaterialSpecularModel'),
           ()),
      ),
      'alphaMode': (
          ('_ZN25QSSGShaderMaterialAdapter9alphaModeEv',
           ('int', 'enum',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.MaterialAlphaMode'),
           ()),
      ),
      'vertexColorRedMask': (
          ('_ZN25QSSGShaderMaterialAdapter18vertexColorRedMaskEv',
           ('int', 'flags',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.VertexColorMask'),
           ()),
      ),
      'vertexColorGreenMask': (
          ('_ZN25QSSGShaderMaterialAdapter20vertexColorGreenMaskEv',
           ('int', 'flags',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.VertexColorMask'),
           ()),
      ),
      'vertexColorBlueMask': (
          ('_ZN25QSSGShaderMaterialAdapter19vertexColorBlueMaskEv',
           ('int', 'flags',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.VertexColorMask'),
           ()),
      ),
      'vertexColorAlphaMask': (
          ('_ZN25QSSGShaderMaterialAdapter20vertexColorAlphaMaskEv',
           ('int', 'flags',
            'QtQuick3DRuntimeRender:QSSGRenderDefaultMaterial.VertexColorMask'),
           ()),
      ),
      'iblProbe': (
          ('_ZN25QSSGShaderMaterialAdapter8iblProbeEv',
           ('address', 'address', 'QtQuick3DRuntimeRender:QSSGRenderImage'),
           ()),
      ),
      'emissiveColor': (
          ('_ZN25QSSGShaderMaterialAdapter13emissiveColorEv',
           ('address', 'value', 'QtGui:QVector3D'),
           ()),
      ),
      'color': (
          ('_ZN25QSSGShaderMaterialAdapter5colorEv',
           ('address', 'value', 'QtGui:QVector4D'),
           ()),
      ),
      'specularTint': (
          ('_ZN25QSSGShaderMaterialAdapter12specularTintEv',
           ('address', 'value', 'QtGui:QVector3D'),
           ()),
      ),
      'ior': (
          ('_ZN25QSSGShaderMaterialAdapter3iorEv',
           ('float', 'number', ''),
           ()),
      ),
      'fresnelScale': (
          ('_ZN25QSSGShaderMaterialAdapter12fresnelScaleEv',
           ('float', 'number', ''),
           ()),
      ),
      'fresnelBias': (
          ('_ZN25QSSGShaderMaterialAdapter11fresnelBiasEv',
           ('float', 'number', ''),
           ()),
      ),
      'fresnelPower': (
          ('_ZN25QSSGShaderMaterialAdapter12fresnelPowerEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatFresnelScale': (
          ('_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelScaleEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatFresnelBias': (
          ('_ZN25QSSGShaderMaterialAdapter20clearcoatFresnelBiasEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatFresnelPower': (
          ('_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelPowerEv',
           ('float', 'number', ''),
           ()),
      ),
      'metalnessAmount': (
          ('_ZN25QSSGShaderMaterialAdapter15metalnessAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'specularAmount': (
          ('_ZN25QSSGShaderMaterialAdapter14specularAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'specularRoughness': (
          ('_ZN25QSSGShaderMaterialAdapter17specularRoughnessEv',
           ('float', 'number', ''),
           ()),
      ),
      'bumpAmount': (
          ('_ZN25QSSGShaderMaterialAdapter10bumpAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'translucentFallOff': (
          ('_ZN25QSSGShaderMaterialAdapter18translucentFallOffEv',
           ('float', 'number', ''),
           ()),
      ),
      'diffuseLightWrap': (
          ('_ZN25QSSGShaderMaterialAdapter16diffuseLightWrapEv',
           ('float', 'number', ''),
           ()),
      ),
      'occlusionAmount': (
          ('_ZN25QSSGShaderMaterialAdapter15occlusionAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'alphaCutOff': (
          ('_ZN25QSSGShaderMaterialAdapter11alphaCutOffEv',
           ('float', 'number', ''),
           ()),
      ),
      'pointSize': (
          ('_ZN25QSSGShaderMaterialAdapter9pointSizeEv',
           ('float', 'number', ''),
           ()),
      ),
      'lineWidth': (
          ('_ZN25QSSGShaderMaterialAdapter9lineWidthEv',
           ('float', 'number', ''),
           ()),
      ),
      'heightAmount': (
          ('_ZN25QSSGShaderMaterialAdapter12heightAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'minHeightSamples': (
          ('_ZN25QSSGShaderMaterialAdapter16minHeightSamplesEv',
           ('float', 'number', ''),
           ()),
      ),
      'maxHeightSamples': (
          ('_ZN25QSSGShaderMaterialAdapter16maxHeightSamplesEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatAmount': (
          ('_ZN25QSSGShaderMaterialAdapter15clearcoatAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatRoughnessAmount': (
          ('_ZN25QSSGShaderMaterialAdapter24clearcoatRoughnessAmountEv',
           ('float', 'number', ''),
           ()),
      ),
      'clearcoatNormalStrength': (
          ('_ZN25QSSGShaderMaterialAdapter23clearcoatNormalStrengthEv',
           ('float', 'number', ''),
           ()),
      ),
      'transmissionFactor': (
          ('_ZN25QSSGShaderMaterialAdapter18transmissionFactorEv',
           ('float', 'number', ''),
           ()),
      ),
      'thicknessFactor': (
          ('_ZN25QSSGShaderMaterialAdapter15thicknessFactorEv',
           ('float', 'number', ''),
           ()),
      ),
      'attenuationDistance': (
          ('_ZN25QSSGShaderMaterialAdapter19attenuationDistanceEv',
           ('float', 'number', ''),
           ()),
      ),
      'attenuationColor': (
          ('_ZN25QSSGShaderMaterialAdapter16attenuationColorEv',
           ('address', 'value', 'QtGui:QVector3D'),
           ()),
      ),
      'isUnshaded': (
          ('_ZN25QSSGShaderMaterialAdapter10isUnshadedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasCustomShaderSnippet': (
          ('_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippetEN15QSSGS'
           'haderCache10ShaderTypeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtQuick3DRuntimeRender:QSSGShaderCache.ShaderType'),
           )),
      ),
      'usesSharedVariables': (
          ('_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

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

  def isPrincipled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isPrincipled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isPrincipled
    """
    #  bool QSSGShaderMaterialAdapter::isPrincipled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter12isPrincipledEv',
    )

  def isSpecularGlossy(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isSpecularGlossy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isSpecularGlossy
    """
    #  bool QSSGShaderMaterialAdapter::isSpecularGlossy()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter16isSpecularGlossyEv',
    )

  def isMetalnessEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isMetalnessEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isMetalnessEnabled
    """
    #  bool QSSGShaderMaterialAdapter::isMetalnessEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18isMetalnessEnabledEv',
    )

  def isSpecularEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isSpecularEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isSpecularEnabled
    """
    #  bool QSSGShaderMaterialAdapter::isSpecularEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter17isSpecularEnabledEv',
    )

  def isVertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isVertexColorsEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isVertexColorsEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter21isVertexColorsEnabledEv',
    )

  def isVertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isVertexColorsMaskEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isVertexColorsMaskEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter25isVertexColorsMaskEnabledEv',
    )

  def isInvertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isInvertOpacityMapValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isInvertOpacityMapValue()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter23isInvertOpacityMapValueEv',
    )

  def isBaseColorSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderMaterialAdapter::isBaseColorSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isBaseColorSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter31isBaseColorSingleChannelEnab'
        'ledEv',
    )

  def isSpecularAmountSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderMaterialAdapter::isSpecularAmountSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isSpecularAmountSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter36isSpecularAmountSingleChanne'
        'lEnabledEv',
    )

  def isEmissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderMaterialAdapter::isEmissiveSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isEmissiveSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter30isEmissiveSingleChannelEnabl'
        'edEv',
    )

  def isFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter25isFresnelScaleBiasEnabledEv',
    )

  def isClearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter34isClearcoatFresnelScaleBiasE'
        'nabledEv',
    )

  def isClearcoatEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isClearcoatEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isClearcoatEnabled
    """
    #  bool QSSGShaderMaterialAdapter::isClearcoatEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18isClearcoatEnabledEv',
    )

  def isTransmissionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isTransmissionEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  bool QSSGShaderMaterialAdapter::isTransmissionEnabled()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter21isTransmissionEnabledEv',
    )

  def hasLighting(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::hasLighting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#hasLighting
    """
    #  bool QSSGShaderMaterialAdapter::hasLighting()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter11hasLightingEv',
    )

  def usesCustomSkinning(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::usesCustomSkinning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#usesCustomSkinning
    """
    #  bool QSSGShaderMaterialAdapter::usesCustomSkinning()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18usesCustomSkinningEv',
    )

  def usesCustomMorphing(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::usesCustomMorphing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#usesCustomMorphing
    """
    #  bool QSSGShaderMaterialAdapter::usesCustomMorphing()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18usesCustomMorphingEv',
    )

  def specularModel(self) -> QSSGRenderDefaultMaterial.MaterialSpecularModel:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialSpecularModel
    QSSGShaderMaterialAdapter::specularModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#specularModel

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialSpecularModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialSpecularModel(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialSpecularModel
    #      QSSGShaderMaterialAdapter::specularModel()
    return QSSGRenderDefaultMaterial.MaterialSpecularModel(
        self.uglySide.call(
            'ritual_ZN25QSSGShaderMaterialAdapter13specularModelEv',
        ))

  def alphaMode(self) -> QSSGRenderDefaultMaterial.MaterialAlphaMode:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode
    QSSGShaderMaterialAdapter::alphaMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#alphaMode

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialAlphaMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialAlphaMode(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialAlphaMode
    #      QSSGShaderMaterialAdapter::alphaMode()
    return QSSGRenderDefaultMaterial.MaterialAlphaMode(self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter9alphaModeEv',
    ))

  def vertexColorRedMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderMaterialAdapter::vertexColorRedMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#vertexColorRedMask

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderMaterialAdapter::vertexColorRedMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18vertexColorRedMaskEv',
    ))

  def vertexColorGreenMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderMaterialAdapter::vertexColorGreenMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderMaterialAdapter::vertexColorGreenMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter20vertexColorGreenMaskEv',
    ))

  def vertexColorBlueMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderMaterialAdapter::vertexColorBlueMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#vertexColorBlueMask

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderMaterialAdapter::vertexColorBlueMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter19vertexColorBlueMaskEv',
    ))

  def vertexColorAlphaMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderMaterialAdapter::vertexColorAlphaMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderMaterialAdapter::vertexColorAlphaMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter20vertexColorAlphaMaskEv',
    ))

  def iblProbe(self) -> Optional[QSSGRenderImage]:
    """
    Calls Qt's 'QSSGRenderImage *QSSGShaderMaterialAdapter::iblProbe()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#iblProbe

    Returns
    -------

    Optional[QSSGRenderImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderImage *QSSGShaderMaterialAdapter::iblProbe()
    address = self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter8iblProbeEv',
    )
    from . import QSSGRenderImage
    return QSSGRenderImage._cuteAt(address)

  def emissiveColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderMaterialAdapter::emissiveColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#emissiveColor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderMaterialAdapter::emissiveColor()
    address = self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter13emissiveColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def color(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QSSGShaderMaterialAdapter::color()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#color

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QSSGShaderMaterialAdapter::color()
    address = self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter5colorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def specularTint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderMaterialAdapter::specularTint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#specularTint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderMaterialAdapter::specularTint()
    address = self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter12specularTintEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def ior(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::ior()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#ior
    """
    #  float QSSGShaderMaterialAdapter::ior()
    return self.uglySide.call('ritual_ZN25QSSGShaderMaterialAdapter3iorEv')

  def fresnelScale(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::fresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#fresnelScale
    """
    #  float QSSGShaderMaterialAdapter::fresnelScale()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter12fresnelScaleEv',
    )

  def fresnelBias(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::fresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#fresnelBias
    """
    #  float QSSGShaderMaterialAdapter::fresnelBias()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter11fresnelBiasEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::fresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#fresnelPower
    """
    #  float QSSGShaderMaterialAdapter::fresnelPower()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter12fresnelPowerEv',
    )

  def clearcoatFresnelScale(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatFresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  float QSSGShaderMaterialAdapter::clearcoatFresnelScale()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelScaleEv',
    )

  def clearcoatFresnelBias(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatFresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  float QSSGShaderMaterialAdapter::clearcoatFresnelBias()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter20clearcoatFresnelBiasEv',
    )

  def clearcoatFresnelPower(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatFresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  float QSSGShaderMaterialAdapter::clearcoatFresnelPower()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelPowerEv',
    )

  def metalnessAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::metalnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#metalnessAmount
    """
    #  float QSSGShaderMaterialAdapter::metalnessAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter15metalnessAmountEv',
    )

  def specularAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::specularAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#specularAmount
    """
    #  float QSSGShaderMaterialAdapter::specularAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter14specularAmountEv',
    )

  def specularRoughness(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::specularRoughness()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#specularRoughness
    """
    #  float QSSGShaderMaterialAdapter::specularRoughness()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter17specularRoughnessEv',
    )

  def bumpAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::bumpAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#bumpAmount
    """
    #  float QSSGShaderMaterialAdapter::bumpAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter10bumpAmountEv',
    )

  def translucentFallOff(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::translucentFallOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#translucentFallOff
    """
    #  float QSSGShaderMaterialAdapter::translucentFallOff()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18translucentFallOffEv',
    )

  def diffuseLightWrap(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::diffuseLightWrap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#diffuseLightWrap
    """
    #  float QSSGShaderMaterialAdapter::diffuseLightWrap()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter16diffuseLightWrapEv',
    )

  def occlusionAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::occlusionAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#occlusionAmount
    """
    #  float QSSGShaderMaterialAdapter::occlusionAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter15occlusionAmountEv',
    )

  def alphaCutOff(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::alphaCutOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#alphaCutOff
    """
    #  float QSSGShaderMaterialAdapter::alphaCutOff()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter11alphaCutOffEv',
    )

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::pointSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#pointSize
    """
    #  float QSSGShaderMaterialAdapter::pointSize()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::lineWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#lineWidth
    """
    #  float QSSGShaderMaterialAdapter::lineWidth()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter9lineWidthEv',
    )

  def heightAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::heightAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#heightAmount
    """
    #  float QSSGShaderMaterialAdapter::heightAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter12heightAmountEv',
    )

  def minHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::minHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#minHeightSamples
    """
    #  float QSSGShaderMaterialAdapter::minHeightSamples()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter16minHeightSamplesEv',
    )

  def maxHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::maxHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#maxHeightSamples
    """
    #  float QSSGShaderMaterialAdapter::maxHeightSamples()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter16maxHeightSamplesEv',
    )

  def clearcoatAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#clearcoatAmount
    """
    #  float QSSGShaderMaterialAdapter::clearcoatAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter15clearcoatAmountEv',
    )

  def clearcoatRoughnessAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatRoughnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  float QSSGShaderMaterialAdapter::clearcoatRoughnessAmount()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter24clearcoatRoughnessAmountEv',
    )

  def clearcoatNormalStrength(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::clearcoatNormalStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html
    """
    #  float QSSGShaderMaterialAdapter::clearcoatNormalStrength()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter23clearcoatNormalStrengthEv',
    )

  def transmissionFactor(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::transmissionFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#transmissionFactor
    """
    #  float QSSGShaderMaterialAdapter::transmissionFactor()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter18transmissionFactorEv',
    )

  def thicknessFactor(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::thicknessFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#thicknessFactor
    """
    #  float QSSGShaderMaterialAdapter::thicknessFactor()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter15thicknessFactorEv',
    )

  def attenuationDistance(self) -> float:
    """
    Calls Qt's 'float QSSGShaderMaterialAdapter::attenuationDistance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#attenuationDistance
    """
    #  float QSSGShaderMaterialAdapter::attenuationDistance()
    return self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter19attenuationDistanceEv',
    )

  def attenuationColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderMaterialAdapter::attenuationColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#attenuationColor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderMaterialAdapter::attenuationColor()
    address = self.uglySide.call(
        'ritual_ZN25QSSGShaderMaterialAdapter16attenuationColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isUnshaded(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::isUnshaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#isUnshaded
    """
    #  bool QSSGShaderMaterialAdapter::isUnshaded()
    ritual = 'ritual_ZN25QSSGShaderMaterialAdapter10isUnshadedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSSGShaderMaterialAdapter10isUnshadedEv'
    return self.uglySide.call(ritual)

  @overload(QSSGShaderCache.ShaderType)
  def hasCustomShaderSnippet(self, type: QSSGShaderCache.ShaderType) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderMaterialAdapter::hasCustomShaderSnippet(QSSGShaderCache::
    ShaderType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html

    Parameters
    ----------

    type : QSSGShaderCache.ShaderType
      Passed on as its number.
    """
    #  bool QSSGShaderMaterialAdapter::hasCustomShaderSnippet(
    #      QSSGShaderCache::ShaderType type)
    ritual = (
        'ritual_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippetEN15QS'
        'SGShaderCache10ShaderTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippet'
          'EN15QSSGShaderCache10ShaderTypeE')
    return self.uglySide.call(ritual, type.value)

  def usesSharedVariables(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderMaterialAdapter::usesSharedVariables()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadermaterialadapter.html#usesSharedVariables
    """
    #  bool QSSGShaderMaterialAdapter::usesSharedVariables()
    ritual = 'ritual_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv')
    return self.uglySide.call(ritual)

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderMaterialAdapter *QSSGShaderMaterialAdapter::create(const
    QSSGRenderGraphObject &materialNode)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderMaterialAdapter.create' has no cute function yet. Qt's "
        "'QSSGShaderMaterialAdapter "
        "*QSSGShaderMaterialAdapter::create(const QSSGRenderGraphObject "
        "&materialNode)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def customShaderSnippet(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    QSSGShaderMaterialAdapter::customShaderSnippet(QSSGShaderCache::
    ShaderType type, QSSGShaderLibraryManager &shaderLibraryManager, bool
    multiViewCompatible)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderMaterialAdapter.customShaderSnippet' has no cute "
        "function yet. Qt's 'QByteArray "
        "QSSGShaderMaterialAdapter::customShaderSnippet(QSSGShaderCache::Sha"
        "derType type, QSSGShaderLibraryManager &shaderLibraryManager, bool "
        "multiViewCompatible)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def hasCustomShaderFunction(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGShaderMaterialAdapter::hasCustomShaderFunction(QSSGShaderCache::
    ShaderType shaderType, const QByteArray &funcName,
    QSSGShaderLibraryManager &shaderLibraryManager)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderMaterialAdapter.hasCustomShaderFunction' has no cute "
        "function yet. Qt's 'bool "
        "QSSGShaderMaterialAdapter::hasCustomShaderFunction(QSSGShaderCache:"
        ":ShaderType shaderType, const QByteArray &funcName, "
        "QSSGShaderLibraryManager &shaderLibraryManager)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setCustomPropertyUniforms(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderMaterialAdapter::setCustomPropertyUniforms(char
    *ubufData, QSSGRhiShaderPipeline &shaderPipeline, const
    QSSGRenderContextInterface &context)': names 'char', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QSSGShaderMaterialAdapter.setCustomPropertyUniforms' has no cute "
        "function yet. Qt's 'void "
        "QSSGShaderMaterialAdapter::setCustomPropertyUniforms(char "
        "*ubufData, QSSGRhiShaderPipeline &shaderPipeline, const "
        "QSSGRenderContextInterface &context)': names 'char', which has no "
        "cute class yet.")
