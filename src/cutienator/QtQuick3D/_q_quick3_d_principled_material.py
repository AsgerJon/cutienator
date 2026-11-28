"""
QQuick3DPrincipledMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dprincipledmaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DPrincipledMaterial to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DMaterial, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DSceneManager, QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuick3DTexture = WAIT['QQuick3DTexture']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DPrincipledMaterial(QQuick3DMaterial):
  """
  The cute side of Qt's QQuick3DPrincipledMaterial: a plain Python object
  standing in front of one C++ QQuick3DPrincipledMaterial.

  It is built on the cute 'QQuick3DMaterial', as Qt's
  QQuick3DPrincipledMaterial is built on Qt's QQuick3DMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DPrincipledMaterial that has a ritual and
  that Python can call so far, 218 names in all: 'metaObject', 'tr',
  'lighting', 'blendMode', 'baseColor', 'baseColorMap',
  'baseColorSingleChannelEnabled', 'baseColorChannel',
  'specularSingleChannelEnabled', 'specularChannel',
  'emissiveSingleChannelEnabled', 'emissiveChannel', 'emissiveMap',
  'emissiveFactor', 'specularReflectionMap', 'specularMap', 'specularTint',
  'specularAmount', 'roughness', 'roughnessMap', 'invertOpacityMapValue',
  'opacity', 'opacityMap', 'normalMap', 'metalness', 'metalnessMap',
  'normalStrength', 'occlusionMap', 'occlusionAmount', 'alphaMode',
  'alphaCutoff', 'metalnessChannel', 'roughnessChannel', 'opacityChannel',
  'occlusionChannel', 'pointSize', 'lineWidth', 'heightMap', 'heightChannel',
  'heightAmount', 'minHeightMapSamples', 'maxHeightMapSamples',
  'clearcoatAmount', 'clearcoatMap', 'clearcoatChannel',
  'clearcoatRoughnessAmount', 'clearcoatRoughnessChannel',
  'clearcoatRoughnessMap', 'clearcoatNormalMap', 'clearcoatNormalStrength',
  'transmissionFactor', 'transmissionMap', 'transmissionChannel',
  'thicknessFactor', 'thicknessMap', 'attenuationDistance',
  'attenuationColor', 'indexOfRefraction', 'fresnelScaleBiasEnabled',
  'fresnelScale', 'fresnelBias', 'fresnelPower',
  'clearcoatFresnelScaleBiasEnabled', 'clearcoatFresnelScale',
  'clearcoatFresnelBias', 'clearcoatFresnelPower', 'vertexColorsEnabled',
  'vertexColorsMaskEnabled', 'vertexColorRedMask', 'vertexColorGreenMask',
  'vertexColorBlueMask', 'vertexColorAlphaMask', 'setLighting',
  'setBlendMode', 'setBaseColor', 'setBaseColorMap',
  'setBaseColorSingleChannelEnabled', 'setBaseColorChannel',
  'setSpecularSingleChannelEnabled', 'setSpecularChannel',
  'setEmissiveSingleChannelEnabled', 'setEmissiveChannel', 'setEmissiveMap',
  'setEmissiveFactor', 'setSpecularReflectionMap', 'setSpecularMap',
  'setSpecularTint', 'setSpecularAmount', 'setRoughness', 'setRoughnessMap',
  'setInvertOpacityMapValue', 'setOpacity', 'setOpacityMap', 'setNormalMap',
  'setMetalness', 'setMetalnessMap', 'setNormalStrength', 'setOcclusionMap',
  'setOcclusionAmount', 'setAlphaMode', 'setAlphaCutoff',
  'setMetalnessChannel', 'setRoughnessChannel', 'setOpacityChannel',
  'setOcclusionChannel', 'setPointSize', 'setLineWidth', 'setHeightMap',
  'setHeightChannel', 'setHeightAmount', 'setMinHeightMapSamples',
  'setMaxHeightMapSamples', 'setClearcoatAmount', 'setClearcoatMap',
  'setClearcoatChannel', 'setClearcoatRoughnessAmount',
  'setClearcoatRoughnessChannel', 'setClearcoatRoughnessMap',
  'setClearcoatNormalMap', 'setClearcoatNormalStrength',
  'setTransmissionFactor', 'setTransmissionMap', 'setTransmissionChannel',
  'setThicknessFactor', 'setThicknessMap', 'setAttenuationDistance',
  'setAttenuationColor', 'setIndexOfRefraction',
  'setFresnelScaleBiasEnabled', 'setFresnelScale', 'setFresnelBias',
  'setFresnelPower', 'setClearcoatFresnelScaleBiasEnabled',
  'setClearcoatFresnelScale', 'setClearcoatFresnelBias',
  'setClearcoatFresnelPower', 'setVertexColorsEnabled',
  'setVertexColorsMaskEnabled', 'setVertexColorRedMask',
  'setVertexColorGreenMask', 'setVertexColorBlueMask',
  'setVertexColorAlphaMask', 'lightingChanged', 'blendModeChanged',
  'baseColorChanged', 'baseColorMapChanged',
  'baseColorSingleChannelEnabledChanged', 'baseColorChannelChanged',
  'specularSingleChannelEnabledChanged', 'specularChannelChanged',
  'emissiveSingleChannelEnabledChanged', 'emissiveChannelChanged',
  'emissiveMapChanged', 'emissiveFactorChanged',
  'specularReflectionMapChanged', 'specularMapChanged',
  'specularTintChanged', 'specularAmountChanged', 'roughnessChanged',
  'roughnessMapChanged', 'invertOpacityMapValueChanged', 'opacityChanged',
  'opacityMapChanged', 'normalMapChanged', 'metalnessChanged',
  'metalnessMapChanged', 'normalStrengthChanged', 'occlusionMapChanged',
  'occlusionAmountChanged', 'alphaModeChanged', 'alphaCutoffChanged',
  'metalnessChannelChanged', 'roughnessChannelChanged',
  'opacityChannelChanged', 'occlusionChannelChanged', 'pointSizeChanged',
  'lineWidthChanged', 'heightMapChanged', 'heightChannelChanged',
  'heightAmountChanged', 'minHeightMapSamplesChanged',
  'maxHeightMapSamplesChanged', 'clearcoatAmountChanged',
  'clearcoatMapChanged', 'clearcoatChannelChanged',
  'clearcoatRoughnessAmountChanged', 'clearcoatRoughnessChannelChanged',
  'clearcoatRoughnessMapChanged', 'clearcoatNormalMapChanged',
  'clearcoatNormalStrengthChanged', 'transmissionFactorChanged',
  'transmissionMapChanged', 'transmissionChannelChanged',
  'thicknessFactorChanged', 'thicknessMapChanged', 'thicknessChannelChanged',
  'attenuationDistanceChanged', 'attenuationColorChanged',
  'indexOfRefractionChanged', 'fresnelScaleBiasEnabledChanged',
  'fresnelScaleChanged', 'fresnelBiasChanged', 'fresnelPowerChanged',
  'clearcoatFresnelScaleBiasEnabledChanged', 'clearcoatFresnelScaleChanged',
  'clearcoatFresnelBiasChanged', 'clearcoatFresnelPowerChanged',
  'vertexColorsEnabledChanged', 'vertexColorsMaskEnabledChanged',
  'vertexColorRedMaskChanged', 'vertexColorGreenMaskChanged',
  'vertexColorBlueMaskChanged', 'vertexColorAlphaMaskChanged',
  'updateSpatialNode', 'markAllDirty', 'itemChange', 'updateSceneManager',
  'ensureNormalized'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DPrincipledMaterial::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DPrincipledMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DPrincipledMaterial::~QQuick3DPrincipledMaterial()': the
    destructor: Python never removes a C++ QQuick3DPrincipledMaterial.
  - Qt's 'const TextureChannelMapping
    &QQuick3DPrincipledMaterial::thicknessChannel() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QQuick3DPrincipledMaterial::setThicknessChannel(const
    QQuick3DMaterial::TextureChannelMapping &newThicknessChannel)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQuick3DPrincipledMaterial::markDirty(DirtyType type)': names
    the enum 'QQuick3DPrincipledMaterial::DirtyType', whose class cannot be
    named here.

  What has no ritual
  ------------------

  2 of the 227 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DPrincipledMaterial is created at the first use, not by
    'QQuick3DPrincipledMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DPrincipledMaterial.
  - Qt tells when it has removed the C++ QQuick3DPrincipledMaterial. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DPrincipledMaterial that has no cute function
    yet, 'markDirty', 'setThicknessChannel', 'thicknessChannel', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DPrincipledMaterial, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class AlphaMode(CuteNum):
    """
    The enum 'QQuick3DPrincipledMaterial::AlphaMode' of Qt, with the 4 names
    Qt gives in it.
    """

    Default = Kee[int](0)
    Mask = Kee[int](1)
    Blend = Kee[int](2)
    Opaque = Kee[int](3)

  class BlendMode(CuteNum):
    """
    The enum 'QQuick3DPrincipledMaterial::BlendMode' of Qt, with the 3 names
    Qt gives in it.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class Lighting(CuteNum):
    """
    The enum 'QQuick3DPrincipledMaterial::Lighting' of Qt, with the 2 names
    Qt gives in it.
    """

    NoLighting = Kee[int](0)
    FragmentLighting = Kee[int](1)

  class VertexColorMask(CuteFlags):
    """
    The flags enum 'QQuick3DPrincipledMaterial::VertexColorMask' of Qt, with
    the 12 names Qt gives in it. Qt names the type of its combinations
    'QQuick3DPrincipledMaterial::VertexColorMaskFlags'.
    """

    NoMask = 0x0
    RoughnessMask = 0x1
    NormalStrengthMask = 0x2
    SpecularAmountMask = 0x4
    ClearcoatAmountMask = 0x8
    ClearcoatRoughnessAmountMask = 0x10
    ClearcoatNormalStrengthMask = 0x20
    HeightAmountMask = 0x40
    MetalnessMask = 0x80
    OcclusionAmountMask = 0x100
    ThicknessFactorMask = 0x200
    TransmissionFactorMask = 0x400

  VertexColorMaskFlags = VertexColorMask

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DPrincipledMaterial::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DPrincipledMaterial::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuick3DPrincipledMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(float)
  def ensureNormalized(val: float) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::ensureNormalized(float
    val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#ensureNormalized

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  float QQuick3DPrincipledMaterial::ensureNormalized(float val)
    return Rituals.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16ensureNormalizedEf', val,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPrincipledMaterial'

  #  A C++ QQuick3DPrincipledMaterial Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DPrincipledMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DPrincipledMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DPrincipledMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lighting(self) -> Lighting:
    """
    Calls Qt's 'Lighting QQuick3DPrincipledMaterial::lighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#lighting

    Returns
    -------

    Lighting
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Lighting(number)' gives.
    """
    #  Lighting QQuick3DPrincipledMaterial::lighting() const
    return QQuick3DPrincipledMaterial.Lighting(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial8lightingEv',
    ))

  def blendMode(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DPrincipledMaterial::blendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#blendMode

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DPrincipledMaterial::blendMode() const
    return QQuick3DPrincipledMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9blendModeEv',
    ))

  def baseColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DPrincipledMaterial::baseColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#baseColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DPrincipledMaterial::baseColor() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9baseColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def baseColorMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::baseColorMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#baseColorMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::baseColorMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12baseColorMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def baseColorSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DPrincipledMaterial::baseColorSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::baseColorSingleChannelEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial29baseColorSingleChannelEnab'
        'ledEv',
    )

  def baseColorChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::baseColorChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#baseColorChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::baseColorChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16baseColorChannelEv',
    ))

  def specularSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DPrincipledMaterial::specularSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::specularSingleChannelEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial28specularSingleChannelEnabl'
        'edEv',
    )

  def specularChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::specularChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#specularChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::specularChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15specularChannelEv',
    ))

  def emissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DPrincipledMaterial::emissiveSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::emissiveSingleChannelEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial28emissiveSingleChannelEnabl'
        'edEv',
    )

  def emissiveChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::emissiveChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#emissiveChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::emissiveChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15emissiveChannelEv',
    ))

  def emissiveMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::emissiveMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#emissiveMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::emissiveMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial11emissiveMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def emissiveFactor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DPrincipledMaterial::emissiveFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#emissiveFactor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DPrincipledMaterial::emissiveFactor() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial14emissiveFactorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def specularReflectionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DPrincipledMaterial::specularReflectionMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::specularReflectionMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial21specularReflectionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::specularMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#specularMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::specularMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial11specularMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularTint(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::specularTint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#specularTint
    """
    #  float QQuick3DPrincipledMaterial::specularTint() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12specularTintEv',
    )

  def specularAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::specularAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#specularAmount
    """
    #  float QQuick3DPrincipledMaterial::specularAmount() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial14specularAmountEv',
    )

  def roughness(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::roughness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#roughness
    """
    #  float QQuick3DPrincipledMaterial::roughness() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9roughnessEv',
    )

  def roughnessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::roughnessMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#roughnessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::roughnessMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12roughnessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def invertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DPrincipledMaterial::invertOpacityMapValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::invertOpacityMapValue() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial21invertOpacityMapValueEv',
    )

  def opacity(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#opacity
    """
    #  float QQuick3DPrincipledMaterial::opacity() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial7opacityEv',
    )

  def opacityMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::opacityMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#opacityMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::opacityMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial10opacityMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def normalMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::normalMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#normalMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::normalMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9normalMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def metalness(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::metalness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#metalness
    """
    #  float QQuick3DPrincipledMaterial::metalness() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9metalnessEv',
    )

  def metalnessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::metalnessMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#metalnessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::metalnessMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12metalnessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def normalStrength(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::normalStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#normalStrength
    """
    #  float QQuick3DPrincipledMaterial::normalStrength() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial14normalStrengthEv',
    )

  def occlusionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::occlusionMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#occlusionMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::occlusionMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12occlusionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def occlusionAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::occlusionAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#occlusionAmount
    """
    #  float QQuick3DPrincipledMaterial::occlusionAmount() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15occlusionAmountEv',
    )

  def alphaMode(self) -> AlphaMode:
    """
    Calls Qt's 'AlphaMode QQuick3DPrincipledMaterial::alphaMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#alphaMode

    Returns
    -------

    AlphaMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AlphaMode(number)' gives.
    """
    #  AlphaMode QQuick3DPrincipledMaterial::alphaMode() const
    return QQuick3DPrincipledMaterial.AlphaMode(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9alphaModeEv',
    ))

  def alphaCutoff(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::alphaCutoff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#alphaCutoff
    """
    #  float QQuick3DPrincipledMaterial::alphaCutoff() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial11alphaCutoffEv',
    )

  def metalnessChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::metalnessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#metalnessChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::metalnessChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16metalnessChannelEv',
    ))

  def roughnessChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::roughnessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#roughnessChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::roughnessChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16roughnessChannelEv',
    ))

  def opacityChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::opacityChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#opacityChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::opacityChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial14opacityChannelEv',
    ))

  def occlusionChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::occlusionChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#occlusionChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::occlusionChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16occlusionChannelEv',
    ))

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::pointSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#pointSize
    """
    #  float QQuick3DPrincipledMaterial::pointSize() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::lineWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#lineWidth
    """
    #  float QQuick3DPrincipledMaterial::lineWidth() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9lineWidthEv',
    )

  def heightMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::heightMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#heightMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::heightMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial9heightMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def heightChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::heightChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#heightChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::heightChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial13heightChannelEv',
    ))

  def heightAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::heightAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#heightAmount
    """
    #  float QQuick3DPrincipledMaterial::heightAmount() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12heightAmountEv',
    )

  def minHeightMapSamples(self) -> int:
    """
    Calls Qt's 'int QQuick3DPrincipledMaterial::minHeightMapSamples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  int QQuick3DPrincipledMaterial::minHeightMapSamples() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial19minHeightMapSamplesEv',
    )

  def maxHeightMapSamples(self) -> int:
    """
    Calls Qt's 'int QQuick3DPrincipledMaterial::maxHeightMapSamples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  int QQuick3DPrincipledMaterial::maxHeightMapSamples() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial19maxHeightMapSamplesEv',
    )

  def clearcoatAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#clearcoatAmount
    """
    #  float QQuick3DPrincipledMaterial::clearcoatAmount() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15clearcoatAmountEv',
    )

  def clearcoatMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#clearcoatMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12clearcoatMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def clearcoatChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::clearcoatChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#clearcoatChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DPrincipledMaterial::clearcoatChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16clearcoatChannelEv',
    ))

  def clearcoatRoughnessAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatRoughnessAmount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::clearcoatRoughnessAmount() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial24clearcoatRoughnessAmountEv',
    )

  def clearcoatRoughnessChannel(
      self,
  ) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::clearcoatRoughnessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DPrincipledMaterial::clearcoatRoughnessChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial25clearcoatRoughnessChannelE'
        'v',
    ))

  def clearcoatRoughnessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DPrincipledMaterial::clearcoatRoughnessMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatRoughnessMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatRoughnessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def clearcoatNormalMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DPrincipledMaterial::clearcoatNormalMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#clearcoatNormalMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::clearcoatNormalMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial18clearcoatNormalMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def clearcoatNormalStrength(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatNormalStrength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::clearcoatNormalStrength() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial23clearcoatNormalStrengthEv',
    )

  def transmissionFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::transmissionFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#transmissionFactor
    """
    #  float QQuick3DPrincipledMaterial::transmissionFactor() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial18transmissionFactorEv',
    )

  def transmissionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DPrincipledMaterial::transmissionMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#transmissionMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::transmissionMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15transmissionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def transmissionChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DPrincipledMaterial::transmissionChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DPrincipledMaterial::transmissionChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial19transmissionChannelEv',
    ))

  def thicknessFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::thicknessFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#thicknessFactor
    """
    #  float QQuick3DPrincipledMaterial::thicknessFactor() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial15thicknessFactorEv',
    )

  def thicknessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DPrincipledMaterial::thicknessMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#thicknessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DPrincipledMaterial::thicknessMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12thicknessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def attenuationDistance(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::attenuationDistance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::attenuationDistance() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial19attenuationDistanceEv',
    )

  def attenuationColor(self) -> QColor:
    """
    Calls Qt's 'const QColor &QQuick3DPrincipledMaterial::attenuationColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#attenuationColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QQuick3DPrincipledMaterial::attenuationColor() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial16attenuationColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def indexOfRefraction(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::indexOfRefraction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#indexOfRefraction
    """
    #  float QQuick3DPrincipledMaterial::indexOfRefraction() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial17indexOfRefractionEv',
    )

  def fresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DPrincipledMaterial::fresnelScaleBiasEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::fresnelScaleBiasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial23fresnelScaleBiasEnabledEv',
    )

  def fresnelScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::fresnelScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#fresnelScale
    """
    #  float QQuick3DPrincipledMaterial::fresnelScale() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12fresnelScaleEv',
    )

  def fresnelBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::fresnelBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#fresnelBias
    """
    #  float QQuick3DPrincipledMaterial::fresnelBias() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial11fresnelBiasEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::fresnelPower() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#fresnelPower
    """
    #  float QQuick3DPrincipledMaterial::fresnelPower() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial12fresnelPowerEv',
    )

  def clearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DPrincipledMaterial::clearcoatFresnelScaleBiasEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::clearcoatFresnelScaleBiasEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial32clearcoatFresnelScaleBiasE'
        'nabledEv',
    )

  def clearcoatFresnelScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatFresnelScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::clearcoatFresnelScale() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatFresnelScaleEv',
    )

  def clearcoatFresnelBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatFresnelBias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::clearcoatFresnelBias() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial20clearcoatFresnelBiasEv',
    )

  def clearcoatFresnelPower(self) -> float:
    """
    Calls Qt's 'float QQuick3DPrincipledMaterial::clearcoatFresnelPower()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  float QQuick3DPrincipledMaterial::clearcoatFresnelPower() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial21clearcoatFresnelPowerEv',
    )

  def vertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DPrincipledMaterial::vertexColorsEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::vertexColorsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial19vertexColorsEnabledEv',
    )

  def vertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DPrincipledMaterial::vertexColorsMaskEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  bool QQuick3DPrincipledMaterial::vertexColorsMaskEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DPrincipledMaterial23vertexColorsMaskEnabledEv',
    )

  def vertexColorRedMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DPrincipledMaterial::vertexColorRedMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#vertexColorRedMask

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorRedMask()
    #      const
    return QQuick3DPrincipledMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK26QQuick3DPrincipledMaterial18vertexColorRedMaskEv',
        ))

  def vertexColorGreenMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DPrincipledMaterial::vertexColorGreenMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DPrincipledMaterial::vertexColorGreenMask() const
    return QQuick3DPrincipledMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK26QQuick3DPrincipledMaterial20vertexColorGreenMaskEv',
        ))

  def vertexColorBlueMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DPrincipledMaterial::vertexColorBlueMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags QQuick3DPrincipledMaterial::vertexColorBlueMask()
    #      const
    return QQuick3DPrincipledMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK26QQuick3DPrincipledMaterial19vertexColorBlueMaskEv',
        ))

  def vertexColorAlphaMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DPrincipledMaterial::vertexColorAlphaMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DPrincipledMaterial::vertexColorAlphaMask() const
    return QQuick3DPrincipledMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK26QQuick3DPrincipledMaterial20vertexColorAlphaMaskEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Lighting)
  def setLighting(self, lighting: Lighting) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setLighting(QQuick3DPrincipledMaterial::
    Lighting lighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setLighting

    Parameters
    ----------

    lighting : Lighting
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setLighting(
    #      QQuick3DPrincipledMaterial::Lighting lighting)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial11setLightingENS_8LightingE',
        lighting.value,
    )

  @overload(BlendMode)
  def setBlendMode(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setBlendMode(QQuick3DPrincipledMaterial::
    BlendMode blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setBlendMode

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setBlendMode(
    #      QQuick3DPrincipledMaterial::BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setBlendModeENS_9BlendModeE',
        blendMode.value,
    )

  @overload(QColor)
  def setBaseColor(self, baseColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setBaseColor(QColor
    baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setBaseColor

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::setBaseColor(QColor baseColor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setBaseColorE6QColor',
        self._valueOf(baseColor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setBaseColorMap(self, baseColorMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setBaseColorMap(QQuick3DTexture
    *baseColorMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setBaseColorMap

    Parameters
    ----------

    baseColorMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setBaseColorMap(QQuick3DTexture
    #      *baseColorMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setBaseColorMapEP15QQuick3D'
        'Texture',
        self._addressOf(baseColorMap),
    )

  @overload(bool)
  def setBaseColorSingleChannelEnabled(
      self,
      baseColorSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setBaseColorSingleChannelEnabled(bool
    baseColorSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    baseColorSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setBaseColorSingleChannelEnabled(bool
    #      baseColorSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial32setBaseColorSingleChannelEn'
        'abledEb',
        baseColorSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setBaseColorChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setBaseColorChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setBaseColorChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setBaseColorChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def setSpecularSingleChannelEnabled(
      self,
      specularSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setSpecularSingleChannelEnabled(bool
    specularSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularSingleChannelEnabled(bool
    #      specularSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial31setSpecularSingleChannelEna'
        'bledEb',
        specularSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setSpecularChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setSpecularChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setSpecularChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setSpecularChannelEN16QQuic'
        'k3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def setEmissiveSingleChannelEnabled(
      self,
      emissiveSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setEmissiveSingleChannelEnabled(bool
    emissiveSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    emissiveSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setEmissiveSingleChannelEnabled(bool
    #      emissiveSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial31setEmissiveSingleChannelEna'
        'bledEb',
        emissiveSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setEmissiveChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setEmissiveChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setEmissiveChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setEmissiveChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setEmissiveChannelEN16QQuic'
        'k3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setEmissiveMap(self, emissiveMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setEmissiveMap(QQuick3DTexture
    *emissiveMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setEmissiveMap

    Parameters
    ----------

    emissiveMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setEmissiveMap(QQuick3DTexture
    #      *emissiveMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial14setEmissiveMapEP15QQuick3DT'
        'exture',
        self._addressOf(emissiveMap),
    )

  @overload(QVector3D)
  def setEmissiveFactor(self, emissiveFactor: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setEmissiveFactor(QVector3D
    emissiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setEmissiveFactor

    Parameters
    ----------

    emissiveFactor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::setEmissiveFactor(QVector3D
    #      emissiveFactor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial17setEmissiveFactorE9QVector3'
        'D',
        self._valueOf(emissiveFactor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSpecularReflectionMap(
      self,
      specularReflectionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setSpecularReflectionMap(QQuick3DTexture
    *specularReflectionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularReflectionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularReflectionMap(
    #      QQuick3DTexture *specularReflectionMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24setSpecularReflectionMapEP1'
        '5QQuick3DTexture',
        self._addressOf(specularReflectionMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSpecularMap(self, specularMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setSpecularMap(QQuick3DTexture
    *specularMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setSpecularMap

    Parameters
    ----------

    specularMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularMap(QQuick3DTexture
    #      *specularMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial14setSpecularMapEP15QQuick3DT'
        'exture',
        self._addressOf(specularMap),
    )

  @overload(float)
  def setSpecularTint(self, specularTint: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setSpecularTint(float
    specularTint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setSpecularTint

    Parameters
    ----------

    specularTint : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularTint(float specularTint)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setSpecularTintEf',
        specularTint,
    )

  @overload(float)
  def setSpecularAmount(self, specularAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setSpecularAmount(float
    specularAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setSpecularAmount

    Parameters
    ----------

    specularAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setSpecularAmount(float
    #      specularAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial17setSpecularAmountEf',
        specularAmount,
    )

  @overload(float)
  def setRoughness(self, roughness: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setRoughness(float
    roughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setRoughness

    Parameters
    ----------

    roughness : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setRoughness(float roughness)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setRoughnessEf', roughness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setRoughnessMap(self, roughnessMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setRoughnessMap(QQuick3DTexture
    *roughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setRoughnessMap

    Parameters
    ----------

    roughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setRoughnessMap(QQuick3DTexture
    #      *roughnessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setRoughnessMapEP15QQuick3D'
        'Texture',
        self._addressOf(roughnessMap),
    )

  @overload(bool)
  def setInvertOpacityMapValue(self, invertOpacityMapValue: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setInvertOpacityMapValue(bool
    invertOpacityMapValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    invertOpacityMapValue : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setInvertOpacityMapValue(bool
    #      invertOpacityMapValue)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24setInvertOpacityMapValueEb',
        invertOpacityMapValue,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setOpacity(float opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setOpacity(float opacity)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial10setOpacityEf', opacity,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setOpacityMap(self, opacityMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setOpacityMap(QQuick3DTexture *opacityMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setOpacityMap

    Parameters
    ----------

    opacityMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setOpacityMap(QQuick3DTexture
    #      *opacityMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial13setOpacityMapEP15QQuick3DTe'
        'xture',
        self._addressOf(opacityMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setNormalMap(self, normalMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setNormalMap(QQuick3DTexture
    *normalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setNormalMap

    Parameters
    ----------

    normalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setNormalMap(QQuick3DTexture
    #      *normalMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setNormalMapEP15QQuick3DTex'
        'ture',
        self._addressOf(normalMap),
    )

  @overload(float)
  def setMetalness(self, metalnessAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setMetalness(float
    metalnessAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setMetalness

    Parameters
    ----------

    metalnessAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setMetalness(float metalnessAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setMetalnessEf',
        metalnessAmount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setMetalnessMap(self, metalnessMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setMetalnessMap(QQuick3DTexture
    *metalnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setMetalnessMap

    Parameters
    ----------

    metalnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setMetalnessMap(QQuick3DTexture
    #      *metalnessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setMetalnessMapEP15QQuick3D'
        'Texture',
        self._addressOf(metalnessMap),
    )

  @overload(float)
  def setNormalStrength(self, normalStrength: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setNormalStrength(float
    normalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setNormalStrength

    Parameters
    ----------

    normalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setNormalStrength(float
    #      normalStrength)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial17setNormalStrengthEf',
        normalStrength,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setOcclusionMap(self, occlusionMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setOcclusionMap(QQuick3DTexture
    *occlusionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setOcclusionMap

    Parameters
    ----------

    occlusionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setOcclusionMap(QQuick3DTexture
    #      *occlusionMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setOcclusionMapEP15QQuick3D'
        'Texture',
        self._addressOf(occlusionMap),
    )

  @overload(float)
  def setOcclusionAmount(self, occlusionAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setOcclusionAmount(float
    occlusionAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setOcclusionAmount

    Parameters
    ----------

    occlusionAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setOcclusionAmount(float
    #      occlusionAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setOcclusionAmountEf',
        occlusionAmount,
    )

  @overload(AlphaMode)
  def setAlphaMode(self, alphaMode: AlphaMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setAlphaMode(QQuick3DPrincipledMaterial::
    AlphaMode alphaMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setAlphaMode

    Parameters
    ----------

    alphaMode : AlphaMode
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setAlphaMode(
    #      QQuick3DPrincipledMaterial::AlphaMode alphaMode)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setAlphaModeENS_9AlphaModeE',
        alphaMode.value,
    )

  @overload(float)
  def setAlphaCutoff(self, alphaCutoff: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setAlphaCutoff(float
    alphaCutoff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setAlphaCutoff

    Parameters
    ----------

    alphaCutoff : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setAlphaCutoff(float alphaCutoff)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial14setAlphaCutoffEf',
        alphaCutoff,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setMetalnessChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setMetalnessChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setMetalnessChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setMetalnessChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setRoughnessChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setRoughnessChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setRoughnessChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setRoughnessChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setOpacityChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setOpacityChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setOpacityChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setOpacityChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial17setOpacityChannelEN16QQuick'
        '3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setOcclusionChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setOcclusionChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setOcclusionChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setOcclusionChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def setPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setPointSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setPointSize(float size)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setPointSizeEf', size,
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setLineWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setLineWidth(float width)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setLineWidthEf', width,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setHeightMap(self, heightMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setHeightMap(QQuick3DTexture
    *heightMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setHeightMap

    Parameters
    ----------

    heightMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setHeightMap(QQuick3DTexture
    #      *heightMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial12setHeightMapEP15QQuick3DTex'
        'ture',
        self._addressOf(heightMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setHeightChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setHeightChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setHeightChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setHeightChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16setHeightChannelEN16QQuick3'
        'DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def setHeightAmount(self, heightAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setHeightAmount(float
    heightAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setHeightAmount

    Parameters
    ----------

    heightAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setHeightAmount(float heightAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setHeightAmountEf',
        heightAmount,
    )

  @overload(int)
  def setMinHeightMapSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setMinHeightMapSamples(int
    samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setMinHeightMapSamples(int samples)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setMinHeightMapSamplesEi',
        samples,
    )

  @overload(int)
  def setMaxHeightMapSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setMaxHeightMapSamples(int
    samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setMaxHeightMapSamples(int samples)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setMaxHeightMapSamplesEi',
        samples,
    )

  @overload(float)
  def setClearcoatAmount(self, newClearcoatAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setClearcoatAmount(float
    newClearcoatAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setClearcoatAmount

    Parameters
    ----------

    newClearcoatAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatAmount(float
    #      newClearcoatAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setClearcoatAmountEf',
        newClearcoatAmount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setClearcoatMap(
      self,
      newClearcoatMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatMap(QQuick3DTexture
    *newClearcoatMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setClearcoatMap

    Parameters
    ----------

    newClearcoatMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatMap(QQuick3DTexture
    #      *newClearcoatMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setClearcoatMapEP15QQuick3D'
        'Texture',
        self._addressOf(newClearcoatMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setClearcoatChannel(
      self,
      newClearcoatChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatChannel(QQuick3DMaterial::
    TextureChannelMapping newClearcoatChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newClearcoatChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatChannel(
    #      QQuick3DMaterial::TextureChannelMapping newClearcoatChannel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setClearcoatChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        newClearcoatChannel.value,
    )

  @overload(float)
  def setClearcoatRoughnessAmount(
      self,
      newClearcoatRoughnessAmount: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatRoughnessAmount(float
    newClearcoatRoughnessAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newClearcoatRoughnessAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatRoughnessAmount(float
    #      newClearcoatRoughnessAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial27setClearcoatRoughnessAmount'
        'Ef',
        newClearcoatRoughnessAmount,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setClearcoatRoughnessChannel(
      self,
      newClearcoatRoughnessChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatRoughnessChannel(
    QQuick3DMaterial::TextureChannelMapping newClearcoatRoughnessChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newClearcoatRoughnessChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatRoughnessChannel(
    #      QQuick3DMaterial::TextureChannelMapping
    #      newClearcoatRoughnessChannel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28setClearcoatRoughnessChanne'
        'lEN16QQuick3DMaterial21TextureChannelMappingE',
        newClearcoatRoughnessChannel.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setClearcoatRoughnessMap(
      self,
      newClearcoatRoughnessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatRoughnessMap(QQuick3DTexture
    *newClearcoatRoughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newClearcoatRoughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatRoughnessMap(
    #      QQuick3DTexture *newClearcoatRoughnessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatRoughnessMapEP1'
        '5QQuick3DTexture',
        self._addressOf(newClearcoatRoughnessMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setClearcoatNormalMap(
      self,
      newClearcoatNormalMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatNormalMap(QQuick3DTexture
    *newClearcoatNormalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newClearcoatNormalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatNormalMap(QQuick3DTexture
    #      *newClearcoatNormalMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21setClearcoatNormalMapEP15QQ'
        'uick3DTexture',
        self._addressOf(newClearcoatNormalMap),
    )

  @overload(float)
  def setClearcoatNormalStrength(
      self,
      clearcoatNormalStrength: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatNormalStrength(float
    clearcoatNormalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatNormalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatNormalStrength(float
    #      clearcoatNormalStrength)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26setClearcoatNormalStrengthE'
        'f',
        clearcoatNormalStrength,
    )

  @overload(float)
  def setTransmissionFactor(self, newTransmissionFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setTransmissionFactor(float
    newTransmissionFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newTransmissionFactor : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setTransmissionFactor(float
    #      newTransmissionFactor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21setTransmissionFactorEf',
        newTransmissionFactor,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setTransmissionMap(
      self,
      newTransmissionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setTransmissionMap(QQuick3DTexture
    *newTransmissionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setTransmissionMap

    Parameters
    ----------

    newTransmissionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setTransmissionMap(QQuick3DTexture
    #      *newTransmissionMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setTransmissionMapEP15QQuic'
        'k3DTexture',
        self._addressOf(newTransmissionMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setTransmissionChannel(
      self,
      newTransmissionChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setTransmissionChannel(QQuick3DMaterial::
    TextureChannelMapping newTransmissionChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newTransmissionChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setTransmissionChannel(
    #      QQuick3DMaterial::TextureChannelMapping newTransmissionChannel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setTransmissionChannelEN16Q'
        'Quick3DMaterial21TextureChannelMappingE',
        newTransmissionChannel.value,
    )

  @overload(float)
  def setThicknessFactor(self, newThicknessFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setThicknessFactor(float
    newThicknessFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setThicknessFactor

    Parameters
    ----------

    newThicknessFactor : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setThicknessFactor(float
    #      newThicknessFactor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18setThicknessFactorEf',
        newThicknessFactor,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setThicknessMap(
      self,
      newThicknessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setThicknessMap(QQuick3DTexture
    *newThicknessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setThicknessMap

    Parameters
    ----------

    newThicknessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::setThicknessMap(QQuick3DTexture
    #      *newThicknessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setThicknessMapEP15QQuick3D'
        'Texture',
        self._addressOf(newThicknessMap),
    )

  @overload(float)
  def setAttenuationDistance(self, newAttenuationDistance: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setAttenuationDistance(float
    newAttenuationDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newAttenuationDistance : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setAttenuationDistance(float
    #      newAttenuationDistance)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setAttenuationDistanceEf',
        newAttenuationDistance,
    )

  @overload(QColor)
  def setAttenuationColor(self, newAttenuationColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setAttenuationColor(const
    QColor &newAttenuationColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    newAttenuationColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::setAttenuationColor(const QColor
    #      &newAttenuationColor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19setAttenuationColorERK6QCol'
        'or',
        self._valueOf(newAttenuationColor),
    )

  @overload(float)
  def setIndexOfRefraction(self, indexOfRefraction: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setIndexOfRefraction(float
    indexOfRefraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    indexOfRefraction : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setIndexOfRefraction(float
    #      indexOfRefraction)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial20setIndexOfRefractionEf',
        indexOfRefraction,
    )

  @overload(bool)
  def setFresnelScaleBiasEnabled(self, fresnelScaleBias: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setFresnelScaleBiasEnabled(bool
    fresnelScaleBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    fresnelScaleBias : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setFresnelScaleBiasEnabled(bool
    #      fresnelScaleBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26setFresnelScaleBiasEnabledE'
        'b',
        fresnelScaleBias,
    )

  @overload(float)
  def setFresnelScale(self, fresnelScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setFresnelScale(float
    fresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setFresnelScale

    Parameters
    ----------

    fresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setFresnelScale(float fresnelScale)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setFresnelScaleEf',
        fresnelScale,
    )

  @overload(float)
  def setFresnelBias(self, fresnelBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setFresnelBias(float
    fresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setFresnelBias

    Parameters
    ----------

    fresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setFresnelBias(float fresnelBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial14setFresnelBiasEf',
        fresnelBias,
    )

  @overload(float)
  def setFresnelPower(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setFresnelPower(float
    fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#setFresnelPower

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setFresnelPower(float fresnelPower)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15setFresnelPowerEf',
        fresnelPower,
    )

  @overload(bool)
  def setClearcoatFresnelScaleBiasEnabled(
      self,
      clearcoatFresnelScaleBias: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatFresnelScaleBiasEnabled(bool
    clearcoatFresnelScaleBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelScaleBias : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatFresnelScaleBiasEnabled(
    #      bool clearcoatFresnelScaleBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial35setClearcoatFresnelScaleBia'
        'sEnabledEb',
        clearcoatFresnelScaleBias,
    )

  @overload(float)
  def setClearcoatFresnelScale(self, clearcoatFresnelScale: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatFresnelScale(float
    clearcoatFresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatFresnelScale(float
    #      clearcoatFresnelScale)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatFresnelScaleEf',
        clearcoatFresnelScale,
    )

  @overload(float)
  def setClearcoatFresnelBias(self, clearcoatFresnelBias: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatFresnelBias(float
    clearcoatFresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatFresnelBias(float
    #      clearcoatFresnelBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23setClearcoatFresnelBiasEf',
        clearcoatFresnelBias,
    )

  @overload(float)
  def setClearcoatFresnelPower(self, clearcoatFresnelPower: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setClearcoatFresnelPower(float
    clearcoatFresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setClearcoatFresnelPower(float
    #      clearcoatFresnelPower)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24setClearcoatFresnelPowerEf',
        clearcoatFresnelPower,
    )

  @overload(bool)
  def setVertexColorsEnabled(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::setVertexColorsEnabled(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorsEnabled(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setVertexColorsEnabledEb',
        vertexColorsEnabled,
    )

  @overload(bool)
  def setVertexColorsMaskEnabled(
      self,
      vertexColorsMaskEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setVertexColorsMaskEnabled(bool
    vertexColorsMaskEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorsMaskEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorsMaskEnabled(bool
    #      vertexColorsMaskEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26setVertexColorsMaskEnabledE'
        'b',
        vertexColorsMaskEnabled,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorRedMask(
      self,
      vertexColorRedMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setVertexColorRedMask(VertexColorMaskFlags
    vertexColorRedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorRedMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorRedMask(
    #      VertexColorMaskFlags vertexColorRedMask)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21setVertexColorRedMaskE6QFla'
        'gsINS_15VertexColorMaskEE',
        vertexColorRedMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorGreenMask(
      self,
      vertexColorGreenMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setVertexColorGreenMask(VertexColorMaskFlags
    vertexColorGreenMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorGreenMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorGreenMask(
    #      VertexColorMaskFlags vertexColorGreenMask)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23setVertexColorGreenMaskE6QF'
        'lagsINS_15VertexColorMaskEE',
        vertexColorGreenMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorBlueMask(
      self,
      vertexColorBlueMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setVertexColorBlueMask(VertexColorMaskFlags
    vertexColorBlueMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorBlueMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorBlueMask(
    #      VertexColorMaskFlags vertexColorBlueMask)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22setVertexColorBlueMaskE6QFl'
        'agsINS_15VertexColorMaskEE',
        vertexColorBlueMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorAlphaMask(
      self,
      vertexColorAlphaMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::setVertexColorAlphaMask(VertexColorMaskFlags
    vertexColorAlphaMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorAlphaMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::setVertexColorAlphaMask(
    #      VertexColorMaskFlags vertexColorAlphaMask)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23setVertexColorAlphaMaskE6QF'
        'lagsINS_15VertexColorMaskEE',
        vertexColorAlphaMask.value,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPrincipledMaterial::QQuick3DPrincipledMaterial(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DPrincipledMaterial::QQuick3DPrincipledMaterial(QQuick3DObject
    #      *parent)
    self._noteCreation(QQuick3DPrincipledMaterial, lambda: Rituals.call(
        'ritual_ZN26QQuick3DPrincipledMaterialC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  @overload(Lighting)
  def lightingChanged(self, lighting: Lighting) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::lightingChanged(QQuick3DPrincipledMaterial::
    Lighting lighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#lightingChanged

    Parameters
    ----------

    lighting : Lighting
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::lightingChanged(
    #      QQuick3DPrincipledMaterial::Lighting lighting)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial15lightingChangedENS_8Lightin'
        'gE',
        lighting.value,
    )

  @overload(BlendMode)
  def blendModeChanged(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::blendModeChanged(
    QQuick3DPrincipledMaterial::BlendMode blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#blendModeChanged

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::blendModeChanged(
    #      QQuick3DPrincipledMaterial::BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16blendModeChangedENS_9BlendM'
        'odeE',
        blendMode.value,
    )

  @overload(QColor)
  def baseColorChanged(self, baseColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::baseColorChanged(QColor
    baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#baseColorChanged

    Parameters
    ----------

    baseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::baseColorChanged(QColor baseColor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16baseColorChangedE6QColor',
        self._valueOf(baseColor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def baseColorMapChanged(
      self,
      baseColorMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::baseColorMapChanged(QQuick3DTexture
    *baseColorMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    baseColorMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::baseColorMapChanged(QQuick3DTexture
    #      *baseColorMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19baseColorMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(baseColorMap),
    )

  @overload(bool)
  def baseColorSingleChannelEnabledChanged(
      self,
      baseColorSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::baseColorSingleChannelEnabledChanged(bool
    baseColorSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    baseColorSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::baseColorSingleChannelEnabledChanged(
    #      bool baseColorSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial36baseColorSingleChannelEnabl'
        'edChangedEb',
        baseColorSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def baseColorChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::baseColorChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::baseColorChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23baseColorChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def specularSingleChannelEnabledChanged(
      self,
      specularColorSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::specularSingleChannelEnabledChanged(bool
    specularColorSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularColorSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::specularSingleChannelEnabledChanged(
    #      bool specularColorSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial35specularSingleChannelEnable'
        'dChangedEb',
        specularColorSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def specularChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::specularChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::specularChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22specularChannelChangedEN16Q'
        'Quick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def emissiveSingleChannelEnabledChanged(
      self,
      emissiveColorSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::emissiveSingleChannelEnabledChanged(bool
    emissiveColorSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    emissiveColorSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::emissiveSingleChannelEnabledChanged(
    #      bool emissiveColorSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial35emissiveSingleChannelEnable'
        'dChangedEb',
        emissiveColorSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def emissiveChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::emissiveChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::emissiveChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22emissiveChannelChangedEN16Q'
        'Quick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def emissiveMapChanged(
      self,
      emissiveMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::emissiveMapChanged(QQuick3DTexture
    *emissiveMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#emissiveMapChanged

    Parameters
    ----------

    emissiveMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::emissiveMapChanged(QQuick3DTexture
    #      *emissiveMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18emissiveMapChangedEP15QQuic'
        'k3DTexture',
        self._addressOf(emissiveMap),
    )

  @overload(QVector3D)
  def emissiveFactorChanged(self, emissiveFactor: QVector3D) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::emissiveFactorChanged(QVector3D
    emissiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    emissiveFactor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::emissiveFactorChanged(QVector3D
    #      emissiveFactor)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21emissiveFactorChangedE9QVec'
        'tor3D',
        self._valueOf(emissiveFactor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def specularReflectionMapChanged(
      self,
      specularReflectionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::specularReflectionMapChanged(QQuick3DTexture
    *specularReflectionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularReflectionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::specularReflectionMapChanged(
    #      QQuick3DTexture *specularReflectionMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28specularReflectionMapChange'
        'dEP15QQuick3DTexture',
        self._addressOf(specularReflectionMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def specularMapChanged(
      self,
      specularMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::specularMapChanged(QQuick3DTexture
    *specularMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#specularMapChanged

    Parameters
    ----------

    specularMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::specularMapChanged(QQuick3DTexture
    #      *specularMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18specularMapChangedEP15QQuic'
        'k3DTexture',
        self._addressOf(specularMap),
    )

  @overload(float)
  def specularTintChanged(self, specularTint: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::specularTintChanged(float
    specularTint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularTint : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::specularTintChanged(float
    #      specularTint)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19specularTintChangedEf',
        specularTint,
    )

  @overload(float)
  def specularAmountChanged(self, specularAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::specularAmountChanged(float
    specularAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    specularAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::specularAmountChanged(float
    #      specularAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21specularAmountChangedEf',
        specularAmount,
    )

  @overload(float)
  def roughnessChanged(self, roughness: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::roughnessChanged(float
    roughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#roughnessChanged

    Parameters
    ----------

    roughness : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::roughnessChanged(float roughness)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16roughnessChangedEf',
        roughness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def roughnessMapChanged(
      self,
      roughnessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::roughnessMapChanged(QQuick3DTexture
    *roughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    roughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::roughnessMapChanged(QQuick3DTexture
    #      *roughnessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19roughnessMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(roughnessMap),
    )

  @overload(bool)
  def invertOpacityMapValueChanged(
      self,
      invertOpacityMapValue: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::invertOpacityMapValueChanged(bool
    invertOpacityMapValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    invertOpacityMapValue : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::invertOpacityMapValueChanged(bool
    #      invertOpacityMapValue)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28invertOpacityMapValueChange'
        'dEb',
        invertOpacityMapValue,
    )

  @overload(float)
  def opacityChanged(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::opacityChanged(float
    opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#opacityChanged

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::opacityChanged(float opacity)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial14opacityChangedEf', opacity,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def opacityMapChanged(self, opacityMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::opacityMapChanged(QQuick3DTexture
    *opacityMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#opacityMapChanged

    Parameters
    ----------

    opacityMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::opacityMapChanged(QQuick3DTexture
    #      *opacityMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial17opacityMapChangedEP15QQuick'
        '3DTexture',
        self._addressOf(opacityMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def normalMapChanged(self, normalMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::normalMapChanged(QQuick3DTexture
    *normalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#normalMapChanged

    Parameters
    ----------

    normalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::normalMapChanged(QQuick3DTexture
    #      *normalMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16normalMapChangedEP15QQuick3'
        'DTexture',
        self._addressOf(normalMap),
    )

  @overload(float)
  def metalnessChanged(self, metalness: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::metalnessChanged(float
    metalness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#metalnessChanged

    Parameters
    ----------

    metalness : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::metalnessChanged(float metalness)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16metalnessChangedEf',
        metalness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def metalnessMapChanged(
      self,
      metalnessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::metalnessMapChanged(QQuick3DTexture
    *metalnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    metalnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::metalnessMapChanged(QQuick3DTexture
    #      *metalnessMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19metalnessMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(metalnessMap),
    )

  @overload(float)
  def normalStrengthChanged(self, normalStrength: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::normalStrengthChanged(float
    normalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    normalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::normalStrengthChanged(float
    #      normalStrength)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21normalStrengthChangedEf',
        normalStrength,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def occlusionMapChanged(
      self,
      occlusionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::occlusionMapChanged(QQuick3DTexture
    *occlusionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    occlusionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::occlusionMapChanged(QQuick3DTexture
    #      *occlusionMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19occlusionMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(occlusionMap),
    )

  @overload(float)
  def occlusionAmountChanged(self, occlusionAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::occlusionAmountChanged(float
    occlusionAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    occlusionAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::occlusionAmountChanged(float
    #      occlusionAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22occlusionAmountChangedEf',
        occlusionAmount,
    )

  @overload(AlphaMode)
  def alphaModeChanged(self, alphaMode: AlphaMode) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::alphaModeChanged(
    QQuick3DPrincipledMaterial::AlphaMode alphaMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#alphaModeChanged

    Parameters
    ----------

    alphaMode : AlphaMode
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::alphaModeChanged(
    #      QQuick3DPrincipledMaterial::AlphaMode alphaMode)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16alphaModeChangedENS_9AlphaM'
        'odeE',
        alphaMode.value,
    )

  @overload(float)
  def alphaCutoffChanged(self, alphaCutoff: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::alphaCutoffChanged(float
    alphaCutoff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#alphaCutoffChanged

    Parameters
    ----------

    alphaCutoff : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::alphaCutoffChanged(float alphaCutoff)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18alphaCutoffChangedEf',
        alphaCutoff,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def metalnessChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::metalnessChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::metalnessChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23metalnessChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def roughnessChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::roughnessChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::roughnessChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23roughnessChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def opacityChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::opacityChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::opacityChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial21opacityChannelChangedEN16QQ'
        'uick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def occlusionChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::occlusionChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::occlusionChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23occlusionChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  def pointSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::pointSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#pointSizeChanged
    """
    #  void QQuick3DPrincipledMaterial::pointSizeChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16pointSizeChangedEv',
    )

  def lineWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::lineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#lineWidthChanged
    """
    #  void QQuick3DPrincipledMaterial::lineWidthChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16lineWidthChangedEv',
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def heightMapChanged(self, heightMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::heightMapChanged(QQuick3DTexture
    *heightMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#heightMapChanged

    Parameters
    ----------

    heightMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::heightMapChanged(QQuick3DTexture
    #      *heightMap)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial16heightMapChangedEP15QQuick3'
        'DTexture',
        self._addressOf(heightMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def heightChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::heightChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::heightChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial20heightChannelChangedEN16QQu'
        'ick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def heightAmountChanged(self, heightAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::heightAmountChanged(float
    heightAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    heightAmount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::heightAmountChanged(float
    #      heightAmount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19heightAmountChangedEf',
        heightAmount,
    )

  @overload(int)
  def minHeightMapSamplesChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::minHeightMapSamplesChanged(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::minHeightMapSamplesChanged(int
    #      samples)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26minHeightMapSamplesChangedE'
        'i',
        samples,
    )

  @overload(int)
  def maxHeightMapSamplesChanged(self, samples: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::maxHeightMapSamplesChanged(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::maxHeightMapSamplesChanged(int
    #      samples)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26maxHeightMapSamplesChangedE'
        'i',
        samples,
    )

  @overload(float)
  def clearcoatAmountChanged(self, amount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::clearcoatAmountChanged(float
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    amount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatAmountChanged(float amount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22clearcoatAmountChangedEf',
        amount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def clearcoatMapChanged(self, texture: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatMapChanged(QQuick3DTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatMapChanged(QQuick3DTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19clearcoatMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(texture),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def clearcoatChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23clearcoatChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def clearcoatRoughnessAmountChanged(self, amount: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatRoughnessAmountChanged(float
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    amount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatRoughnessAmountChanged(float
    #      amount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial31clearcoatRoughnessAmountCha'
        'ngedEf',
        amount,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def clearcoatRoughnessChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatRoughnessChannelChanged(
    QQuick3DMaterial::TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatRoughnessChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial32clearcoatRoughnessChannelCh'
        'angedEN16QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def clearcoatRoughnessMapChanged(
      self,
      texture: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatRoughnessMapChanged(QQuick3DTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatRoughnessMapChanged(
    #      QQuick3DTexture *texture)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28clearcoatRoughnessMapChange'
        'dEP15QQuick3DTexture',
        self._addressOf(texture),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def clearcoatNormalMapChanged(
      self,
      texture: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatNormalMapChanged(QQuick3DTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatNormalMapChanged(
    #      QQuick3DTexture *texture)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial25clearcoatNormalMapChangedEP'
        '15QQuick3DTexture',
        self._addressOf(texture),
    )

  @overload(float)
  def clearcoatNormalStrengthChanged(
      self,
      clearcoatNormalStrength: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatNormalStrengthChanged(float
    clearcoatNormalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatNormalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatNormalStrengthChanged(float
    #      clearcoatNormalStrength)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial30clearcoatNormalStrengthChan'
        'gedEf',
        clearcoatNormalStrength,
    )

  @overload(float)
  def transmissionFactorChanged(self, amount: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::transmissionFactorChanged(float amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    amount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::transmissionFactorChanged(float
    #      amount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial25transmissionFactorChangedEf',
        amount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def transmissionMapChanged(
      self,
      texture: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::transmissionMapChanged(QQuick3DTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DPrincipledMaterial::transmissionMapChanged(QQuick3DTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22transmissionMapChangedEP15Q'
        'Quick3DTexture',
        self._addressOf(texture),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def transmissionChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::transmissionChannelChanged(
    QQuick3DMaterial::TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::transmissionChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26transmissionChannelChangedE'
        'N16QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def thicknessFactorChanged(self, amount: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::thicknessFactorChanged(float
    amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    amount : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::thicknessFactorChanged(float amount)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial22thicknessFactorChangedEf',
        amount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def thicknessMapChanged(self, texture: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::thicknessMapChanged(QQuick3DTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    texture : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::thicknessMapChanged(QQuick3DTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19thicknessMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(texture),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def thicknessChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::thicknessChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DPrincipledMaterial::thicknessChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23thicknessChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def attenuationDistanceChanged(self, distance: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::attenuationDistanceChanged(float distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::attenuationDistanceChanged(float
    #      distance)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26attenuationDistanceChangedE'
        'f',
        distance,
    )

  @overload(QColor)
  def attenuationColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::attenuationColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DPrincipledMaterial::attenuationColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial23attenuationColorChangedE6QC'
        'olor',
        self._valueOf(color),
    )

  @overload(float)
  def indexOfRefractionChanged(self, indexOfRefraction: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::indexOfRefractionChanged(float
    indexOfRefraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    indexOfRefraction : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::indexOfRefractionChanged(float
    #      indexOfRefraction)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial24indexOfRefractionChangedEf',
        indexOfRefraction,
    )

  @overload(bool)
  def fresnelScaleBiasEnabledChanged(
      self,
      fresnelScaleBiasEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::fresnelScaleBiasEnabledChanged(bool
    fresnelScaleBiasEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    fresnelScaleBiasEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::fresnelScaleBiasEnabledChanged(bool
    #      fresnelScaleBiasEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial30fresnelScaleBiasEnabledChan'
        'gedEb',
        fresnelScaleBiasEnabled,
    )

  @overload(float)
  def fresnelScaleChanged(self, fresnelScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::fresnelScaleChanged(float
    fresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    fresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::fresnelScaleChanged(float
    #      fresnelScale)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19fresnelScaleChangedEf',
        fresnelScale,
    )

  @overload(float)
  def fresnelBiasChanged(self, fresnelBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::fresnelBiasChanged(float
    fresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#fresnelBiasChanged

    Parameters
    ----------

    fresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::fresnelBiasChanged(float fresnelBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18fresnelBiasChangedEf',
        fresnelBias,
    )

  @overload(float)
  def fresnelPowerChanged(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::fresnelPowerChanged(float
    fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::fresnelPowerChanged(float
    #      fresnelPower)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial19fresnelPowerChangedEf',
        fresnelPower,
    )

  @overload(bool)
  def clearcoatFresnelScaleBiasEnabledChanged(
      self,
      clearcoatFresnelScaleBiasEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatFresnelScaleBiasEnabledChanged(bool
    clearcoatFresnelScaleBiasEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelScaleBiasEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::
    #      clearcoatFresnelScaleBiasEnabledChanged(bool
    #      clearcoatFresnelScaleBiasEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial39clearcoatFresnelScaleBiasEn'
        'abledChangedEb',
        clearcoatFresnelScaleBiasEnabled,
    )

  @overload(float)
  def clearcoatFresnelScaleChanged(
      self,
      clearcoatFresnelScale: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatFresnelScaleChanged(float
    clearcoatFresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatFresnelScaleChanged(float
    #      clearcoatFresnelScale)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28clearcoatFresnelScaleChange'
        'dEf',
        clearcoatFresnelScale,
    )

  @overload(float)
  def clearcoatFresnelBiasChanged(self, clearcoatFresnelBias: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatFresnelBiasChanged(float
    clearcoatFresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatFresnelBiasChanged(float
    #      clearcoatFresnelBias)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial27clearcoatFresnelBiasChanged'
        'Ef',
        clearcoatFresnelBias,
    )

  @overload(float)
  def clearcoatFresnelPowerChanged(
      self,
      clearcoatFresnelPower: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::clearcoatFresnelPowerChanged(float
    clearcoatFresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    clearcoatFresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::clearcoatFresnelPowerChanged(float
    #      clearcoatFresnelPower)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial28clearcoatFresnelPowerChange'
        'dEf',
        clearcoatFresnelPower,
    )

  @overload(bool)
  def vertexColorsEnabledChanged(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorsEnabledChanged(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DPrincipledMaterial::vertexColorsEnabledChanged(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26vertexColorsEnabledChangedE'
        'b',
        vertexColorsEnabled,
    )

  def vertexColorsMaskEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorsMaskEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  void QQuick3DPrincipledMaterial::vertexColorsMaskEnabledChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial30vertexColorsMaskEnabledChan'
        'gedEv',
    )

  def vertexColorRedMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorRedMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  void QQuick3DPrincipledMaterial::vertexColorRedMaskChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial25vertexColorRedMaskChangedEv',
    )

  def vertexColorGreenMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorGreenMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  void QQuick3DPrincipledMaterial::vertexColorGreenMaskChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial27vertexColorGreenMaskChanged'
        'Ev',
    )

  def vertexColorBlueMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorBlueMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  void QQuick3DPrincipledMaterial::vertexColorBlueMaskChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial26vertexColorBlueMaskChangedE'
        'v',
    )

  def vertexColorAlphaMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::vertexColorAlphaMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html
    """
    #  void QQuick3DPrincipledMaterial::vertexColorAlphaMaskChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial27vertexColorAlphaMaskChanged'
        'Ev',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DPrincipledMaterial::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject *QQuick3DPrincipledMaterial::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN26QQuick3DPrincipledMaterial17updateSpatialNodeEP21QSSGRe'
        'nderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuick3DPrincipledMaterial17updateSpatialNodeEP21'
          'QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#markAllDirty
    """
    #  void QQuick3DPrincipledMaterial::markAllDirty()
    ritual = 'ritual_ZN26QQuick3DPrincipledMaterial12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuick3DPrincipledMaterial12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DPrincipledMaterial::itemChange(ItemChange a0,
    const ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DPrincipledMaterial::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN26QQuick3DPrincipledMaterial10itemChangeEN14QQuick3DObjec'
        't10ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuick3DPrincipledMaterial10itemChangeEN14QQuick3'
          'DObject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      window: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPrincipledMaterial::updateSceneManager(QQuick3DSceneManager
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dprincipledmaterial.html#updateSceneManager

    Parameters
    ----------

    window : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DPrincipledMaterial::updateSceneManager(
    #      QQuick3DSceneManager *window)
    self.uglySide.call(
        'ritual_ZN26QQuick3DPrincipledMaterial18updateSceneManagerEP20QQuic'
        'k3DSceneManager',
        self._addressOf(window),
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DPrincipledMaterial::markDirty(DirtyType type)': names
    the enum 'QQuick3DPrincipledMaterial::DirtyType', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQuick3DPrincipledMaterial.markDirty' has no cute function yet. "
        "Qt's 'void QQuick3DPrincipledMaterial::markDirty(DirtyType type)': "
        "names the enum 'QQuick3DPrincipledMaterial::DirtyType', whose "
        "class cannot be named here.")

  @staticmethod
  def setThicknessChannel(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DPrincipledMaterial::setThicknessChannel(const
    QQuick3DMaterial::TextureChannelMapping &newThicknessChannel)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DPrincipledMaterial.setThicknessChannel' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DPrincipledMaterial::setThicknessChannel(const "
        "QQuick3DMaterial::TextureChannelMapping &newThicknessChannel)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def thicknessChannel(*__, **_) -> Never:
    """
    Qt's 'const TextureChannelMapping
    &QQuick3DPrincipledMaterial::thicknessChannel() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DPrincipledMaterial.thicknessChannel' has no cute function "
        "yet. Qt's 'const TextureChannelMapping "
        "&QQuick3DPrincipledMaterial::thicknessChannel() const': gives a "
        "type Python has no way to take yet.")
