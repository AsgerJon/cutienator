"""
QQuick3DSpecularGlossyMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dspecularglossymaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DSpecularGlossyMaterial to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class QQuick3DSpecularGlossyMaterial(QQuick3DMaterial):
  """
  The cute side of Qt's QQuick3DSpecularGlossyMaterial: a plain Python object
  standing in front of one C++ QQuick3DSpecularGlossyMaterial.

  It is built on the cute 'QQuick3DMaterial', as Qt's
  QQuick3DSpecularGlossyMaterial is built on Qt's QQuick3DMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSpecularGlossyMaterial that has a ritual and
  that Python can call so far, 202 names in all: 'metaObject', 'tr',
  'lighting', 'blendMode', 'albedoColor', 'albedoMap',
  'albedoSingleChannelEnabled', 'albedoChannel',
  'specularSingleChannelEnabled', 'specularChannel',
  'emissiveSingleChannelEnabled', 'emissiveChannel', 'emissiveMap',
  'emissiveFactor', 'glossiness', 'glossinessMap', 'invertOpacityMapValue',
  'opacity', 'opacityMap', 'normalMap', 'specularColor', 'specularMap',
  'normalStrength', 'occlusionMap', 'occlusionAmount', 'alphaMode',
  'alphaCutoff', 'glossinessChannel', 'opacityChannel', 'occlusionChannel',
  'pointSize', 'lineWidth', 'heightMap', 'heightChannel', 'heightAmount',
  'minHeightMapSamples', 'maxHeightMapSamples', 'clearcoatAmount',
  'clearcoatMap', 'clearcoatChannel', 'clearcoatRoughnessAmount',
  'clearcoatRoughnessChannel', 'clearcoatRoughnessMap', 'clearcoatNormalMap',
  'transmissionFactor', 'transmissionMap', 'transmissionChannel',
  'thicknessFactor', 'thicknessMap', 'thicknessChannel',
  'attenuationDistance', 'attenuationColor', 'fresnelScaleBiasEnabled',
  'fresnelScale', 'fresnelBias', 'fresnelPower',
  'clearcoatFresnelScaleBiasEnabled', 'clearcoatFresnelScale',
  'clearcoatFresnelBias', 'clearcoatFresnelPower', 'vertexColorsEnabled',
  'clearcoatNormalStrength', 'vertexColorsMaskEnabled', 'vertexColorRedMask',
  'vertexColorGreenMask', 'vertexColorBlueMask', 'vertexColorAlphaMask',
  'setLighting', 'setBlendMode', 'setAlbedoColor', 'setAlbedoMap',
  'setAlbedoSingleChannelEnabled', 'setAlbedoChannel',
  'setSpecularSingleChannelEnabled', 'setSpecularChannel',
  'setEmissiveSingleChannelEnabled', 'setEmissiveChannel', 'setEmissiveMap',
  'setEmissiveFactor', 'setGlossiness', 'setGlossinessMap',
  'setInvertOpacityMapValue', 'setOpacity', 'setOpacityMap', 'setNormalMap',
  'setSpecularColor', 'setSpecularMap', 'setNormalStrength',
  'setOcclusionMap', 'setOcclusionAmount', 'setAlphaMode', 'setAlphaCutoff',
  'setGlossinessChannel', 'setOpacityChannel', 'setOcclusionChannel',
  'setPointSize', 'setLineWidth', 'setHeightMap', 'setHeightChannel',
  'setHeightAmount', 'setMinHeightMapSamples', 'setMaxHeightMapSamples',
  'setClearcoatAmount', 'setClearcoatMap', 'setClearcoatChannel',
  'setClearcoatRoughnessAmount', 'setClearcoatRoughnessChannel',
  'setClearcoatRoughnessMap', 'setClearcoatNormalMap',
  'setClearcoatNormalStrength', 'setTransmissionFactor',
  'setTransmissionMap', 'setTransmissionChannel', 'setThicknessFactor',
  'setThicknessMap', 'setThicknessChannel', 'setAttenuationDistance',
  'setAttenuationColor', 'setFresnelScaleBiasEnabled', 'setFresnelScale',
  'setFresnelBias', 'setFresnelPower', 'setClearcoatFresnelScaleBiasEnabled',
  'setClearcoatFresnelScale', 'setClearcoatFresnelBias',
  'setClearcoatFresnelPower', 'setVertexColorsEnabled',
  'setVertexColorsMaskEnabled', 'setVertexColorRedMask',
  'setVertexColorGreenMask', 'setVertexColorBlueMask',
  'setVertexColorAlphaMask', 'lightingChanged', 'blendModeChanged',
  'albedoColorChanged', 'albedoMapChanged',
  'albedoSingleChannelEnabledChanged', 'albedoChannelChanged',
  'specularSingleChannelEnabledChanged', 'specularChannelChanged',
  'emissiveSingleChannelEnabledChanged', 'emissiveChannelChanged',
  'emissiveMapChanged', 'emissiveFactorChanged', 'glossinessChanged',
  'glossinessMapChanged', 'invertOpacityMapValueChanged', 'opacityChanged',
  'opacityMapChanged', 'normalMapChanged', 'specularColorChanged',
  'specularMapChanged', 'normalStrengthChanged', 'occlusionMapChanged',
  'occlusionAmountChanged', 'alphaModeChanged', 'alphaCutoffChanged',
  'glossinessChannelChanged', 'opacityChannelChanged',
  'occlusionChannelChanged', 'pointSizeChanged', 'lineWidthChanged',
  'heightMapChanged', 'heightChannelChanged', 'heightAmountChanged',
  'minHeightMapSamplesChanged', 'maxHeightMapSamplesChanged',
  'clearcoatAmountChanged', 'clearcoatMapChanged', 'clearcoatChannelChanged',
  'clearcoatRoughnessAmountChanged', 'clearcoatRoughnessChannelChanged',
  'clearcoatRoughnessMapChanged', 'clearcoatNormalMapChanged',
  'clearcoatNormalStrengthChanged', 'transmissionFactorChanged',
  'transmissionMapChanged', 'transmissionChannelChanged',
  'thicknessFactorChanged', 'thicknessMapChanged', 'thicknessChannelChanged',
  'attenuationDistanceChanged', 'attenuationColorChanged',
  'vertexColorsEnabledChanged', 'fresnelScaleBiasEnabledChanged',
  'fresnelScaleChanged', 'fresnelBiasChanged', 'fresnelPowerChanged',
  'clearcoatFresnelScaleBiasEnabledChanged', 'clearcoatFresnelScaleChanged',
  'clearcoatFresnelBiasChanged', 'clearcoatFresnelPowerChanged',
  'vertexColorsMaskEnabledChanged', 'vertexColorRedMaskChanged',
  'vertexColorGreenMaskChanged', 'vertexColorBlueMaskChanged',
  'vertexColorAlphaMaskChanged', 'updateSpatialNode', 'markAllDirty',
  'itemChange', 'updateSceneManager', 'ensureNormalized'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSpecularGlossyMaterial::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuick3DSpecularGlossyMaterial::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSpecularGlossyMaterial::~QQuick3DSpecularGlossyMaterial()':
    the destructor: Python never removes a C++
    QQuick3DSpecularGlossyMaterial.
  - Qt's 'void QQuick3DSpecularGlossyMaterial::markDirty(DirtyType type)':
    names the enum 'QQuick3DSpecularGlossyMaterial::DirtyType', whose class
    cannot be named here.

  What has no ritual
  ------------------

  2 of the 209 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DSpecularGlossyMaterial is created at the first use, not
    by 'QQuick3DSpecularGlossyMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSpecularGlossyMaterial.
  - Qt tells when it has removed the C++ QQuick3DSpecularGlossyMaterial.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSpecularGlossyMaterial that has no cute
    function yet, 'markDirty', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSpecularGlossyMaterial, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class AlphaMode(CuteNum):
    """
    The enum 'QQuick3DSpecularGlossyMaterial::AlphaMode' of Qt, with the 4
    names Qt gives in it.
    """

    Default = Kee[int](0)
    Mask = Kee[int](1)
    Blend = Kee[int](2)
    Opaque = Kee[int](3)

  class BlendMode(CuteNum):
    """
    The enum 'QQuick3DSpecularGlossyMaterial::BlendMode' of Qt, with the 3
    names Qt gives in it.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class Lighting(CuteNum):
    """
    The enum 'QQuick3DSpecularGlossyMaterial::Lighting' of Qt, with the 2
    names Qt gives in it.
    """

    NoLighting = Kee[int](0)
    FragmentLighting = Kee[int](1)

  class VertexColorMask(CuteFlags):
    """
    The flags enum 'QQuick3DSpecularGlossyMaterial::VertexColorMask' of Qt,
    with the 10 names Qt gives in it. Qt names the type of its combinations
    'QQuick3DSpecularGlossyMaterial::VertexColorMaskFlags'.
    """

    NoMask = 0x0
    GlossinessMask = 0x1
    NormalStrengthMask = 0x2
    ClearcoatAmountMask = 0x8
    ClearcoatRoughnessAmountMask = 0x10
    ClearcoatNormalStrengthMask = 0x2
    HeightAmountMask = 0x40
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
    Calls Qt's 'QString QQuick3DSpecularGlossyMaterial::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#tr

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
    #  QString QQuick3DSpecularGlossyMaterial::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(float)
  def ensureNormalized(val: float) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::ensureNormalized(float
    val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  float QQuick3DSpecularGlossyMaterial::ensureNormalized(float val)
    return Rituals.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16ensureNormalizedEf', val,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSpecularGlossyMaterial'

  #  A C++ QQuick3DSpecularGlossyMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSpecularGlossyMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuick3DSpecularGlossyMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSpecularGlossyMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lighting(self) -> Lighting:
    """
    Calls Qt's 'Lighting QQuick3DSpecularGlossyMaterial::lighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#lighting

    Returns
    -------

    Lighting
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Lighting(number)' gives.
    """
    #  Lighting QQuick3DSpecularGlossyMaterial::lighting() const
    return QQuick3DSpecularGlossyMaterial.Lighting(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial8lightingEv',
    ))

  def blendMode(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DSpecularGlossyMaterial::blendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#blendMode

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DSpecularGlossyMaterial::blendMode() const
    return QQuick3DSpecularGlossyMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9blendModeEv',
    ))

  def albedoColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DSpecularGlossyMaterial::albedoColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#albedoColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DSpecularGlossyMaterial::albedoColor() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial11albedoColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def albedoMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSpecularGlossyMaterial::albedoMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#albedoMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::albedoMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9albedoMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def albedoSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial26albedoSingleChannelEna'
        'bledEv',
    )

  def albedoChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::albedoChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#albedoChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DSpecularGlossyMaterial::albedoChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial13albedoChannelEv',
    ))

  def specularSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::specularSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::specularSingleChannelEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial28specularSingleChannelE'
        'nabledEv',
    )

  def specularChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::specularChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::specularChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15specularChannelEv',
    ))

  def emissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::emissiveSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::emissiveSingleChannelEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial28emissiveSingleChannelE'
        'nabledEv',
    )

  def emissiveChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::emissiveChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::emissiveChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15emissiveChannelEv',
    ))

  def emissiveMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::emissiveMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#emissiveMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::emissiveMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial11emissiveMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def emissiveFactor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DSpecularGlossyMaterial::emissiveFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#emissiveFactor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DSpecularGlossyMaterial::emissiveFactor() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial14emissiveFactorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def glossiness(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::glossiness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#glossiness
    """
    #  float QQuick3DSpecularGlossyMaterial::glossiness() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial10glossinessEv',
    )

  def glossinessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::glossinessMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#glossinessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::glossinessMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial13glossinessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def invertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSpecularGlossyMaterial::invertOpacityMapValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::invertOpacityMapValue() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial21invertOpacityMapValueE'
        'v',
    )

  def opacity(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#opacity
    """
    #  float QQuick3DSpecularGlossyMaterial::opacity() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial7opacityEv',
    )

  def opacityMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSpecularGlossyMaterial::opacityMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#opacityMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::opacityMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial10opacityMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def normalMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSpecularGlossyMaterial::normalMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#normalMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::normalMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9normalMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DSpecularGlossyMaterial::specularColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#specularColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DSpecularGlossyMaterial::specularColor() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial13specularColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specularMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::specularMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#specularMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::specularMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial11specularMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def normalStrength(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::normalStrength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#normalStrength
    """
    #  float QQuick3DSpecularGlossyMaterial::normalStrength() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial14normalStrengthEv',
    )

  def occlusionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::occlusionMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#occlusionMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::occlusionMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12occlusionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def occlusionAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::occlusionAmount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::occlusionAmount() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15occlusionAmountEv',
    )

  def alphaMode(self) -> AlphaMode:
    """
    Calls Qt's 'AlphaMode QQuick3DSpecularGlossyMaterial::alphaMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#alphaMode

    Returns
    -------

    AlphaMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AlphaMode(number)' gives.
    """
    #  AlphaMode QQuick3DSpecularGlossyMaterial::alphaMode() const
    return QQuick3DSpecularGlossyMaterial.AlphaMode(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9alphaModeEv',
    ))

  def alphaCutoff(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::alphaCutoff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#alphaCutoff
    """
    #  float QQuick3DSpecularGlossyMaterial::alphaCutoff() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial11alphaCutoffEv',
    )

  def glossinessChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::glossinessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::glossinessChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial17glossinessChannelEv',
    ))

  def opacityChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::opacityChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#opacityChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DSpecularGlossyMaterial::opacityChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial14opacityChannelEv',
    ))

  def occlusionChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::occlusionChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::occlusionChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial16occlusionChannelEv',
    ))

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::pointSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#pointSize
    """
    #  float QQuick3DSpecularGlossyMaterial::pointSize() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::lineWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#lineWidth
    """
    #  float QQuick3DSpecularGlossyMaterial::lineWidth() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9lineWidthEv',
    )

  def heightMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSpecularGlossyMaterial::heightMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#heightMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::heightMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial9heightMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def heightChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::heightChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#heightChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DSpecularGlossyMaterial::heightChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial13heightChannelEv',
    ))

  def heightAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::heightAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#heightAmount
    """
    #  float QQuick3DSpecularGlossyMaterial::heightAmount() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12heightAmountEv',
    )

  def minHeightMapSamples(self) -> int:
    """
    Calls Qt's 'int QQuick3DSpecularGlossyMaterial::minHeightMapSamples()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  int QQuick3DSpecularGlossyMaterial::minHeightMapSamples() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial19minHeightMapSamplesEv',
    )

  def maxHeightMapSamples(self) -> int:
    """
    Calls Qt's 'int QQuick3DSpecularGlossyMaterial::maxHeightMapSamples()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  int QQuick3DSpecularGlossyMaterial::maxHeightMapSamples() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial19maxHeightMapSamplesEv',
    )

  def clearcoatAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::clearcoatAmount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatAmount() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15clearcoatAmountEv',
    )

  def clearcoatMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::clearcoatMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#clearcoatMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::clearcoatMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12clearcoatMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def clearcoatChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::clearcoatChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::clearcoatChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial16clearcoatChannelEv',
    ))

  def clearcoatRoughnessAmount(self) -> float:
    """
    Calls Qt's 'float
    QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmount() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial24clearcoatRoughnessAmou'
        'ntEv',
    )

  def clearcoatRoughnessChannel(
      self,
  ) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial25clearcoatRoughnessChan'
        'nelEv',
    ))

  def clearcoatRoughnessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture
    #      *QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatRoughnessMapE'
        'v',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def clearcoatNormalMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::clearcoatNormalMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::clearcoatNormalMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial18clearcoatNormalMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def transmissionFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::transmissionFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::transmissionFactor() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial18transmissionFactorEv',
    )

  def transmissionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::transmissionMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::transmissionMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15transmissionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def transmissionChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::transmissionChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::transmissionChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial19transmissionChannelEv',
    ))

  def thicknessFactor(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::thicknessFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::thicknessFactor() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial15thicknessFactorEv',
    )

  def thicknessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DSpecularGlossyMaterial::thicknessMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#thicknessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSpecularGlossyMaterial::thicknessMap() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12thicknessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def thicknessChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DSpecularGlossyMaterial::thicknessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping
    #      QQuick3DSpecularGlossyMaterial::thicknessChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial16thicknessChannelEv',
    ))

  def attenuationDistance(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::attenuationDistance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::attenuationDistance() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial19attenuationDistanceEv',
    )

  def attenuationColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DSpecularGlossyMaterial::attenuationColor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DSpecularGlossyMaterial::attenuationColor() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial16attenuationColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial23fresnelScaleBiasEnable'
        'dEv',
    )

  def fresnelScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::fresnelScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#fresnelScale
    """
    #  float QQuick3DSpecularGlossyMaterial::fresnelScale() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12fresnelScaleEv',
    )

  def fresnelBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::fresnelBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#fresnelBias
    """
    #  float QQuick3DSpecularGlossyMaterial::fresnelBias() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial11fresnelBiasEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::fresnelPower() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#fresnelPower
    """
    #  float QQuick3DSpecularGlossyMaterial::fresnelPower() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial12fresnelPowerEv',
    )

  def clearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleBiasEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool
    #      QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleBiasEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial32clearcoatFresnelScaleB'
        'iasEnabledEv',
    )

  def clearcoatFresnelScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::clearcoatFresnelScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelScale() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatFresnelScaleE'
        'v',
    )

  def clearcoatFresnelBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::clearcoatFresnelBias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelBias() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial20clearcoatFresnelBiasEv',
    )

  def clearcoatFresnelPower(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpecularGlossyMaterial::clearcoatFresnelPower()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatFresnelPower() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial21clearcoatFresnelPowerE'
        'v',
    )

  def vertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSpecularGlossyMaterial::vertexColorsEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::vertexColorsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial19vertexColorsEnabledEv',
    )

  def clearcoatNormalStrength(self) -> float:
    """
    Calls Qt's 'float
    QQuick3DSpecularGlossyMaterial::clearcoatNormalStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  float QQuick3DSpecularGlossyMaterial::clearcoatNormalStrength() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial23clearcoatNormalStrengt'
        'hEv',
    )

  def vertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  bool QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabled() const
    return self.uglySide.call(
        'ritual_ZNK30QQuick3DSpecularGlossyMaterial23vertexColorsMaskEnable'
        'dEv',
    )

  def vertexColorRedMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DSpecularGlossyMaterial::vertexColorRedMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DSpecularGlossyMaterial::vertexColorRedMask() const
    return QQuick3DSpecularGlossyMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK30QQuick3DSpecularGlossyMaterial18vertexColorRedMask'
            'Ev',
        ))

  def vertexColorGreenMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DSpecularGlossyMaterial::vertexColorGreenMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DSpecularGlossyMaterial::vertexColorGreenMask() const
    return QQuick3DSpecularGlossyMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK30QQuick3DSpecularGlossyMaterial20vertexColorGreenMa'
            'skEv',
        ))

  def vertexColorBlueMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DSpecularGlossyMaterial::vertexColorBlueMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DSpecularGlossyMaterial::vertexColorBlueMask() const
    return QQuick3DSpecularGlossyMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK30QQuick3DSpecularGlossyMaterial19vertexColorBlueMas'
            'kEv',
        ))

  def vertexColorAlphaMask(self) -> VertexColorMaskFlags:
    """
    Calls Qt's 'VertexColorMaskFlags
    QQuick3DSpecularGlossyMaterial::vertexColorAlphaMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Returns
    -------

    VertexColorMaskFlags
      The value standing for the combination Qt gave back.
    """
    #  VertexColorMaskFlags
    #      QQuick3DSpecularGlossyMaterial::vertexColorAlphaMask() const
    return QQuick3DSpecularGlossyMaterial.VertexColorMaskFlags(
        self.uglySide.call(
            'ritual_ZNK30QQuick3DSpecularGlossyMaterial20vertexColorAlphaMa'
            'skEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Lighting)
  def setLighting(self, lighting: Lighting) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setLighting(
    QQuick3DSpecularGlossyMaterial::Lighting lighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setLighting

    Parameters
    ----------

    lighting : Lighting
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setLighting(
    #      QQuick3DSpecularGlossyMaterial::Lighting lighting)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial11setLightingENS_8Lightin'
        'gE',
        lighting.value,
    )

  @overload(BlendMode)
  def setBlendMode(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setBlendMode(
    QQuick3DSpecularGlossyMaterial::BlendMode blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setBlendMode

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setBlendMode(
    #      QQuick3DSpecularGlossyMaterial::BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setBlendModeENS_9BlendM'
        'odeE',
        blendMode.value,
    )

  @overload(QColor)
  def setAlbedoColor(self, albedo: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setAlbedoColor(const
    QColor &albedo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setAlbedoColor

    Parameters
    ----------

    albedo : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAlbedoColor(const QColor
    #      &albedo)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14setAlbedoColorERK6QColo'
        'r',
        self._valueOf(albedo),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setAlbedoMap(self, albedoMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setAlbedoMap(QQuick3DTexture
    *albedoMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setAlbedoMap

    Parameters
    ----------

    albedoMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAlbedoMap(QQuick3DTexture
    #      *albedoMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setAlbedoMapEP15QQuick3'
        'DTexture',
        self._addressOf(albedoMap),
    )

  @overload(bool)
  def setAlbedoSingleChannelEnabled(
      self,
      albedoSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setAlbedoSingleChannelEnabled(bool
    albedoSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    albedoSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::setAlbedoSingleChannelEnabled(bool
    #      albedoSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial29setAlbedoSingleChannelE'
        'nabledEb',
        albedoSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setAlbedoChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setAlbedoChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAlbedoChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16setAlbedoChannelEN16QQu'
        'ick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def setSpecularSingleChannelEnabled(
      self,
      specularSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setSpecularSingleChannelEnabled(bool
    specularSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    specularSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setSpecularSingleChannelEnabled(
    #      bool specularSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial31setSpecularSingleChanne'
        'lEnabledEb',
        specularSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setSpecularChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setSpecularChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setSpecularChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setSpecularChannelEN16Q'
        'Quick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(bool)
  def setEmissiveSingleChannelEnabled(
      self,
      emissiveSingleChannelEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setEmissiveSingleChannelEnabled(bool
    emissiveSingleChannelEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    emissiveSingleChannelEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setEmissiveSingleChannelEnabled(
    #      bool emissiveSingleChannelEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial31setEmissiveSingleChanne'
        'lEnabledEb',
        emissiveSingleChannelEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setEmissiveChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setEmissiveChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setEmissiveChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setEmissiveChannelEN16Q'
        'Quick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setEmissiveMap(self, emissiveMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setEmissiveMap(QQuick3DTexture
    *emissiveMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setEmissiveMap

    Parameters
    ----------

    emissiveMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setEmissiveMap(QQuick3DTexture
    #      *emissiveMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14setEmissiveMapEP15QQuic'
        'k3DTexture',
        self._addressOf(emissiveMap),
    )

  @overload(QVector3D)
  def setEmissiveFactor(self, emissiveFactor: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setEmissiveFactor(const
    QVector3D &emissiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    emissiveFactor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DSpecularGlossyMaterial::setEmissiveFactor(const QVector3D
    #      &emissiveFactor)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17setEmissiveFactorERK9QV'
        'ector3D',
        self._valueOf(emissiveFactor),
    )

  @overload(float)
  def setGlossiness(self, glossiness: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setGlossiness(float
    glossiness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setGlossiness

    Parameters
    ----------

    glossiness : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setGlossiness(float glossiness)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial13setGlossinessEf',
        glossiness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setGlossinessMap(
      self,
      glossinessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setGlossinessMap(QQuick3DTexture
    *glossinessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    glossinessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setGlossinessMap(QQuick3DTexture
    #      *glossinessMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16setGlossinessMapEP15QQu'
        'ick3DTexture',
        self._addressOf(glossinessMap),
    )

  @overload(bool)
  def setInvertOpacityMapValue(self, invertOpacityMapValue: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setInvertOpacityMapValue(bool
    invertOpacityMapValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    invertOpacityMapValue : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setInvertOpacityMapValue(bool
    #      invertOpacityMapValue)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial24setInvertOpacityMapValu'
        'eEb',
        invertOpacityMapValue,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setOpacity(float
    opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOpacity(float opacity)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial10setOpacityEf', opacity,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setOpacityMap(self, opacityMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setOpacityMap(QQuick3DTexture
    *opacityMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setOpacityMap

    Parameters
    ----------

    opacityMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOpacityMap(QQuick3DTexture
    #      *opacityMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial13setOpacityMapEP15QQuick'
        '3DTexture',
        self._addressOf(opacityMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setNormalMap(self, normalMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setNormalMap(QQuick3DTexture
    *normalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setNormalMap

    Parameters
    ----------

    normalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setNormalMap(QQuick3DTexture
    #      *normalMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setNormalMapEP15QQuick3'
        'DTexture',
        self._addressOf(normalMap),
    )

  @overload(QColor)
  def setSpecularColor(self, specular: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setSpecularColor(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DSpecularGlossyMaterial::setSpecularColor(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16setSpecularColorERK6QCo'
        'lor',
        self._valueOf(specular),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSpecularMap(self, specularMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setSpecularMap(QQuick3DTexture
    *specularMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setSpecularMap

    Parameters
    ----------

    specularMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setSpecularMap(QQuick3DTexture
    #      *specularMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14setSpecularMapEP15QQuic'
        'k3DTexture',
        self._addressOf(specularMap),
    )

  @overload(float)
  def setNormalStrength(self, normalStrength: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setNormalStrength(float
    normalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    normalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setNormalStrength(float
    #      normalStrength)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17setNormalStrengthEf',
        normalStrength,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setOcclusionMap(self, occlusionMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setOcclusionMap(QQuick3DTexture
    *occlusionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    occlusionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOcclusionMap(QQuick3DTexture
    #      *occlusionMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setOcclusionMapEP15QQui'
        'ck3DTexture',
        self._addressOf(occlusionMap),
    )

  @overload(float)
  def setOcclusionAmount(self, occlusionAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setOcclusionAmount(float
    occlusionAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    occlusionAmount : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOcclusionAmount(float
    #      occlusionAmount)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setOcclusionAmountEf',
        occlusionAmount,
    )

  @overload(AlphaMode)
  def setAlphaMode(self, alphaMode: AlphaMode) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setAlphaMode(
    QQuick3DSpecularGlossyMaterial::AlphaMode alphaMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setAlphaMode

    Parameters
    ----------

    alphaMode : AlphaMode
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAlphaMode(
    #      QQuick3DSpecularGlossyMaterial::AlphaMode alphaMode)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setAlphaModeENS_9AlphaM'
        'odeE',
        alphaMode.value,
    )

  @overload(float)
  def setAlphaCutoff(self, alphaCutoff: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setAlphaCutoff(float
    alphaCutoff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setAlphaCutoff

    Parameters
    ----------

    alphaCutoff : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAlphaCutoff(float alphaCutoff)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14setAlphaCutoffEf',
        alphaCutoff,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setGlossinessChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setGlossinessChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setGlossinessChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial20setGlossinessChannelEN1'
        '6QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setOpacityChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setOpacityChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOpacityChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17setOpacityChannelEN16QQ'
        'uick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setOcclusionChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setOcclusionChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setOcclusionChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19setOcclusionChannelEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def setPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setPointSize(float
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setPointSize(float size)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setPointSizeEf', size,
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setLineWidth(float
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setLineWidth(float width)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setLineWidthEf', width,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setHeightMap(self, heightMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setHeightMap(QQuick3DTexture
    *heightMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setHeightMap

    Parameters
    ----------

    heightMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setHeightMap(QQuick3DTexture
    #      *heightMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial12setHeightMapEP15QQuick3'
        'DTexture',
        self._addressOf(heightMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setHeightChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setHeightChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setHeightChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16setHeightChannelEN16QQu'
        'ick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def setHeightAmount(self, heightAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setHeightAmount(float
    heightAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    heightAmount : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setHeightAmount(float
    #      heightAmount)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setHeightAmountEf',
        heightAmount,
    )

  @overload(int)
  def setMinHeightMapSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setMinHeightMapSamples(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setMinHeightMapSamples(int
    #      samples)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setMinHeightMapSamplesE'
        'i',
        samples,
    )

  @overload(int)
  def setMaxHeightMapSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setMaxHeightMapSamples(int samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setMaxHeightMapSamples(int
    #      samples)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setMaxHeightMapSamplesE'
        'i',
        samples,
    )

  @overload(float)
  def setClearcoatAmount(self, newClearcoatAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setClearcoatAmount(float
    newClearcoatAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatAmount : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatAmount(float
    #      newClearcoatAmount)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setClearcoatAmountEf',
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
    QQuick3DSpecularGlossyMaterial::setClearcoatMap(QQuick3DTexture
    *newClearcoatMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatMap(QQuick3DTexture
    #      *newClearcoatMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setClearcoatMapEP15QQui'
        'ck3DTexture',
        self._addressOf(newClearcoatMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setClearcoatChannel(
      self,
      newClearcoatChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatChannel(QQuick3DMaterial::
    TextureChannelMapping newClearcoatChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatChannel(
    #      QQuick3DMaterial::TextureChannelMapping newClearcoatChannel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19setClearcoatChannelEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        newClearcoatChannel.value,
    )

  @overload(float)
  def setClearcoatRoughnessAmount(
      self,
      newClearcoatRoughnessAmount: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessAmount(float
    newClearcoatRoughnessAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatRoughnessAmount : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessAmount(float
    #      newClearcoatRoughnessAmount)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial27setClearcoatRoughnessAm'
        'ountEf',
        newClearcoatRoughnessAmount,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setClearcoatRoughnessChannel(
      self,
      newClearcoatRoughnessChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessChannel(
    QQuick3DMaterial::TextureChannelMapping newClearcoatRoughnessChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatRoughnessChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessChannel(
    #      QQuick3DMaterial::TextureChannelMapping
    #      newClearcoatRoughnessChannel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial28setClearcoatRoughnessCh'
        'annelEN16QQuick3DMaterial21TextureChannelMappingE',
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
    QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessMap(QQuick3DTexture
    *newClearcoatRoughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatRoughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatRoughnessMap(
    #      QQuick3DTexture *newClearcoatRoughnessMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatRoughnessMa'
        'pEP15QQuick3DTexture',
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
    QQuick3DSpecularGlossyMaterial::setClearcoatNormalMap(QQuick3DTexture
    *newClearcoatNormalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatNormalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatNormalMap(
    #      QQuick3DTexture *newClearcoatNormalMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21setClearcoatNormalMapEP'
        '15QQuick3DTexture',
        self._addressOf(newClearcoatNormalMap),
    )

  @overload(float)
  def setClearcoatNormalStrength(
      self,
      newClearcoatNormalStrength: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatNormalStrength(float
    newClearcoatNormalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newClearcoatNormalStrength : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatNormalStrength(float
    #      newClearcoatNormalStrength)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26setClearcoatNormalStren'
        'gthEf',
        newClearcoatNormalStrength,
    )

  @overload(float)
  def setTransmissionFactor(self, newTransmissionFactor: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setTransmissionFactor(float
    newTransmissionFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newTransmissionFactor : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setTransmissionFactor(float
    #      newTransmissionFactor)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21setTransmissionFactorEf',
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
    QQuick3DSpecularGlossyMaterial::setTransmissionMap(QQuick3DTexture
    *newTransmissionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newTransmissionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::setTransmissionMap(QQuick3DTexture
    #      *newTransmissionMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setTransmissionMapEP15Q'
        'Quick3DTexture',
        self._addressOf(newTransmissionMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setTransmissionChannel(
      self,
      newTransmissionChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setTransmissionChannel(
    QQuick3DMaterial::TextureChannelMapping newTransmissionChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newTransmissionChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setTransmissionChannel(
    #      QQuick3DMaterial::TextureChannelMapping newTransmissionChannel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setTransmissionChannelE'
        'N16QQuick3DMaterial21TextureChannelMappingE',
        newTransmissionChannel.value,
    )

  @overload(float)
  def setThicknessFactor(self, newThicknessFactor: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setThicknessFactor(float
    newThicknessFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newThicknessFactor : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setThicknessFactor(float
    #      newThicknessFactor)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18setThicknessFactorEf',
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
    QQuick3DSpecularGlossyMaterial::setThicknessMap(QQuick3DTexture
    *newThicknessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newThicknessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::setThicknessMap(QQuick3DTexture
    #      *newThicknessMap)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setThicknessMapEP15QQui'
        'ck3DTexture',
        self._addressOf(newThicknessMap),
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setThicknessChannel(
      self,
      newThicknessChannel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setThicknessChannel(QQuick3DMaterial::
    TextureChannelMapping newThicknessChannel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newThicknessChannel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setThicknessChannel(
    #      QQuick3DMaterial::TextureChannelMapping newThicknessChannel)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19setThicknessChannelEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        newThicknessChannel.value,
    )

  @overload(float)
  def setAttenuationDistance(self, newAttenuationDistance: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setAttenuationDistance(float
    newAttenuationDistance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newAttenuationDistance : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAttenuationDistance(float
    #      newAttenuationDistance)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setAttenuationDistanceE'
        'f',
        newAttenuationDistance,
    )

  @overload(QColor)
  def setAttenuationColor(self, newAttenuationColor: QColor) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setAttenuationColor(const QColor
    &newAttenuationColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    newAttenuationColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DSpecularGlossyMaterial::setAttenuationColor(const QColor
    #      &newAttenuationColor)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19setAttenuationColorERK6'
        'QColor',
        self._valueOf(newAttenuationColor),
    )

  @overload(bool)
  def setFresnelScaleBiasEnabled(self, fresnelScaleBias: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setFresnelScaleBiasEnabled(bool
    fresnelScaleBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelScaleBias : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setFresnelScaleBiasEnabled(bool
    #      fresnelScaleBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26setFresnelScaleBiasEnab'
        'ledEb',
        fresnelScaleBias,
    )

  @overload(float)
  def setFresnelScale(self, fresnelScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setFresnelScale(float
    fresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setFresnelScale(float
    #      fresnelScale)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setFresnelScaleEf',
        fresnelScale,
    )

  @overload(float)
  def setFresnelBias(self, fresnelBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setFresnelBias(float
    fresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#setFresnelBias

    Parameters
    ----------

    fresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setFresnelBias(float fresnelBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14setFresnelBiasEf',
        fresnelBias,
    )

  @overload(float)
  def setFresnelPower(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setFresnelPower(float
    fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setFresnelPower(float
    #      fresnelPower)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15setFresnelPowerEf',
        fresnelPower,
    )

  @overload(bool)
  def setClearcoatFresnelScaleBiasEnabled(
      self,
      clearcoatFresnelScaleBias: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatFresnelScaleBiasEnabled(bool
    clearcoatFresnelScaleBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelScaleBias : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::
    #      setClearcoatFresnelScaleBiasEnabled(bool
    #      clearcoatFresnelScaleBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial35setClearcoatFresnelScal'
        'eBiasEnabledEb',
        clearcoatFresnelScaleBias,
    )

  @overload(float)
  def setClearcoatFresnelScale(self, clearcoatFresnelScale: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatFresnelScale(float
    clearcoatFresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelScale(float
    #      clearcoatFresnelScale)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatFresnelScal'
        'eEf',
        clearcoatFresnelScale,
    )

  @overload(float)
  def setClearcoatFresnelBias(self, clearcoatFresnelBias: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatFresnelBias(float
    clearcoatFresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelBias(float
    #      clearcoatFresnelBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23setClearcoatFresnelBias'
        'Ef',
        clearcoatFresnelBias,
    )

  @overload(float)
  def setClearcoatFresnelPower(self, clearcoatFresnelPower: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setClearcoatFresnelPower(float
    clearcoatFresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setClearcoatFresnelPower(float
    #      clearcoatFresnelPower)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial24setClearcoatFresnelPowe'
        'rEf',
        clearcoatFresnelPower,
    )

  @overload(bool)
  def setVertexColorsEnabled(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setVertexColorsEnabled(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorsEnabled(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setVertexColorsEnabledE'
        'b',
        vertexColorsEnabled,
    )

  @overload(bool)
  def setVertexColorsMaskEnabled(
      self,
      vertexColorsMaskEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::setVertexColorsMaskEnabled(bool
    vertexColorsMaskEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorsMaskEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorsMaskEnabled(bool
    #      vertexColorsMaskEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26setVertexColorsMaskEnab'
        'ledEb',
        vertexColorsMaskEnabled,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorRedMask(
      self,
      vertexColorRedMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setVertexColorRedMask(
    VertexColorMaskFlags vertexColorRedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorRedMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorRedMask(
    #      VertexColorMaskFlags vertexColorRedMask)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21setVertexColorRedMaskE6'
        'QFlagsINS_15VertexColorMaskEE',
        vertexColorRedMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorGreenMask(
      self,
      vertexColorGreenMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setVertexColorGreenMask(
    VertexColorMaskFlags vertexColorGreenMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorGreenMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorGreenMask(
    #      VertexColorMaskFlags vertexColorGreenMask)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23setVertexColorGreenMask'
        'E6QFlagsINS_15VertexColorMaskEE',
        vertexColorGreenMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorBlueMask(
      self,
      vertexColorBlueMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setVertexColorBlueMask(
    VertexColorMaskFlags vertexColorBlueMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorBlueMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorBlueMask(
    #      VertexColorMaskFlags vertexColorBlueMask)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22setVertexColorBlueMaskE'
        '6QFlagsINS_15VertexColorMaskEE',
        vertexColorBlueMask.value,
    )

  @overload(VertexColorMaskFlags)
  def setVertexColorAlphaMask(
      self,
      vertexColorAlphaMask: VertexColorMaskFlags,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::setVertexColorAlphaMask(
    VertexColorMaskFlags vertexColorAlphaMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorAlphaMask : VertexColorMaskFlags
      Passed on as its number.
    """
    #  void QQuick3DSpecularGlossyMaterial::setVertexColorAlphaMask(
    #      VertexColorMaskFlags vertexColorAlphaMask)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23setVertexColorAlphaMask'
        'E6QFlagsINS_15VertexColorMaskEE',
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
    'QQuick3DSpecularGlossyMaterial::QQuick3DSpecularGlossyMaterial(
    QQuick3DObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DSpecularGlossyMaterial::QQuick3DSpecularGlossyMaterial(
    #      QQuick3DObject *parent)
    self._noteCreation(QQuick3DSpecularGlossyMaterial, lambda: Rituals.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterialC1EP14QQuick3DObject',
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

  def lightingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::lightingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::lightingChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial15lightingChangedEv',
    )

  def blendModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::blendModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::blendModeChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16blendModeChangedEv',
    )

  def albedoColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::albedoColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::albedoColorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18albedoColorChangedEv',
    )

  def albedoMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::albedoMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::albedoMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16albedoMapChangedEv',
    )

  def albedoSingleChannelEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::albedoSingleChannelEnabledChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial33albedoSingleChannelEnab'
        'ledChangedEv',
    )

  def albedoChannelChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::albedoChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::albedoChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial20albedoChannelChangedEv',
    )

  def specularSingleChannelEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::specularSingleChannelEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::
    #      specularSingleChannelEnabledChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial35specularSingleChannelEn'
        'abledChangedEv',
    )

  def specularChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::specularChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::specularChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22specularChannelChangedE'
        'v',
    )

  def emissiveSingleChannelEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::emissiveSingleChannelEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::
    #      emissiveSingleChannelEnabledChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial35emissiveSingleChannelEn'
        'abledChangedEv',
    )

  def emissiveChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::emissiveChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::emissiveChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22emissiveChannelChangedE'
        'v',
    )

  def emissiveMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::emissiveMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::emissiveMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18emissiveMapChangedEv',
    )

  def emissiveFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::emissiveFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::emissiveFactorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21emissiveFactorChangedEv',
    )

  def glossinessChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::glossinessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::glossinessChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17glossinessChangedEv',
    )

  def glossinessMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::glossinessMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::glossinessMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial20glossinessMapChangedEv',
    )

  def invertOpacityMapValueChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::invertOpacityMapValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::invertOpacityMapValueChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial28invertOpacityMapValueCh'
        'angedEv',
    )

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#opacityChanged
    """
    #  void QQuick3DSpecularGlossyMaterial::opacityChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial14opacityChangedEv',
    )

  def opacityMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::opacityMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::opacityMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17opacityMapChangedEv',
    )

  def normalMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::normalMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::normalMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16normalMapChangedEv',
    )

  def specularColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::specularColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::specularColorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial20specularColorChangedEv',
    )

  def specularMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::specularMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::specularMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18specularMapChangedEv',
    )

  def normalStrengthChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::normalStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::normalStrengthChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21normalStrengthChangedEv',
    )

  def occlusionMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::occlusionMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::occlusionMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19occlusionMapChangedEv',
    )

  def occlusionAmountChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::occlusionAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::occlusionAmountChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22occlusionAmountChangedE'
        'v',
    )

  def alphaModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::alphaModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::alphaModeChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16alphaModeChangedEv',
    )

  def alphaCutoffChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::alphaCutoffChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::alphaCutoffChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18alphaCutoffChangedEv',
    )

  def glossinessChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::glossinessChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::glossinessChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial24glossinessChannelChange'
        'dEv',
    )

  def opacityChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::opacityChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::opacityChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial21opacityChannelChangedEv',
    )

  def occlusionChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::occlusionChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::occlusionChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23occlusionChannelChanged'
        'Ev',
    )

  def pointSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::pointSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::pointSizeChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16pointSizeChangedEv',
    )

  def lineWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::lineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::lineWidthChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16lineWidthChangedEv',
    )

  def heightMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::heightMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::heightMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial16heightMapChangedEv',
    )

  def heightChannelChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::heightChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::heightChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial20heightChannelChangedEv',
    )

  def heightAmountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::heightAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::heightAmountChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19heightAmountChangedEv',
    )

  def minHeightMapSamplesChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::minHeightMapSamplesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::minHeightMapSamplesChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26minHeightMapSamplesChan'
        'gedEv',
    )

  def maxHeightMapSamplesChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::maxHeightMapSamplesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::maxHeightMapSamplesChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26maxHeightMapSamplesChan'
        'gedEv',
    )

  def clearcoatAmountChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatAmountChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22clearcoatAmountChangedE'
        'v',
    )

  def clearcoatMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::clearcoatMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19clearcoatMapChangedEv',
    )

  def clearcoatChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23clearcoatChannelChanged'
        'Ev',
    )

  def clearcoatRoughnessAmountChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatRoughnessAmountChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial31clearcoatRoughnessAmoun'
        'tChangedEv',
    )

  def clearcoatRoughnessChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::clearcoatRoughnessChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial32clearcoatRoughnessChann'
        'elChangedEv',
    )

  def clearcoatRoughnessMapChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatRoughnessMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatRoughnessMapCh'
        'angedEv',
    )

  def clearcoatNormalMapChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatNormalMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatNormalMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial25clearcoatNormalMapChang'
        'edEv',
    )

  def clearcoatNormalStrengthChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatNormalStrengthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatNormalStrengthChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial30clearcoatNormalStrength'
        'ChangedEv',
    )

  def transmissionFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::transmissionFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::transmissionFactorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial25transmissionFactorChang'
        'edEv',
    )

  def transmissionMapChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::transmissionMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::transmissionMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22transmissionMapChangedE'
        'v',
    )

  def transmissionChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::transmissionChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::transmissionChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26transmissionChannelChan'
        'gedEv',
    )

  def thicknessFactorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::thicknessFactorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::thicknessFactorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial22thicknessFactorChangedE'
        'v',
    )

  def thicknessMapChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::thicknessMapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::thicknessMapChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19thicknessMapChangedEv',
    )

  def thicknessChannelChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::thicknessChannelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::thicknessChannelChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23thicknessChannelChanged'
        'Ev',
    )

  def attenuationDistanceChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::attenuationDistanceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::attenuationDistanceChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26attenuationDistanceChan'
        'gedEv',
    )

  def attenuationColorChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::attenuationColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::attenuationColorChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial23attenuationColorChanged'
        'Ev',
    )

  @overload(bool)
  def vertexColorsEnabledChanged(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorsEnabledChanged(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorsEnabledChanged(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26vertexColorsEnabledChan'
        'gedEb',
        vertexColorsEnabled,
    )

  @overload(bool)
  def fresnelScaleBiasEnabledChanged(
      self,
      fresnelScaleBiasEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabledChanged(bool
    fresnelScaleBiasEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelScaleBiasEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::fresnelScaleBiasEnabledChanged(
    #      bool fresnelScaleBiasEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial30fresnelScaleBiasEnabled'
        'ChangedEb',
        fresnelScaleBiasEnabled,
    )

  @overload(float)
  def fresnelScaleChanged(self, fresnelScale: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::fresnelScaleChanged(float fresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelScale : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::fresnelScaleChanged(float
    #      fresnelScale)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19fresnelScaleChangedEf',
        fresnelScale,
    )

  @overload(float)
  def fresnelBiasChanged(self, fresnelBias: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::fresnelBiasChanged(float
    fresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::fresnelBiasChanged(float
    #      fresnelBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18fresnelBiasChangedEf',
        fresnelBias,
    )

  @overload(float)
  def fresnelPowerChanged(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::fresnelPowerChanged(float fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::fresnelPowerChanged(float
    #      fresnelPower)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial19fresnelPowerChangedEf',
        fresnelPower,
    )

  @overload(bool)
  def clearcoatFresnelScaleBiasEnabledChanged(
      self,
      clearcoatFresnelScaleBiasEnabled: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleBiasEnabledChanged(
    bool clearcoatFresnelScaleBiasEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelScaleBiasEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::
    #      clearcoatFresnelScaleBiasEnabledChanged(bool
    #      clearcoatFresnelScaleBiasEnabled)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial39clearcoatFresnelScaleBi'
        'asEnabledChangedEb',
        clearcoatFresnelScaleBiasEnabled,
    )

  @overload(float)
  def clearcoatFresnelScaleChanged(
      self,
      clearcoatFresnelScale: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleChanged(float
    clearcoatFresnelScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelScale : float
      Passed on as it is.
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::clearcoatFresnelScaleChanged(float
    #      clearcoatFresnelScale)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatFresnelScaleCh'
        'angedEf',
        clearcoatFresnelScale,
    )

  @overload(float)
  def clearcoatFresnelBiasChanged(self, clearcoatFresnelBias: float) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatFresnelBiasChanged(float
    clearcoatFresnelBias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelBias : float
      Passed on as it is.
    """
    #  void QQuick3DSpecularGlossyMaterial::clearcoatFresnelBiasChanged(float
    #      clearcoatFresnelBias)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial27clearcoatFresnelBiasCha'
        'ngedEf',
        clearcoatFresnelBias,
    )

  @overload(float)
  def clearcoatFresnelPowerChanged(
      self,
      clearcoatFresnelPower: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::clearcoatFresnelPowerChanged(float
    clearcoatFresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    clearcoatFresnelPower : float
      Passed on as it is.
    """
    #  void
    #      QQuick3DSpecularGlossyMaterial::clearcoatFresnelPowerChanged(float
    #      clearcoatFresnelPower)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial28clearcoatFresnelPowerCh'
        'angedEf',
        clearcoatFresnelPower,
    )

  def vertexColorsMaskEnabledChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorsMaskEnabledChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial30vertexColorsMaskEnabled'
        'ChangedEv',
    )

  def vertexColorRedMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorRedMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorRedMaskChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial25vertexColorRedMaskChang'
        'edEv',
    )

  def vertexColorGreenMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorGreenMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorGreenMaskChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial27vertexColorGreenMaskCha'
        'ngedEv',
    )

  def vertexColorBlueMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorBlueMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorBlueMaskChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial26vertexColorBlueMaskChan'
        'gedEv',
    )

  def vertexColorAlphaMaskChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::vertexColorAlphaMaskChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html
    """
    #  void QQuick3DSpecularGlossyMaterial::vertexColorAlphaMaskChanged()
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial27vertexColorAlphaMaskCha'
        'ngedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DSpecularGlossyMaterial::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

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
    #  QSSGRenderGraphObject
    #      *QQuick3DSpecularGlossyMaterial::updateSpatialNode(
    #      QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN30QQuick3DSpecularGlossyMaterial17updateSpatialNodeEP21QS'
        'SGRenderGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DSpecularGlossyMaterial17updateSpatialNode'
          'EP21QSSGRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#markAllDirty
    """
    #  void QQuick3DSpecularGlossyMaterial::markAllDirty()
    ritual = 'ritual_ZN30QQuick3DSpecularGlossyMaterial12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DSpecularGlossyMaterial12markAllDirtyEv')
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSpecularGlossyMaterial::itemChange(ItemChange
    a0, const ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DSpecularGlossyMaterial::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN30QQuick3DSpecularGlossyMaterial10itemChangeEN14QQuick3DO'
        'bject10ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuick3DSpecularGlossyMaterial10itemChangeEN14QQu'
          'ick3DObject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      window: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSpecularGlossyMaterial::updateSceneManager(QQuick3DSceneManager
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspecularglossymaterial.html

    Parameters
    ----------

    window : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSpecularGlossyMaterial::updateSceneManager(
    #      QQuick3DSceneManager *window)
    self.uglySide.call(
        'ritual_ZN30QQuick3DSpecularGlossyMaterial18updateSceneManagerEP20Q'
        'Quick3DSceneManager',
        self._addressOf(window),
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSpecularGlossyMaterial::markDirty(DirtyType type)':
    names the enum 'QQuick3DSpecularGlossyMaterial::DirtyType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DSpecularGlossyMaterial.markDirty' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DSpecularGlossyMaterial::markDirty(DirtyType type)': names "
        "the enum 'QQuick3DSpecularGlossyMaterial::DirtyType', whose class "
        "cannot be named here.")
