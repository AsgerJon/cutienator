"""
QQuick3DDefaultMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddefaultmaterial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DDefaultMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
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


class QQuick3DDefaultMaterial(QQuick3DMaterial):
  """
  The cute side of Qt's QQuick3DDefaultMaterial: a plain Python object
  standing in front of one C++ QQuick3DDefaultMaterial.

  It is built on the cute 'QQuick3DMaterial', as Qt's QQuick3DDefaultMaterial
  is built on Qt's QQuick3DMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DDefaultMaterial that has a ritual and that
  Python can call so far, 93 names in all: 'metaObject', 'tr', 'lighting',
  'blendMode', 'diffuseColor', 'diffuseMap', 'emissiveFactor', 'emissiveMap',
  'specularReflectionMap', 'specularMap', 'specularModel', 'specularTint',
  'indexOfRefraction', 'fresnelPower', 'specularAmount', 'specularRoughness',
  'roughnessMap', 'opacity', 'opacityMap', 'bumpMap', 'bumpAmount',
  'normalMap', 'translucencyMap', 'translucentFalloff', 'diffuseLightWrap',
  'vertexColorsEnabled', 'roughnessChannel', 'opacityChannel',
  'translucencyChannel', 'pointSize', 'lineWidth', 'setLighting',
  'setBlendMode', 'setDiffuseColor', 'setDiffuseMap', 'setEmissiveFactor',
  'setEmissiveMap', 'setSpecularReflectionMap', 'setSpecularMap',
  'setSpecularModel', 'setSpecularTint', 'setIndexOfRefraction',
  'setFresnelPower', 'setSpecularAmount', 'setSpecularRoughness',
  'setRoughnessMap', 'setOpacity', 'setOpacityMap', 'setBumpMap',
  'setBumpAmount', 'setNormalMap', 'setTranslucencyMap',
  'setTranslucentFalloff', 'setDiffuseLightWrap', 'setVertexColorsEnabled',
  'setRoughnessChannel', 'setOpacityChannel', 'setTranslucencyChannel',
  'setPointSize', 'setLineWidth', 'lightingChanged', 'blendModeChanged',
  'diffuseColorChanged', 'diffuseMapChanged', 'emissiveFactorChanged',
  'emissiveMapChanged', 'specularReflectionMapChanged', 'specularMapChanged',
  'specularModelChanged', 'specularTintChanged', 'indexOfRefractionChanged',
  'fresnelPowerChanged', 'specularAmountChanged', 'specularRoughnessChanged',
  'roughnessMapChanged', 'opacityChanged', 'opacityMapChanged',
  'bumpMapChanged', 'bumpAmountChanged', 'normalMapChanged',
  'translucencyMapChanged', 'translucentFalloffChanged',
  'diffuseLightWrapChanged', 'vertexColorsEnabledChanged',
  'roughnessChannelChanged', 'opacityChannelChanged',
  'translucencyChannelChanged', 'pointSizeChanged', 'lineWidthChanged',
  'updateSpatialNode', 'markAllDirty', 'itemChange', 'updateSceneManager'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DDefaultMaterial::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DDefaultMaterial::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DDefaultMaterial::~QQuick3DDefaultMaterial()': the
    destructor: Python never removes a C++ QQuick3DDefaultMaterial.
  - Qt's 'void QQuick3DDefaultMaterial::markDirty(DirtyType type)': names the
    enum 'QQuick3DDefaultMaterial::DirtyType', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 100 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DDefaultMaterial is created at the first use, not by
    'QQuick3DDefaultMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DDefaultMaterial.
  - Qt tells when it has removed the C++ QQuick3DDefaultMaterial. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DDefaultMaterial that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DDefaultMaterial, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BlendMode(CuteNum):
    """
    The enum 'QQuick3DDefaultMaterial::BlendMode' of Qt, with the 3 names Qt
    gives in it.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class Lighting(CuteNum):
    """
    The enum 'QQuick3DDefaultMaterial::Lighting' of Qt, with the 2 names Qt
    gives in it.
    """

    NoLighting = Kee[int](0)
    FragmentLighting = Kee[int](1)

  class SpecularModel(CuteNum):
    """
    The enum 'QQuick3DDefaultMaterial::SpecularModel' of Qt, with the 2 names
    Qt gives in it.
    """

    Default = Kee[int](0)
    KGGX = Kee[int](1)

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
    Calls Qt's 'QString QQuick3DDefaultMaterial::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#tr

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
    #  QString QQuick3DDefaultMaterial::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DDefaultMaterial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DDefaultMaterial'

  #  A C++ QQuick3DDefaultMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DDefaultMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DDefaultMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DDefaultMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lighting(self) -> Lighting:
    """
    Calls Qt's 'Lighting QQuick3DDefaultMaterial::lighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#lighting

    Returns
    -------

    Lighting
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Lighting(number)' gives.
    """
    #  Lighting QQuick3DDefaultMaterial::lighting() const
    return QQuick3DDefaultMaterial.Lighting(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial8lightingEv',
    ))

  def blendMode(self) -> BlendMode:
    """
    Calls Qt's 'BlendMode QQuick3DDefaultMaterial::blendMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#blendMode

    Returns
    -------

    BlendMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BlendMode(number)' gives.
    """
    #  BlendMode QQuick3DDefaultMaterial::blendMode() const
    return QQuick3DDefaultMaterial.BlendMode(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial9blendModeEv',
    ))

  def diffuseColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DDefaultMaterial::diffuseColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#diffuseColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DDefaultMaterial::diffuseColor() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial12diffuseColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuseMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::diffuseMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#diffuseMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::diffuseMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial10diffuseMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def emissiveFactor(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DDefaultMaterial::emissiveFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#emissiveFactor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DDefaultMaterial::emissiveFactor() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial14emissiveFactorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def emissiveMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::emissiveMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#emissiveMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::emissiveMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial11emissiveMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularReflectionMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture
    *QQuick3DDefaultMaterial::specularReflectionMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularReflectionMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::specularReflectionMap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial21specularReflectionMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::specularMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::specularMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial11specularMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def specularModel(self) -> SpecularModel:
    """
    Calls Qt's 'SpecularModel QQuick3DDefaultMaterial::specularModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularModel

    Returns
    -------

    SpecularModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SpecularModel(number)'
      gives.
    """
    #  SpecularModel QQuick3DDefaultMaterial::specularModel() const
    return QQuick3DDefaultMaterial.SpecularModel(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial13specularModelEv',
    ))

  def specularTint(self) -> QColor:
    """
    Calls Qt's 'QColor QQuick3DDefaultMaterial::specularTint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularTint

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuick3DDefaultMaterial::specularTint() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial12specularTintEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def indexOfRefraction(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::indexOfRefraction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#indexOfRefraction
    """
    #  float QQuick3DDefaultMaterial::indexOfRefraction() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial17indexOfRefractionEv',
    )

  def fresnelPower(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::fresnelPower() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#fresnelPower
    """
    #  float QQuick3DDefaultMaterial::fresnelPower() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial12fresnelPowerEv',
    )

  def specularAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::specularAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularAmount
    """
    #  float QQuick3DDefaultMaterial::specularAmount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial14specularAmountEv',
    )

  def specularRoughness(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::specularRoughness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularRoughness
    """
    #  float QQuick3DDefaultMaterial::specularRoughness() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial17specularRoughnessEv',
    )

  def roughnessMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::roughnessMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#roughnessMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::roughnessMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial12roughnessMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def opacity(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::opacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacity
    """
    #  float QQuick3DDefaultMaterial::opacity() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial7opacityEv',
    )

  def opacityMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::opacityMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacityMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::opacityMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial10opacityMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def bumpMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::bumpMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#bumpMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::bumpMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial7bumpMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def bumpAmount(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::bumpAmount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#bumpAmount
    """
    #  float QQuick3DDefaultMaterial::bumpAmount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial10bumpAmountEv',
    )

  def normalMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::normalMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#normalMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::normalMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial9normalMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def translucencyMap(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DDefaultMaterial::translucencyMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#translucencyMap

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DDefaultMaterial::translucencyMap() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial15translucencyMapEv',
    )
    from . import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

  def translucentFalloff(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::translucentFalloff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#translucentFalloff
    """
    #  float QQuick3DDefaultMaterial::translucentFalloff() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial18translucentFalloffEv',
    )

  def diffuseLightWrap(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::diffuseLightWrap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#diffuseLightWrap
    """
    #  float QQuick3DDefaultMaterial::diffuseLightWrap() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial16diffuseLightWrapEv',
    )

  def vertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DDefaultMaterial::vertexColorsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#vertexColorsEnabled
    """
    #  bool QQuick3DDefaultMaterial::vertexColorsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial19vertexColorsEnabledEv',
    )

  def roughnessChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DDefaultMaterial::roughnessChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#roughnessChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DDefaultMaterial::roughnessChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial16roughnessChannelEv',
    ))

  def opacityChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DDefaultMaterial::opacityChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacityChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DDefaultMaterial::opacityChannel() const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial14opacityChannelEv',
    ))

  def translucencyChannel(self) -> QQuick3DMaterial.TextureChannelMapping:
    """
    Calls Qt's 'TextureChannelMapping
    QQuick3DDefaultMaterial::translucencyChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#translucencyChannel

    Returns
    -------

    QQuick3DMaterial.TextureChannelMapping
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DMaterial.TextureChannelMapping(number)' gives.
    """
    #  TextureChannelMapping QQuick3DDefaultMaterial::translucencyChannel()
    #      const
    return QQuick3DMaterial.TextureChannelMapping(self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial19translucencyChannelEv',
    ))

  def pointSize(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::pointSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#pointSize
    """
    #  float QQuick3DDefaultMaterial::pointSize() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial9pointSizeEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QQuick3DDefaultMaterial::lineWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#lineWidth
    """
    #  float QQuick3DDefaultMaterial::lineWidth() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DDefaultMaterial9lineWidthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Lighting)
  def setLighting(self, lighting: Lighting) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setLighting(QQuick3DDefaultMaterial::Lighting
    lighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setLighting

    Parameters
    ----------

    lighting : Lighting
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setLighting(QQuick3DDefaultMaterial::
    #      Lighting lighting)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial11setLightingENS_8LightingE',
        lighting.value,
    )

  @overload(BlendMode)
  def setBlendMode(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setBlendMode(QQuick3DDefaultMaterial::BlendMode
    blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setBlendMode

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setBlendMode(QQuick3DDefaultMaterial::
    #      BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial12setBlendModeENS_9BlendModeE',
        blendMode.value,
    )

  @overload(QColor)
  def setDiffuseColor(self, diffuseColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setDiffuseColor(QColor
    diffuseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setDiffuseColor

    Parameters
    ----------

    diffuseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::setDiffuseColor(QColor diffuseColor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial15setDiffuseColorE6QColor',
        self._valueOf(diffuseColor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setDiffuseMap(self, diffuseMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setDiffuseMap(QQuick3DTexture
    *diffuseMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setDiffuseMap

    Parameters
    ----------

    diffuseMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setDiffuseMap(QQuick3DTexture
    #      *diffuseMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial13setDiffuseMapEP15QQuick3DTextu'
        're',
        self._addressOf(diffuseMap),
    )

  @overload(QVector3D)
  def setEmissiveFactor(self, emissiveFactor: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setEmissiveFactor(QVector3D
    emissiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setEmissiveFactor

    Parameters
    ----------

    emissiveFactor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::setEmissiveFactor(QVector3D
    #      emissiveFactor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17setEmissiveFactorE9QVector3D',
        self._valueOf(emissiveFactor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setEmissiveMap(self, emissiveMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setEmissiveMap(QQuick3DTexture
    *emissiveMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setEmissiveMap

    Parameters
    ----------

    emissiveMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setEmissiveMap(QQuick3DTexture
    #      *emissiveMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial14setEmissiveMapEP15QQuick3DText'
        'ure',
        self._addressOf(emissiveMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSpecularReflectionMap(
      self,
      specularReflectionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setSpecularReflectionMap(QQuick3DTexture
    *specularReflectionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    specularReflectionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setSpecularReflectionMap(QQuick3DTexture
    #      *specularReflectionMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial24setSpecularReflectionMapEP15QQ'
        'uick3DTexture',
        self._addressOf(specularReflectionMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setSpecularMap(self, specularMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setSpecularMap(QQuick3DTexture
    *specularMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setSpecularMap

    Parameters
    ----------

    specularMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setSpecularMap(QQuick3DTexture
    #      *specularMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial14setSpecularMapEP15QQuick3DText'
        'ure',
        self._addressOf(specularMap),
    )

  @overload(SpecularModel)
  def setSpecularModel(self, specularModel: SpecularModel) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setSpecularModel(QQuick3DDefaultMaterial::
    SpecularModel specularModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setSpecularModel

    Parameters
    ----------

    specularModel : SpecularModel
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setSpecularModel(
    #      QQuick3DDefaultMaterial::SpecularModel specularModel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial16setSpecularModelENS_13Specular'
        'ModelE',
        specularModel.value,
    )

  @overload(QColor)
  def setSpecularTint(self, specularTint: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setSpecularTint(QColor
    specularTint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setSpecularTint

    Parameters
    ----------

    specularTint : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::setSpecularTint(QColor specularTint)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial15setSpecularTintE6QColor',
        self._valueOf(specularTint),
    )

  @overload(float)
  def setIndexOfRefraction(self, indexOfRefraction: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setIndexOfRefraction(float
    indexOfRefraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setIndexOfRefraction

    Parameters
    ----------

    indexOfRefraction : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setIndexOfRefraction(float
    #      indexOfRefraction)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial20setIndexOfRefractionEf',
        indexOfRefraction,
    )

  @overload(float)
  def setFresnelPower(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setFresnelPower(float
    fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setFresnelPower

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setFresnelPower(float fresnelPower)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial15setFresnelPowerEf',
        fresnelPower,
    )

  @overload(float)
  def setSpecularAmount(self, specularAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setSpecularAmount(float
    specularAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setSpecularAmount

    Parameters
    ----------

    specularAmount : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setSpecularAmount(float specularAmount)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17setSpecularAmountEf',
        specularAmount,
    )

  @overload(float)
  def setSpecularRoughness(self, specularRoughness: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setSpecularRoughness(float
    specularRoughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setSpecularRoughness

    Parameters
    ----------

    specularRoughness : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setSpecularRoughness(float
    #      specularRoughness)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial20setSpecularRoughnessEf',
        specularRoughness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setRoughnessMap(self, roughnessMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setRoughnessMap(QQuick3DTexture
    *roughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setRoughnessMap

    Parameters
    ----------

    roughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setRoughnessMap(QQuick3DTexture
    #      *roughnessMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial15setRoughnessMapEP15QQuick3DTex'
        'ture',
        self._addressOf(roughnessMap),
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setOpacity(float opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setOpacity(float opacity)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial10setOpacityEf', opacity,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setOpacityMap(self, opacityMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setOpacityMap(QQuick3DTexture
    *opacityMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setOpacityMap

    Parameters
    ----------

    opacityMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setOpacityMap(QQuick3DTexture
    #      *opacityMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial13setOpacityMapEP15QQuick3DTextu'
        're',
        self._addressOf(opacityMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setBumpMap(self, bumpMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setBumpMap(QQuick3DTexture
    *bumpMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setBumpMap

    Parameters
    ----------

    bumpMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setBumpMap(QQuick3DTexture *bumpMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial10setBumpMapEP15QQuick3DTexture',
        self._addressOf(bumpMap),
    )

  @overload(float)
  def setBumpAmount(self, bumpAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setBumpAmount(float
    bumpAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setBumpAmount

    Parameters
    ----------

    bumpAmount : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setBumpAmount(float bumpAmount)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial13setBumpAmountEf', bumpAmount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setNormalMap(self, normalMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setNormalMap(QQuick3DTexture
    *normalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setNormalMap

    Parameters
    ----------

    normalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setNormalMap(QQuick3DTexture *normalMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial12setNormalMapEP15QQuick3DTextur'
        'e',
        self._addressOf(normalMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def setTranslucencyMap(
      self,
      translucencyMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setTranslucencyMap(QQuick3DTexture
    *translucencyMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setTranslucencyMap

    Parameters
    ----------

    translucencyMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::setTranslucencyMap(QQuick3DTexture
    #      *translucencyMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial18setTranslucencyMapEP15QQuick3D'
        'Texture',
        self._addressOf(translucencyMap),
    )

  @overload(float)
  def setTranslucentFalloff(self, translucentFalloff: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setTranslucentFalloff(float
    translucentFalloff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setTranslucentFalloff

    Parameters
    ----------

    translucentFalloff : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setTranslucentFalloff(float
    #      translucentFalloff)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial21setTranslucentFalloffEf',
        translucentFalloff,
    )

  @overload(float)
  def setDiffuseLightWrap(self, diffuseLightWrap: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setDiffuseLightWrap(float
    diffuseLightWrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setDiffuseLightWrap

    Parameters
    ----------

    diffuseLightWrap : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setDiffuseLightWrap(float
    #      diffuseLightWrap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19setDiffuseLightWrapEf',
        diffuseLightWrap,
    )

  @overload(bool)
  def setVertexColorsEnabled(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setVertexColorsEnabled(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setVertexColorsEnabled(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial22setVertexColorsEnabledEb',
        vertexColorsEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setRoughnessChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setRoughnessChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setRoughnessChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setRoughnessChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19setRoughnessChannelEN16QQuick3'
        'DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setOpacityChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setOpacityChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setOpacityChannel

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setOpacityChannel(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17setOpacityChannelEN16QQuick3DM'
        'aterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def setTranslucencyChannel(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::setTranslucencyChannel(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::setTranslucencyChannel(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial22setTranslucencyChannelEN16QQui'
        'ck3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(float)
  def setPointSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setPointSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setPointSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setPointSize(float size)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial12setPointSizeEf', size,
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::setLineWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::setLineWidth(float width)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial12setLineWidthEf', width,
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
    'QQuick3DDefaultMaterial::QQuick3DDefaultMaterial(QQuick3DObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DDefaultMaterial::QQuick3DDefaultMaterial(QQuick3DObject
    #      *parent)
    self._noteCreation(QQuick3DDefaultMaterial, lambda: Rituals.call(
        'ritual_ZN23QQuick3DDefaultMaterialC1EP14QQuick3DObject',
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
    QQuick3DDefaultMaterial::lightingChanged(QQuick3DDefaultMaterial::
    Lighting lighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#lightingChanged

    Parameters
    ----------

    lighting : Lighting
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::lightingChanged(
    #      QQuick3DDefaultMaterial::Lighting lighting)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial15lightingChangedENS_8LightingE',
        lighting.value,
    )

  @overload(BlendMode)
  def blendModeChanged(self, blendMode: BlendMode) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::blendModeChanged(QQuick3DDefaultMaterial::
    BlendMode blendMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#blendModeChanged

    Parameters
    ----------

    blendMode : BlendMode
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::blendModeChanged(
    #      QQuick3DDefaultMaterial::BlendMode blendMode)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial16blendModeChangedENS_9BlendMode'
        'E',
        blendMode.value,
    )

  @overload(QColor)
  def diffuseColorChanged(self, diffuseColor: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::diffuseColorChanged(QColor
    diffuseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#diffuseColorChanged

    Parameters
    ----------

    diffuseColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::diffuseColorChanged(QColor diffuseColor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19diffuseColorChangedE6QColor',
        self._valueOf(diffuseColor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def diffuseMapChanged(self, diffuseMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::diffuseMapChanged(QQuick3DTexture *diffuseMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#diffuseMapChanged

    Parameters
    ----------

    diffuseMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::diffuseMapChanged(QQuick3DTexture
    #      *diffuseMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17diffuseMapChangedEP15QQuick3DT'
        'exture',
        self._addressOf(diffuseMap),
    )

  @overload(QVector3D)
  def emissiveFactorChanged(self, emissiveFactor: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::emissiveFactorChanged(QVector3D
    emissiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#emissiveFactorChanged

    Parameters
    ----------

    emissiveFactor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::emissiveFactorChanged(QVector3D
    #      emissiveFactor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial21emissiveFactorChangedE9QVector'
        '3D',
        self._valueOf(emissiveFactor),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def emissiveMapChanged(
      self,
      emissiveMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::emissiveMapChanged(QQuick3DTexture
    *emissiveMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#emissiveMapChanged

    Parameters
    ----------

    emissiveMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::emissiveMapChanged(QQuick3DTexture
    #      *emissiveMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial18emissiveMapChangedEP15QQuick3D'
        'Texture',
        self._addressOf(emissiveMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def specularReflectionMapChanged(
      self,
      specularReflectionMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::specularReflectionMapChanged(QQuick3DTexture
    *specularReflectionMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    specularReflectionMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::specularReflectionMapChanged(
    #      QQuick3DTexture *specularReflectionMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial28specularReflectionMapChangedEP'
        '15QQuick3DTexture',
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
    QQuick3DDefaultMaterial::specularMapChanged(QQuick3DTexture
    *specularMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularMapChanged

    Parameters
    ----------

    specularMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::specularMapChanged(QQuick3DTexture
    #      *specularMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial18specularMapChangedEP15QQuick3D'
        'Texture',
        self._addressOf(specularMap),
    )

  @overload(SpecularModel)
  def specularModelChanged(self, specularModel: SpecularModel) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::specularModelChanged(QQuick3DDefaultMaterial::
    SpecularModel specularModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularModelChanged

    Parameters
    ----------

    specularModel : SpecularModel
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::specularModelChanged(
    #      QQuick3DDefaultMaterial::SpecularModel specularModel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial20specularModelChangedENS_13Spec'
        'ularModelE',
        specularModel.value,
    )

  @overload(QColor)
  def specularTintChanged(self, specularTint: QColor) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::specularTintChanged(QColor
    specularTint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularTintChanged

    Parameters
    ----------

    specularTint : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuick3DDefaultMaterial::specularTintChanged(QColor specularTint)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19specularTintChangedE6QColor',
        self._valueOf(specularTint),
    )

  @overload(float)
  def indexOfRefractionChanged(self, indexOfRefraction: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::indexOfRefractionChanged(float
    indexOfRefraction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    indexOfRefraction : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::indexOfRefractionChanged(float
    #      indexOfRefraction)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial24indexOfRefractionChangedEf',
        indexOfRefraction,
    )

  @overload(float)
  def fresnelPowerChanged(self, fresnelPower: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::fresnelPowerChanged(float
    fresnelPower)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#fresnelPowerChanged

    Parameters
    ----------

    fresnelPower : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::fresnelPowerChanged(float fresnelPower)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19fresnelPowerChangedEf',
        fresnelPower,
    )

  @overload(float)
  def specularAmountChanged(self, specularAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::specularAmountChanged(float
    specularAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#specularAmountChanged

    Parameters
    ----------

    specularAmount : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::specularAmountChanged(float
    #      specularAmount)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial21specularAmountChangedEf',
        specularAmount,
    )

  @overload(float)
  def specularRoughnessChanged(self, specularRoughness: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::specularRoughnessChanged(float
    specularRoughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    specularRoughness : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::specularRoughnessChanged(float
    #      specularRoughness)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial24specularRoughnessChangedEf',
        specularRoughness,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def roughnessMapChanged(
      self,
      roughnessMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::roughnessMapChanged(QQuick3DTexture
    *roughnessMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#roughnessMapChanged

    Parameters
    ----------

    roughnessMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::roughnessMapChanged(QQuick3DTexture
    #      *roughnessMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial19roughnessMapChangedEP15QQuick3'
        'DTexture',
        self._addressOf(roughnessMap),
    )

  @overload(float)
  def opacityChanged(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::opacityChanged(float opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacityChanged

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::opacityChanged(float opacity)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial14opacityChangedEf', opacity,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def opacityMapChanged(self, opacityMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::opacityMapChanged(QQuick3DTexture *opacityMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacityMapChanged

    Parameters
    ----------

    opacityMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::opacityMapChanged(QQuick3DTexture
    #      *opacityMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17opacityMapChangedEP15QQuick3DT'
        'exture',
        self._addressOf(opacityMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def bumpMapChanged(self, bumpMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::bumpMapChanged(QQuick3DTexture
    *bumpMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#bumpMapChanged

    Parameters
    ----------

    bumpMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::bumpMapChanged(QQuick3DTexture *bumpMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial14bumpMapChangedEP15QQuick3DText'
        'ure',
        self._addressOf(bumpMap),
    )

  @overload(float)
  def bumpAmountChanged(self, bumpAmount: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::bumpAmountChanged(float
    bumpAmount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#bumpAmountChanged

    Parameters
    ----------

    bumpAmount : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::bumpAmountChanged(float bumpAmount)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial17bumpAmountChangedEf',
        bumpAmount,
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def normalMapChanged(self, normalMap: Optional[QQuick3DTexture]) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::normalMapChanged(QQuick3DTexture *normalMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#normalMapChanged

    Parameters
    ----------

    normalMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::normalMapChanged(QQuick3DTexture
    #      *normalMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial16normalMapChangedEP15QQuick3DTe'
        'xture',
        self._addressOf(normalMap),
    )

  @overload(QQuick3DTexture)
  @overload(NoneType)
  def translucencyMapChanged(
      self,
      translucencyMap: Optional[QQuick3DTexture],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::translucencyMapChanged(QQuick3DTexture
    *translucencyMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    translucencyMap : Optional[QQuick3DTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::translucencyMapChanged(QQuick3DTexture
    #      *translucencyMap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial22translucencyMapChangedEP15QQui'
        'ck3DTexture',
        self._addressOf(translucencyMap),
    )

  @overload(float)
  def translucentFalloffChanged(self, translucentFalloff: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::translucentFalloffChanged(float
    translucentFalloff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    translucentFalloff : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::translucentFalloffChanged(float
    #      translucentFalloff)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial25translucentFalloffChangedEf',
        translucentFalloff,
    )

  @overload(float)
  def diffuseLightWrapChanged(self, diffuseLightWrap: float) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::diffuseLightWrapChanged(float
    diffuseLightWrap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    diffuseLightWrap : float
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::diffuseLightWrapChanged(float
    #      diffuseLightWrap)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial23diffuseLightWrapChangedEf',
        diffuseLightWrap,
    )

  @overload(bool)
  def vertexColorsEnabledChanged(self, vertexColorsEnabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::vertexColorsEnabledChanged(bool
    vertexColorsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    vertexColorsEnabled : bool
      Passed on as it is.
    """
    #  void QQuick3DDefaultMaterial::vertexColorsEnabledChanged(bool
    #      vertexColorsEnabled)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial26vertexColorsEnabledChangedEb',
        vertexColorsEnabled,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def roughnessChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::roughnessChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::roughnessChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial23roughnessChannelChangedEN16QQu'
        'ick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def opacityChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::opacityChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#opacityChannelChanged

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::opacityChannelChanged(QQuick3DMaterial::
    #      TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial21opacityChannelChangedEN16QQuic'
        'k3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  @overload(QQuick3DMaterial.TextureChannelMapping)
  def translucencyChannelChanged(
      self,
      channel: QQuick3DMaterial.TextureChannelMapping,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::translucencyChannelChanged(QQuick3DMaterial::
    TextureChannelMapping channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html

    Parameters
    ----------

    channel : QQuick3DMaterial.TextureChannelMapping
      Passed on as its number.
    """
    #  void QQuick3DDefaultMaterial::translucencyChannelChanged(
    #      QQuick3DMaterial::TextureChannelMapping channel)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial26translucencyChannelChangedEN16'
        'QQuick3DMaterial21TextureChannelMappingE',
        channel.value,
    )

  def pointSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::pointSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#pointSizeChanged
    """
    #  void QQuick3DDefaultMaterial::pointSizeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial16pointSizeChangedEv',
    )

  def lineWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::lineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#lineWidthChanged
    """
    #  void QQuick3DDefaultMaterial::lineWidthChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial16lineWidthChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DDefaultMaterial::updateSpatialNode(QSSGRenderGraphObject
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#updateSpatialNode

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
    #      *QQuick3DDefaultMaterial::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN23QQuick3DDefaultMaterial17updateSpatialNodeEP21QSSGRende'
        'rGraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DDefaultMaterial17updateSpatialNodeEP21QSS'
          'GRenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#markAllDirty
    """
    #  void QQuick3DDefaultMaterial::markAllDirty()
    ritual = 'ritual_ZN23QQuick3DDefaultMaterial12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DDefaultMaterial12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DDefaultMaterial::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DDefaultMaterial::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN23QQuick3DDefaultMaterial10itemChangeEN14QQuick3DObject10'
        'ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DDefaultMaterial10itemChangeEN14QQuick3DOb'
          'ject10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DDefaultMaterial::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3ddefaultmaterial.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DDefaultMaterial::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN23QQuick3DDefaultMaterial18updateSceneManagerEP20QQuick3D'
        'SceneManager',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DDefaultMaterial::markDirty(DirtyType type)': names the
    enum 'QQuick3DDefaultMaterial::DirtyType', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQuick3DDefaultMaterial.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DDefaultMaterial::markDirty(DirtyType type)': names "
        "the enum 'QQuick3DDefaultMaterial::DirtyType', whose class cannot "
        "be named here.")
