"""
QSSGRenderLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderLayer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGRenderNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D
  from . import QSSGRenderEffect, QSSGRenderRoot
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderEffect = WAIT['QSSGRenderEffect']
  QSSGRenderRoot = WAIT['QSSGRenderRoot']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderLayer(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderLayer: a plain Python object standing in
  front of one C++ QSSGRenderLayer.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderLayer is built
  on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderLayer that has a ritual and that Python
  can call so far, 12 names in all: 'isDirty', 'markDirty', 'clearDirty',
  'ref', 'ssaoEnabled', 'setProbeOrientation', 'hasEffect', 'isMsaaEnabled',
  'isSsaaEnabled', 'isProgressiveAAEnabled', 'isTemporalAAEnabled',
  'ssaaMultiplierForQuality'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderLayer::~QSSGRenderLayer()': the destructor: Python never
    removes a C++ QSSGRenderLayer.
  - Qt's 'void QSSGRenderLayer::addEffect(QSSGRenderEffect &inEffect)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderLayer::setImportScene(QSSGRenderNode &rootNode)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderLayer::removeImportScene(QSSGRenderNode
    &importedNode)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGRenderLayer is created at the first use, not by
    'QSSGRenderLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderLayer.
  - Each name of Qt's QSSGRenderLayer that has no cute function yet,
    'addEffect', 'removeImportScene', 'setImportScene', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderLayer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AAMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::AAMode' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoAA = Kee[int](0)
    SSAA = Kee[int](1)
    MSAA = Kee[int](2)
    ProgressiveAA = Kee[int](3)

  class AAQuality(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::AAQuality' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Normal = Kee[int](2)
    High = Kee[int](4)
    VeryHigh = Kee[int](8)

  class Background(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::Background' of Qt, with the 6 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Transparent = Kee[int](0)
    Unspecified = Kee[int](1)
    Color = Kee[int](2)
    SkyBox = Kee[int](3)
    SkyBoxCubeMap = Kee[int](4)
    SkyMaterial = Kee[int](5)

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::DirtyFlag' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    TreeDirty = Kee[int](1)
    VisibilityDirty = Kee[int](2)

  class HorizontalField(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::HorizontalField' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    LeftWidth = Kee[int](0)
    LeftRight = Kee[int](1)
    WidthRight = Kee[int](2)

  class LayerFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGRenderLayer::LayerFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QSSGRenderLayer::LayerFlags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    EnableDepthTest = 0x1
    EnableDepthPrePass = 0x2
    RenderToTarget = 0x3

  LayerFlags = LayerFlag

  class MaterialDebugMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::MaterialDebugMode' of Qt, with the 13 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    BaseColor = Kee[int](1)
    Roughness = Kee[int](2)
    Metalness = Kee[int](3)
    Diffuse = Kee[int](4)
    Specular = Kee[int](5)
    ShadowOcclusion = Kee[int](6)
    Emission = Kee[int](7)
    AmbientOcclusion = Kee[int](8)
    Normal = Kee[int](9)
    Tangent = Kee[int](10)
    Binormal = Kee[int](11)
    F0 = Kee[int](12)

  class OITMethod(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::OITMethod' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    WeightedBlended = Kee[int](1)
    LinkedList = Kee[int](2)

  class RenderExtensionStage(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::RenderExtensionStage' of Qt, with the 4 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    TextureProviders = Kee[int](0)
    Underlay = Kee[int](1)
    Overlay = Kee[int](2)
    Count = Kee[int](3)

  class RenderOverrides(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::RenderOverrides' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    DisableInternalPasses = Kee[int](1)

  class TAAMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::TAAMode' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Off = Kee[int](0)
    Default = Kee[int](1)
    MotionVector = Kee[int](2)

  class TonemapMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::TonemapMode' of Qt, with the 6 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    Linear = Kee[int](1)
    Aces = Kee[int](2)
    HejlDawson = Kee[int](3)
    Filmic = Kee[int](4)
    Custom = Kee[int](5)

  class UnitType(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::UnitType' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Percent = Kee[int](0)
    Pixels = Kee[int](1)

  class VerticalField(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderLayer::VerticalField' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    TopHeight = Kee[int](0)
    TopBottom = Kee[int](1)
    HeightBottom = Kee[int](2)

  #  The classes Qt writes inside QSSGRenderLayer, each a class in here as in
  #  C++.

  class FogOptions(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderLayer::FogOptions: a plain Python object
    standing in front of one C++ QSSGRenderLayer::FogOptions.

    C++ hands a QSSGRenderLayer::FogOptions around as a copy, so every C++
    QSSGRenderLayer::FogOptions behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGRenderLayer::FogOptions yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderLayer::FogOptions::~FogOptions()': the destructor:
      Python removes its C++ QSSGRenderLayer::FogOptions by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderLayer::FogOptions is created at the first use, not by
      'QSSGRenderLayer::FogOptions(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderLayer::FogOptions back gives a copy the
      ritual made for Python, in a new cute QSSGRenderLayer::FogOptions.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderLayer::FogOptions'

    #  Qt's '~QSSGRenderLayer::FogOptions()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderLayer::FogOptions behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QSSGRenderLayer10FogOptionsD1Ev'

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

  class LightProbeSettings(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderLayer::LightProbeSettings: a plain Python
    object standing in front of one C++ QSSGRenderLayer::LightProbeSettings.

    C++ hands a QSSGRenderLayer::LightProbeSettings around as a copy, so
    every C++ QSSGRenderLayer::LightProbeSettings behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderLayer::LightProbeSettings yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderLayer::LightProbeSettings::~LightProbeSettings()': the
      destructor: Python removes its C++ QSSGRenderLayer::LightProbeSettings
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderLayer::LightProbeSettings is created at the first
      use, not by 'QSSGRenderLayer::LightProbeSettings(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderLayer::LightProbeSettings back gives a
      copy the ritual made for Python, in a new cute
      QSSGRenderLayer::LightProbeSettings.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderLayer::LightProbeSettings'

    #  Qt's '~QSSGRenderLayer::LightProbeSettings()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderLayer::LightProbeSettings
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QSSGRenderLayer18LightProbeSettingsD1Ev'

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

  @staticmethod
  @overload(AAQuality)
  def ssaaMultiplierForQuality(quality: AAQuality) -> float:
    """
    Calls Qt's 'float
    QSSGRenderLayer::ssaaMultiplierForQuality(QSSGRenderLayer::AAQuality
    quality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlayer.html#ssaaMultiplierForQuality

    Parameters
    ----------

    quality : AAQuality
      Passed on as its number.
    """
    #  float QSSGRenderLayer::ssaaMultiplierForQuality(QSSGRenderLayer::
    #      AAQuality quality)
    return Rituals.call(
        'ritual_ZN15QSSGRenderLayer24ssaaMultiplierForQualityENS_9AAQuality'
        'E',
        quality.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderLayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DirtyFlag)
  def isDirty(self, dirtyFlag: DirtyFlag) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::isDirty(DirtyFlag dirtyFlag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#isDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  bool QSSGRenderLayer::isDirty(DirtyFlag dirtyFlag) const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderLayer7isDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  def ssaoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::ssaoEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#ssaoEnabled
    """
    #  bool QSSGRenderLayer::ssaoEnabled() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderLayer11ssaoEnabledEv')

  @overload(QSSGRenderEffect)
  @overload(NoneType)
  def hasEffect(self, inEffect: Optional[QSSGRenderEffect]) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::hasEffect(QSSGRenderEffect *inEffect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#hasEffect

    Parameters
    ----------

    inEffect : Optional[QSSGRenderEffect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSSGRenderLayer::hasEffect(QSSGRenderEffect *inEffect) const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderLayer9hasEffectEP16QSSGRenderEffect',
        self._addressOf(inEffect),
    )

  def isMsaaEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::isMsaaEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#isMsaaEnabled
    """
    #  bool QSSGRenderLayer::isMsaaEnabled() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderLayer13isMsaaEnabledEv')

  def isSsaaEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::isSsaaEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#isSsaaEnabled
    """
    #  bool QSSGRenderLayer::isSsaaEnabled() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderLayer13isSsaaEnabledEv')

  def isProgressiveAAEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::isProgressiveAAEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlayer.html#isProgressiveAAEnabled
    """
    #  bool QSSGRenderLayer::isProgressiveAAEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderLayer22isProgressiveAAEnabledEv',
    )

  def isTemporalAAEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderLayer::isTemporalAAEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlayer.html#isTemporalAAEnabled
    """
    #  bool QSSGRenderLayer::isTemporalAAEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderLayer19isTemporalAAEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setProbeOrientation(self, angles: QVector3D) -> None:
    """
    Calls Qt's 'void QSSGRenderLayer::setProbeOrientation(const QVector3D
    &angles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlayer.html#setProbeOrientation

    Parameters
    ----------

    angles : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGRenderLayer::setProbeOrientation(const QVector3D &angles)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLayer19setProbeOrientationERK9QVector3D',
        self._valueOf(angles),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderLayer::QSSGRenderLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderlayer.html#QSSGRenderLayer
    """
    #  QSSGRenderLayer::QSSGRenderLayer()
    self._noteCreation(QSSGRenderLayer, lambda: Rituals.call(
        'ritual_ZN15QSSGRenderLayerC1Ev',
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

  @overload(DirtyFlag)
  def markDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderLayer::markDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#markDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderLayer::markDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLayer9markDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderLayer::clearDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#clearDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderLayer::clearDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLayer10clearDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(QSSGRenderRoot)
  @overload(NoneType)
  def ref(self, inRootNode: Optional[QSSGRenderRoot]) -> None:
    """
    Calls Qt's 'void QSSGRenderLayer::ref(QSSGRenderRoot *inRootNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderlayer.html#ref

    Parameters
    ----------

    inRootNode : Optional[QSSGRenderRoot]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRenderLayer::ref(QSSGRenderRoot *inRootNode)
    self.uglySide.call(
        'ritual_ZN15QSSGRenderLayer3refEP14QSSGRenderRoot',
        self._addressOf(inRootNode),
    )

  @staticmethod
  def addEffect(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderLayer::addEffect(QSSGRenderEffect &inEffect)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderLayer.addEffect' has no cute function yet. Qt's 'void "
        "QSSGRenderLayer::addEffect(QSSGRenderEffect &inEffect)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def removeImportScene(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderLayer::removeImportScene(QSSGRenderNode
    &importedNode)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderLayer.removeImportScene' has no cute function yet. Qt's "
        "'void QSSGRenderLayer::removeImportScene(QSSGRenderNode "
        "&importedNode)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setImportScene(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderLayer::setImportScene(QSSGRenderNode &rootNode)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderLayer.setImportScene' has no cute function yet. Qt's "
        "'void QSSGRenderLayer::setImportScene(QSSGRenderNode &rootNode)': "
        "takes a type Python has no way to hand over yet.")
