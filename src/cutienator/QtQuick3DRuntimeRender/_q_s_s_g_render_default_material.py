"""
QSSGRenderDefaultMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterial_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderDefaultMaterial to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum
from ..occult import Rituals
from . import QSSGRenderGraphObject


class QSSGRenderDefaultMaterial(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderDefaultMaterial: a plain Python object
  standing in front of one C++ QSSGRenderDefaultMaterial.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderDefaultMaterial is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderDefaultMaterial that has a ritual and that
  Python can call so far, 16 names in all: 'isSpecularEnabled',
  'isMetalnessEnabled', 'isFresnelScaleBiasEnabled',
  'isClearcoatFresnelScaleBiasEnabled', 'isFresnelEnabled',
  'isVertexColorsEnabled', 'isVertexColorsMaskEnabled',
  'isInvertOpacityMapValue', 'isBaseColorSingleChannelEnabled',
  'isSpecularAmountSingleChannelEnabled', 'isEmissiveSingleChannelEnabled',
  'hasLighting', 'isClearcoatEnabled', 'isTransmissionEnabled', 'isDirty',
  'clearDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderDefaultMaterial::~QSSGRenderDefaultMaterial()': the
    destructor: Python never removes a C++ QSSGRenderDefaultMaterial.

  What to expect
  --------------

  - The C++ QSSGRenderDefaultMaterial is created at the first use, not by
    'QSSGRenderDefaultMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderDefaultMaterial.
  """

  #  The enums Qt writes inside QSSGRenderDefaultMaterial, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class MaterialAlphaMode(CuteNum):
    """
    The enum 'QSSGRenderDefaultMaterial::MaterialAlphaMode' of Qt, with the 4
    names Qt gives in it.
    """

    Default = Kee[int](0)
    Mask = Kee[int](1)
    Blend = Kee[int](2)
    Opaque = Kee[int](3)

  class MaterialBlendMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderDefaultMaterial::MaterialBlendMode' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    SourceOver = Kee[int](0)
    Screen = Kee[int](1)
    Multiply = Kee[int](2)

  class MaterialDiffuseModel(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderDefaultMaterial::MaterialDiffuseModel' of Qt, with
    the 3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Burley = Kee[int](0)
    Lambert = Kee[int](1)
    LambertWrap = Kee[int](2)

  class MaterialLighting(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderDefaultMaterial::MaterialLighting' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    NoLighting = Kee[int](0)
    FragmentLighting = Kee[int](1)

  class MaterialSpecularModel(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderDefaultMaterial::MaterialSpecularModel' of Qt, with
    the 2 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    BlinnPhong = Kee[int](0)
    SchlickGGX = Kee[int](1)

  class TextureChannelMapping(CuteNum):
    """
    The enum 'QSSGRenderDefaultMaterial::TextureChannelMapping' of Qt, with
    the 4 names Qt gives in it.
    """

    R = Kee[int](0)
    G = Kee[int](1)
    B = Kee[int](2)
    A = Kee[int](3)

  class VertexColorMask(CuteFlags, number='unsigned short'):
    """
    The flags enum 'QSSGRenderDefaultMaterial::VertexColorMask' of Qt, with
    the 12 names Qt gives in it. Qt names the type of its combinations
    'QSSGRenderDefaultMaterial::VertexColorMaskFlags'.
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderDefaultMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSpecularEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isSpecularEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#isSpecularEnabled
    """
    #  bool QSSGRenderDefaultMaterial::isSpecularEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial17isSpecularEnabledEv',
    )

  def isMetalnessEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isMetalnessEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#isMetalnessEnabled
    """
    #  bool QSSGRenderDefaultMaterial::isMetalnessEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial18isMetalnessEnabledEv',
    )

  def isFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isFresnelScaleBiasEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isFresnelScaleBiasEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial25isFresnelScaleBiasEnabledEv',
    )

  def isClearcoatFresnelScaleBiasEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderDefaultMaterial::isClearcoatFresnelScaleBiasEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isClearcoatFresnelScaleBiasEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial34isClearcoatFresnelScaleBias'
        'EnabledEv',
    )

  def isFresnelEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isFresnelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#isFresnelEnabled
    """
    #  bool QSSGRenderDefaultMaterial::isFresnelEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial16isFresnelEnabledEv',
    )

  def isVertexColorsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isVertexColorsEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isVertexColorsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial21isVertexColorsEnabledEv',
    )

  def isVertexColorsMaskEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isVertexColorsMaskEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isVertexColorsMaskEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial25isVertexColorsMaskEnabledEv',
    )

  def isInvertOpacityMapValue(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isInvertOpacityMapValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isInvertOpacityMapValue() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial23isInvertOpacityMapValueEv',
    )

  def isBaseColorSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderDefaultMaterial::isBaseColorSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isBaseColorSingleChannelEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial31isBaseColorSingleChannelEna'
        'bledEv',
    )

  def isSpecularAmountSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderDefaultMaterial::isSpecularAmountSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isSpecularAmountSingleChannelEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial36isSpecularAmountSingleChann'
        'elEnabledEv',
    )

  def isEmissiveSingleChannelEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderDefaultMaterial::isEmissiveSingleChannelEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isEmissiveSingleChannelEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial30isEmissiveSingleChannelEnab'
        'ledEv',
    )

  def hasLighting(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::hasLighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#hasLighting
    """
    #  bool QSSGRenderDefaultMaterial::hasLighting() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial11hasLightingEv',
    )

  def isClearcoatEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isClearcoatEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#isClearcoatEnabled
    """
    #  bool QSSGRenderDefaultMaterial::isClearcoatEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial18isClearcoatEnabledEv',
    )

  def isTransmissionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isTransmissionEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html
    """
    #  bool QSSGRenderDefaultMaterial::isTransmissionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial21isTransmissionEnabledEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderDefaultMaterial::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#isDirty
    """
    #  bool QSSGRenderDefaultMaterial::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderDefaultMaterial7isDirtyEv',
    )

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
  @overload(QSSGRenderGraphObject.Type)
  def __init__(
      self,
      type: QSSGRenderGraphObject.Type = (
          QSSGRenderGraphObject.Type.DefaultMaterial),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderDefaultMaterial::QSSGRenderDefaultMaterial(Type type)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QSSGRenderGraphObject.Type.DefaultMaterial.
    """
    #  QSSGRenderDefaultMaterial::QSSGRenderDefaultMaterial(Type type)
    self._noteCreation(QSSGRenderDefaultMaterial, lambda: Rituals.call(
        'ritual_ZN25QSSGRenderDefaultMaterialC1EN21QSSGRenderGraphObject4Ty'
        'peE',
        type.value,
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

  def clearDirty(self) -> None:
    """
    Calls Qt's 'void QSSGRenderDefaultMaterial::clearDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderdefaultmaterial.html#clearDirty
    """
    #  void QSSGRenderDefaultMaterial::clearDirty()
    self.uglySide.call('ritual_ZN25QSSGRenderDefaultMaterial10clearDirtyEv')
