"""
QSSGShaderDefaultMaterialAdapter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderDefaultMaterialAdapter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSSGRenderDefaultMaterial, QSSGShaderMaterialAdapter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D, QVector4D
  from . import QSSGRenderImage


class QSSGShaderDefaultMaterialAdapter(QSSGShaderMaterialAdapter):
  """
  The cute side of Qt's QSSGShaderDefaultMaterialAdapter: a plain Python
  object standing in front of one C++ QSSGShaderDefaultMaterialAdapter.

  It is built on the cute 'QSSGShaderMaterialAdapter', as Qt's
  QSSGShaderDefaultMaterialAdapter is built on Qt's
  QSSGShaderMaterialAdapter, and has everything that class has.

  C++ hands a QSSGShaderDefaultMaterialAdapter around as a copy, so every C++
  QSSGShaderDefaultMaterialAdapter behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderDefaultMaterialAdapter that has a ritual
  and that Python can call so far, 54 names in all: 'isPrincipled',
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
  'attenuationColor'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGShaderDefaultMaterialAdapter::QSSGShaderDefaultMaterialAdapter(const
    QSSGRenderDefaultMaterial &material)': takes a type Python has no way to
    hand over yet.
  - Qt's
    'QSSGShaderDefaultMaterialAdapter::~QSSGShaderDefaultMaterialAdapter()':
    the destructor: Python removes its C++ QSSGShaderDefaultMaterialAdapter
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderDefaultMaterialAdapter is created at the first use, not
    by 'QSSGShaderDefaultMaterialAdapter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderDefaultMaterialAdapter back gives a copy
    the ritual made for Python, in a new cute
    QSSGShaderDefaultMaterialAdapter.
  - Each name of Qt's QSSGShaderDefaultMaterialAdapter that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QSSGShaderDefaultMaterialAdapter'

  #  Qt's '~QSSGShaderDefaultMaterialAdapter()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGShaderDefaultMaterialAdapter behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QSSGShaderDefaultMaterialAdapterD1Ev'

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
    'QSSGShaderDefaultMaterialAdapter::QSSGShaderDefaultMaterialAdapter(const
    QSSGRenderDefaultMaterial &material)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderDefaultMaterialAdapter.__init__' has no cute function "
        "yet. Qt's "
        "'QSSGShaderDefaultMaterialAdapter::QSSGShaderDefaultMaterialAdapter"
        "(const QSSGRenderDefaultMaterial &material)': takes a type Python "
        "has no way to hand over yet.")

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
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::isPrincipled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#isPrincipled
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isPrincipled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter12isPrincipledEv',
    )

  def isSpecularGlossy(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::isSpecularGlossy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isSpecularGlossy()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter16isSpecularGlossyEv',
    )

  def isMetalnessEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::isMetalnessEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isMetalnessEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18isMetalnessEnabledEv',
    )

  def isSpecularEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::isSpecularEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isSpecularEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter17isSpecularEnabledEv',
    )

  def isVertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isVertexColorsEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isVertexColorsEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter21isVertexColorsEnabled'
        'Ev',
    )

  def isVertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isVertexColorsMaskEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isVertexColorsMaskEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter25isVertexColorsMaskEna'
        'bledEv',
    )

  def isInvertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isInvertOpacityMapValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isInvertOpacityMapValue()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter23isInvertOpacityMapVal'
        'ueEv',
    )

  def isBaseColorSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isBaseColorSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool
    #      QSSGShaderDefaultMaterialAdapter::isBaseColorSingleChannelEnabled(
    #      )
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter31isBaseColorSingleChan'
        'nelEnabledEv',
    )

  def isSpecularAmountSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isSpecularAmountSingleChannelEnabled(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::
    #      isSpecularAmountSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter36isSpecularAmountSingl'
        'eChannelEnabledEv',
    )

  def isEmissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isEmissiveSingleChannelEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool
    #      QSSGShaderDefaultMaterialAdapter::isEmissiveSingleChannelEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter30isEmissiveSingleChann'
        'elEnabledEv',
    )

  def isClearcoatEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::isClearcoatEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isClearcoatEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18isClearcoatEnabledEv',
    )

  def isTransmissionEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isTransmissionEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isTransmissionEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter21isTransmissionEnabled'
        'Ev',
    )

  def isFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::isFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter25isFresnelScaleBiasEna'
        'bledEv',
    )

  def isClearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGShaderDefaultMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::
    #      isClearcoatFresnelScaleBiasEnabled()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter34isClearcoatFresnelSca'
        'leBiasEnabledEv',
    )

  def hasLighting(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::hasLighting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#hasLighting
    """
    #  bool QSSGShaderDefaultMaterialAdapter::hasLighting()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter11hasLightingEv',
    )

  def usesCustomSkinning(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::usesCustomSkinning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::usesCustomSkinning()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18usesCustomSkinningEv',
    )

  def usesCustomMorphing(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderDefaultMaterialAdapter::usesCustomMorphing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  bool QSSGShaderDefaultMaterialAdapter::usesCustomMorphing()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18usesCustomMorphingEv',
    )

  def specularModel(self) -> QSSGRenderDefaultMaterial.MaterialSpecularModel:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialSpecularModel
    QSSGShaderDefaultMaterialAdapter::specularModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialSpecularModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialSpecularModel(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialSpecularModel
    #      QSSGShaderDefaultMaterialAdapter::specularModel()
    return QSSGRenderDefaultMaterial.MaterialSpecularModel(
        self.uglySide.call(
            'ritual_ZN32QSSGShaderDefaultMaterialAdapter13specularModelEv',
        ))

  def alphaMode(self) -> QSSGRenderDefaultMaterial.MaterialAlphaMode:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::MaterialAlphaMode
    QSSGShaderDefaultMaterialAdapter::alphaMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#alphaMode

    Returns
    -------

    QSSGRenderDefaultMaterial.MaterialAlphaMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderDefaultMaterial.MaterialAlphaMode(number)' gives.
    """
    #  QSSGRenderDefaultMaterial::MaterialAlphaMode
    #      QSSGShaderDefaultMaterialAdapter::alphaMode()
    return QSSGRenderDefaultMaterial.MaterialAlphaMode(self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter9alphaModeEv',
    ))

  def vertexColorRedMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderDefaultMaterialAdapter::vertexColorRedMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderDefaultMaterialAdapter::vertexColorRedMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18vertexColorRedMaskEv',
    ))

  def vertexColorGreenMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderDefaultMaterialAdapter::vertexColorGreenMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderDefaultMaterialAdapter::vertexColorGreenMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter20vertexColorGreenMaskE'
        'v',
    ))

  def vertexColorBlueMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderDefaultMaterialAdapter::vertexColorBlueMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderDefaultMaterialAdapter::vertexColorBlueMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter19vertexColorBlueMaskEv',
    ))

  def vertexColorAlphaMask(
      self,
  ) -> QSSGRenderDefaultMaterial.VertexColorMaskFlags:
    """
    Calls Qt's 'QSSGRenderDefaultMaterial::VertexColorMaskFlags
    QSSGShaderDefaultMaterialAdapter::vertexColorAlphaMask()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QSSGRenderDefaultMaterial.VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  QSSGRenderDefaultMaterial::VertexColorMaskFlags
    #      QSSGShaderDefaultMaterialAdapter::vertexColorAlphaMask()
    return QSSGRenderDefaultMaterial.VertexColorMaskFlags(self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter20vertexColorAlphaMaskE'
        'v',
    ))

  def iblProbe(self) -> Optional[QSSGRenderImage]:
    """
    Calls Qt's 'QSSGRenderImage
    *QSSGShaderDefaultMaterialAdapter::iblProbe()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#iblProbe

    Returns
    -------

    Optional[QSSGRenderImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderImage *QSSGShaderDefaultMaterialAdapter::iblProbe()
    address = self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter8iblProbeEv',
    )
    from . import QSSGRenderImage
    return QSSGRenderImage._cuteAt(address)

  def emissiveColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderDefaultMaterialAdapter::emissiveColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderDefaultMaterialAdapter::emissiveColor()
    address = self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter13emissiveColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def color(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QSSGShaderDefaultMaterialAdapter::color()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#color

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QSSGShaderDefaultMaterialAdapter::color()
    address = self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter5colorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def specularTint(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGShaderDefaultMaterialAdapter::specularTint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#specularTint

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderDefaultMaterialAdapter::specularTint()
    address = self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter12specularTintEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def ior(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::ior()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#ior
    """
    #  float QSSGShaderDefaultMaterialAdapter::ior()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter3iorEv',
    )

  def fresnelScale(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::fresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#fresnelScale
    """
    #  float QSSGShaderDefaultMaterialAdapter::fresnelScale()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter12fresnelScaleEv',
    )

  def fresnelBias(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::fresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#fresnelBias
    """
    #  float QSSGShaderDefaultMaterialAdapter::fresnelBias()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter11fresnelBiasEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::fresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#fresnelPower
    """
    #  float QSSGShaderDefaultMaterialAdapter::fresnelPower()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter12fresnelPowerEv',
    )

  def clearcoatFresnelScale(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::clearcoatFresnelScale()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelScale()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter21clearcoatFresnelScale'
        'Ev',
    )

  def clearcoatFresnelBias(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::clearcoatFresnelBias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelBias()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter20clearcoatFresnelBiasE'
        'v',
    )

  def clearcoatFresnelPower(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::clearcoatFresnelPower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelPower()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter21clearcoatFresnelPower'
        'Ev',
    )

  def metalnessAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::metalnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::metalnessAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter15metalnessAmountEv',
    )

  def specularAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::specularAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::specularAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter14specularAmountEv',
    )

  def specularRoughness(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::specularRoughness()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::specularRoughness()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter17specularRoughnessEv',
    )

  def bumpAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::bumpAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#bumpAmount
    """
    #  float QSSGShaderDefaultMaterialAdapter::bumpAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter10bumpAmountEv',
    )

  def translucentFallOff(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::translucentFallOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::translucentFallOff()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18translucentFallOffEv',
    )

  def diffuseLightWrap(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::diffuseLightWrap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::diffuseLightWrap()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter16diffuseLightWrapEv',
    )

  def occlusionAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::occlusionAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::occlusionAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter15occlusionAmountEv',
    )

  def alphaCutOff(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::alphaCutOff()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#alphaCutOff
    """
    #  float QSSGShaderDefaultMaterialAdapter::alphaCutOff()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter11alphaCutOffEv',
    )

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::pointSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#pointSize
    """
    #  float QSSGShaderDefaultMaterialAdapter::pointSize()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::lineWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#lineWidth
    """
    #  float QSSGShaderDefaultMaterialAdapter::lineWidth()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter9lineWidthEv',
    )

  def heightAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::heightAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html#heightAmount
    """
    #  float QSSGShaderDefaultMaterialAdapter::heightAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter12heightAmountEv',
    )

  def minHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::minHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::minHeightSamples()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter16minHeightSamplesEv',
    )

  def maxHeightSamples(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::maxHeightSamples()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::maxHeightSamples()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter16maxHeightSamplesEv',
    )

  def clearcoatAmount(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::clearcoatAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter15clearcoatAmountEv',
    )

  def clearcoatRoughnessAmount(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::clearcoatRoughnessAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatRoughnessAmount()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter24clearcoatRoughnessAmo'
        'untEv',
    )

  def clearcoatNormalStrength(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::clearcoatNormalStrength()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::clearcoatNormalStrength()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter23clearcoatNormalStreng'
        'thEv',
    )

  def transmissionFactor(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::transmissionFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::transmissionFactor()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter18transmissionFactorEv',
    )

  def thicknessFactor(self) -> float:
    """
    Calls Qt's 'float QSSGShaderDefaultMaterialAdapter::thicknessFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::thicknessFactor()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter15thicknessFactorEv',
    )

  def attenuationDistance(self) -> float:
    """
    Calls Qt's 'float
    QSSGShaderDefaultMaterialAdapter::attenuationDistance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html
    """
    #  float QSSGShaderDefaultMaterialAdapter::attenuationDistance()
    return self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter19attenuationDistanceEv',
    )

  def attenuationColor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QSSGShaderDefaultMaterialAdapter::attenuationColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderdefaultmaterialadapter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGShaderDefaultMaterialAdapter::attenuationColor()
    address = self.uglySide.call(
        'ritual_ZN32QSSGShaderDefaultMaterialAdapter16attenuationColorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)
