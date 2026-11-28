"""
QRhiGraphicsPipeline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiImplementation, QRhiRenderPassDescriptor
  from . import QRhiShaderResourceBindings, QRhiShaderStage
  from . import QRhiVertexInputLayout
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QRhiVertexInputLayout = WAIT['QRhiVertexInputLayout']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiGraphicsPipeline(QRhiResource):
  """
  The cute side of Qt's QRhiGraphicsPipeline: a plain Python object standing
  in front of one C++ QRhiGraphicsPipeline.

  It is built on the cute 'QRhiResource', as Qt's QRhiGraphicsPipeline is
  built on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiGraphicsPipeline that has a ritual and that
  Python can call so far, 56 names in all: 'resourceType', 'flags',
  'setFlags', 'topology', 'setTopology', 'cullMode', 'setCullMode',
  'frontFace', 'setFrontFace', 'cbeginTargetBlends', 'cendTargetBlends',
  'targetBlendAt', 'targetBlendCount', 'hasDepthTest', 'setDepthTest',
  'hasDepthWrite', 'setDepthWrite', 'hasDepthClamp', 'setDepthClamp',
  'depthOp', 'setDepthOp', 'hasStencilTest', 'setStencilTest',
  'stencilFront', 'setStencilFront', 'stencilBack', 'setStencilBack',
  'stencilReadMask', 'setStencilReadMask', 'stencilWriteMask',
  'setStencilWriteMask', 'sampleCount', 'setSampleCount', 'lineWidth',
  'setLineWidth', 'depthBias', 'setDepthBias', 'slopeScaledDepthBias',
  'setSlopeScaledDepthBias', 'cbeginShaderStages', 'cendShaderStages',
  'shaderStageAt', 'shaderStageCount', 'vertexInputLayout',
  'setVertexInputLayout', 'shaderResourceBindings',
  'setShaderResourceBindings', 'renderPassDescriptor',
  'setRenderPassDescriptor', 'patchControlPointCount',
  'setPatchControlPointCount', 'polygonMode', 'setPolygonMode',
  'multiViewCount', 'setMultiViewCount', 'create'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QRhiGraphicsPipeline::setTargetBlends(std::initializer_list<TargetBlend>
    list)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRhiGraphicsPipeline::setShaderStages(std::
    initializer_list<QRhiShaderStage> list)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 61 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QRhiGraphicsPipeline is created at the first use, not by
    'QRhiGraphicsPipeline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiGraphicsPipeline.
  - Each name of Qt's QRhiGraphicsPipeline that has no cute function yet,
    'setShaderStages', 'setTargetBlends', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiGraphicsPipeline, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BlendFactor(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::BlendFactor' of Qt, with the 19 names Qt
    gives in it.
    """

    Zero = Kee[int](0)
    One = Kee[int](1)
    SrcColor = Kee[int](2)
    OneMinusSrcColor = Kee[int](3)
    DstColor = Kee[int](4)
    OneMinusDstColor = Kee[int](5)
    SrcAlpha = Kee[int](6)
    OneMinusSrcAlpha = Kee[int](7)
    DstAlpha = Kee[int](8)
    OneMinusDstAlpha = Kee[int](9)
    ConstantColor = Kee[int](10)
    OneMinusConstantColor = Kee[int](11)
    ConstantAlpha = Kee[int](12)
    OneMinusConstantAlpha = Kee[int](13)
    SrcAlphaSaturate = Kee[int](14)
    Src1Color = Kee[int](15)
    OneMinusSrc1Color = Kee[int](16)
    Src1Alpha = Kee[int](17)
    OneMinusSrc1Alpha = Kee[int](18)

  class BlendOp(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::BlendOp' of Qt, with the 5 names Qt gives
    in it.
    """

    Add = Kee[int](0)
    Subtract = Kee[int](1)
    ReverseSubtract = Kee[int](2)
    Min = Kee[int](3)
    Max = Kee[int](4)

  class ColorMaskComponent(CuteFlags):
    """
    The flags enum 'QRhiGraphicsPipeline::ColorMaskComponent' of Qt, with the
    4 names Qt gives in it. Qt names the type of its combinations
    'QRhiGraphicsPipeline::ColorMask'.
    """

    R = 0x1
    G = 0x2
    B = 0x4
    A = 0x8

  ColorMask = ColorMaskComponent

  class CompareOp(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::CompareOp' of Qt, with the 8 names Qt
    gives in it.
    """

    Never = Kee[int](0)
    Less = Kee[int](1)
    Equal = Kee[int](2)
    LessOrEqual = Kee[int](3)
    Greater = Kee[int](4)
    NotEqual = Kee[int](5)
    GreaterOrEqual = Kee[int](6)
    Always = Kee[int](7)

  class CullMode(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::CullMode' of Qt, with the 3 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Front = Kee[int](1)
    Back = Kee[int](2)

  class Flag(CuteFlags):
    """
    The flags enum 'QRhiGraphicsPipeline::Flag' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QRhiGraphicsPipeline::Flags'.
    """

    UsesBlendConstants = 0x1
    UsesStencilRef = 0x2
    UsesScissor = 0x4
    CompileShadersWithDebugInfo = 0x8
    UsesShadingRate = 0x10
    UsesIndirectDraws = 0x20

  Flags = Flag

  class FrontFace(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::FrontFace' of Qt, with the 2 names Qt
    gives in it.
    """

    CCW = Kee[int](0)
    CW = Kee[int](1)

  class PolygonMode(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::PolygonMode' of Qt, with the 2 names Qt
    gives in it.
    """

    Fill = Kee[int](0)
    Line = Kee[int](1)

  class StencilOp(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::StencilOp' of Qt, with the 8 names Qt
    gives in it.
    """

    StencilZero = Kee[int](0)
    Keep = Kee[int](1)
    Replace = Kee[int](2)
    IncrementAndClamp = Kee[int](3)
    DecrementAndClamp = Kee[int](4)
    Invert = Kee[int](5)
    IncrementAndWrap = Kee[int](6)
    DecrementAndWrap = Kee[int](7)

  class Topology(CuteNum):
    """
    The enum 'QRhiGraphicsPipeline::Topology' of Qt, with the 7 names Qt
    gives in it.
    """

    Triangles = Kee[int](0)
    TriangleStrip = Kee[int](1)
    TriangleFan = Kee[int](2)
    Lines = Kee[int](3)
    LineStrip = Kee[int](4)
    Points = Kee[int](5)
    Patches = Kee[int](6)

  #  The classes Qt writes inside QRhiGraphicsPipeline, each a class in here
  #  as in C++.

  class StencilOpState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGraphicsPipeline::StencilOpState: a plain
    Python object standing in front of one C++
    QRhiGraphicsPipeline::StencilOpState.

    C++ hands a QRhiGraphicsPipeline::StencilOpState around as a copy, so
    every C++ QRhiGraphicsPipeline::StencilOpState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiGraphicsPipeline::StencilOpState yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGraphicsPipeline::StencilOpState::~StencilOpState()': the
      destructor: Python removes its C++ QRhiGraphicsPipeline::StencilOpState
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGraphicsPipeline::StencilOpState is created at the first
      use, not by 'QRhiGraphicsPipeline::StencilOpState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGraphicsPipeline::StencilOpState back gives a
      copy the ritual made for Python, in a new cute
      QRhiGraphicsPipeline::StencilOpState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGraphicsPipeline::StencilOpState'

    #  Qt's '~QRhiGraphicsPipeline::StencilOpState()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QRhiGraphicsPipeline::StencilOpState behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN20QRhiGraphicsPipeline14StencilOpStateD1Ev'

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

  class TargetBlend(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiGraphicsPipeline::TargetBlend: a plain Python
    object standing in front of one C++ QRhiGraphicsPipeline::TargetBlend.

    C++ hands a QRhiGraphicsPipeline::TargetBlend around as a copy, so every
    C++ QRhiGraphicsPipeline::TargetBlend behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QRhiGraphicsPipeline::TargetBlend yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiGraphicsPipeline::TargetBlend::~TargetBlend()': the
      destructor: Python removes its C++ QRhiGraphicsPipeline::TargetBlend by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QRhiGraphicsPipeline::TargetBlend is created at the first use,
      not by 'QRhiGraphicsPipeline::TargetBlend(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiGraphicsPipeline::TargetBlend back gives a copy
      the ritual made for Python, in a new cute
      QRhiGraphicsPipeline::TargetBlend.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiGraphicsPipeline::TargetBlend'

    #  Qt's '~QRhiGraphicsPipeline::TargetBlend()'. Naming it makes this a
    #  value class: Python owns every C++ QRhiGraphicsPipeline::TargetBlend
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QRhiGraphicsPipeline11TargetBlendD1Ev'

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
  __qt_class__ = 'QRhiGraphicsPipeline'

  #  A C++ QRhiGraphicsPipeline Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiGraphicsPipeline'

  #  The functions Qt calls itself that QRhiGraphicsPipeline is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN20QRhiGraphicsPipeline6createEv',
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

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiGraphicsPipeline::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
    ritual = 'ritual_ZNK20QRhiGraphicsPipeline12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QRhiGraphicsPipeline12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QRhiGraphicsPipeline::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QRhiGraphicsPipeline::flags() const
    return QRhiGraphicsPipeline.Flags(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline5flagsEv',
    ))

  def topology(self) -> Topology:
    """
    Calls Qt's 'Topology QRhiGraphicsPipeline::topology() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#topology

    Returns
    -------

    Topology
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Topology(number)' gives.
    """
    #  Topology QRhiGraphicsPipeline::topology() const
    return QRhiGraphicsPipeline.Topology(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline8topologyEv',
    ))

  def cullMode(self) -> CullMode:
    """
    Calls Qt's 'CullMode QRhiGraphicsPipeline::cullMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#cullMode

    Returns
    -------

    CullMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CullMode(number)' gives.
    """
    #  CullMode QRhiGraphicsPipeline::cullMode() const
    return QRhiGraphicsPipeline.CullMode(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline8cullModeEv',
    ))

  def frontFace(self) -> FrontFace:
    """
    Calls Qt's 'FrontFace QRhiGraphicsPipeline::frontFace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#frontFace

    Returns
    -------

    FrontFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrontFace(number)' gives.
    """
    #  FrontFace QRhiGraphicsPipeline::frontFace() const
    return QRhiGraphicsPipeline.FrontFace(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline9frontFaceEv',
    ))

  def cbeginTargetBlends(self) -> Optional[TargetBlend]:
    """
    Calls Qt's 'const TargetBlend *QRhiGraphicsPipeline::cbeginTargetBlends()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#cbeginTargetBlends

    Returns
    -------

    Optional[TargetBlend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const TargetBlend *QRhiGraphicsPipeline::cbeginTargetBlends() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline18cbeginTargetBlendsEv',
    )
    return QRhiGraphicsPipeline.TargetBlend._cuteAt(address)

  def cendTargetBlends(self) -> Optional[TargetBlend]:
    """
    Calls Qt's 'const TargetBlend *QRhiGraphicsPipeline::cendTargetBlends()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#cendTargetBlends

    Returns
    -------

    Optional[TargetBlend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const TargetBlend *QRhiGraphicsPipeline::cendTargetBlends() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline16cendTargetBlendsEv',
    )
    return QRhiGraphicsPipeline.TargetBlend._cuteAt(address)

  @overload(int)
  def targetBlendAt(self, index: int) -> Optional[TargetBlend]:
    """
    Calls Qt's 'const TargetBlend
    *QRhiGraphicsPipeline::targetBlendAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#targetBlendAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[TargetBlend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const TargetBlend *QRhiGraphicsPipeline::targetBlendAt(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline13targetBlendAtEx', index,
    )
    return QRhiGraphicsPipeline.TargetBlend._cuteAt(address)

  def targetBlendCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiGraphicsPipeline::targetBlendCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#targetBlendCount
    """
    #  qsizetype QRhiGraphicsPipeline::targetBlendCount() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline16targetBlendCountEv',
    )

  def hasDepthTest(self) -> bool:
    """
    Calls Qt's 'bool QRhiGraphicsPipeline::hasDepthTest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#hasDepthTest
    """
    #  bool QRhiGraphicsPipeline::hasDepthTest() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline12hasDepthTestEv',
    )

  def hasDepthWrite(self) -> bool:
    """
    Calls Qt's 'bool QRhiGraphicsPipeline::hasDepthWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#hasDepthWrite
    """
    #  bool QRhiGraphicsPipeline::hasDepthWrite() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline13hasDepthWriteEv',
    )

  def hasDepthClamp(self) -> bool:
    """
    Calls Qt's 'bool QRhiGraphicsPipeline::hasDepthClamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#hasDepthClamp
    """
    #  bool QRhiGraphicsPipeline::hasDepthClamp() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline13hasDepthClampEv',
    )

  def depthOp(self) -> CompareOp:
    """
    Calls Qt's 'CompareOp QRhiGraphicsPipeline::depthOp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#depthOp

    Returns
    -------

    CompareOp
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompareOp(number)' gives.
    """
    #  CompareOp QRhiGraphicsPipeline::depthOp() const
    return QRhiGraphicsPipeline.CompareOp(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline7depthOpEv',
    ))

  def hasStencilTest(self) -> bool:
    """
    Calls Qt's 'bool QRhiGraphicsPipeline::hasStencilTest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#hasStencilTest
    """
    #  bool QRhiGraphicsPipeline::hasStencilTest() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline14hasStencilTestEv',
    )

  def stencilFront(self) -> StencilOpState:
    """
    Calls Qt's 'StencilOpState QRhiGraphicsPipeline::stencilFront() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#stencilFront

    Returns
    -------

    StencilOpState
      A new cute QRhiGraphicsPipeline::StencilOpState around the copy Qt gave
      back. Python owns it.
    """
    #  StencilOpState QRhiGraphicsPipeline::stencilFront() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline12stencilFrontEv',
    )
    return QRhiGraphicsPipeline.StencilOpState._cuteOwning(address)

  def stencilBack(self) -> StencilOpState:
    """
    Calls Qt's 'StencilOpState QRhiGraphicsPipeline::stencilBack() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#stencilBack

    Returns
    -------

    StencilOpState
      A new cute QRhiGraphicsPipeline::StencilOpState around the copy Qt gave
      back. Python owns it.
    """
    #  StencilOpState QRhiGraphicsPipeline::stencilBack() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline11stencilBackEv',
    )
    return QRhiGraphicsPipeline.StencilOpState._cuteOwning(address)

  def stencilReadMask(self) -> int:
    """
    Calls Qt's 'quint32 QRhiGraphicsPipeline::stencilReadMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#stencilReadMask
    """
    #  quint32 QRhiGraphicsPipeline::stencilReadMask() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline15stencilReadMaskEv',
    )

  def stencilWriteMask(self) -> int:
    """
    Calls Qt's 'quint32 QRhiGraphicsPipeline::stencilWriteMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#stencilWriteMask
    """
    #  quint32 QRhiGraphicsPipeline::stencilWriteMask() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline16stencilWriteMaskEv',
    )

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QRhiGraphicsPipeline::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#sampleCount
    """
    #  int QRhiGraphicsPipeline::sampleCount() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline11sampleCountEv',
    )

  def lineWidth(self) -> float:
    """
    Calls Qt's 'float QRhiGraphicsPipeline::lineWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#lineWidth
    """
    #  float QRhiGraphicsPipeline::lineWidth() const
    return self.uglySide.call('ritual_ZNK20QRhiGraphicsPipeline9lineWidthEv')

  def depthBias(self) -> int:
    """
    Calls Qt's 'int QRhiGraphicsPipeline::depthBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#depthBias
    """
    #  int QRhiGraphicsPipeline::depthBias() const
    return self.uglySide.call('ritual_ZNK20QRhiGraphicsPipeline9depthBiasEv')

  def slopeScaledDepthBias(self) -> float:
    """
    Calls Qt's 'float QRhiGraphicsPipeline::slopeScaledDepthBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#slopeScaledDepthBias
    """
    #  float QRhiGraphicsPipeline::slopeScaledDepthBias() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline20slopeScaledDepthBiasEv',
    )

  def cbeginShaderStages(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage
    *QRhiGraphicsPipeline::cbeginShaderStages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#cbeginShaderStages

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QRhiGraphicsPipeline::cbeginShaderStages()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline18cbeginShaderStagesEv',
    )
    from . import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def cendShaderStages(self) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage
    *QRhiGraphicsPipeline::cendShaderStages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#cendShaderStages

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QRhiGraphicsPipeline::cendShaderStages() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline16cendShaderStagesEv',
    )
    from . import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  @overload(int)
  def shaderStageAt(self, index: int) -> Optional[QRhiShaderStage]:
    """
    Calls Qt's 'const QRhiShaderStage
    *QRhiGraphicsPipeline::shaderStageAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#shaderStageAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiShaderStage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderStage *QRhiGraphicsPipeline::shaderStageAt(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline13shaderStageAtEx', index,
    )
    from . import QRhiShaderStage
    return QRhiShaderStage._cuteAt(address)

  def shaderStageCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiGraphicsPipeline::shaderStageCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#shaderStageCount
    """
    #  qsizetype QRhiGraphicsPipeline::shaderStageCount() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline16shaderStageCountEv',
    )

  def vertexInputLayout(self) -> QRhiVertexInputLayout:
    """
    Calls Qt's 'QRhiVertexInputLayout
    QRhiGraphicsPipeline::vertexInputLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#vertexInputLayout

    Returns
    -------

    QRhiVertexInputLayout
      A new cute QRhiVertexInputLayout around the copy Qt gave back. Python
      owns it.
    """
    #  QRhiVertexInputLayout QRhiGraphicsPipeline::vertexInputLayout() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline17vertexInputLayoutEv',
    )
    from . import QRhiVertexInputLayout
    return QRhiVertexInputLayout._cuteOwning(address)

  def shaderResourceBindings(self) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings
    *QRhiGraphicsPipeline::shaderResourceBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#shaderResourceBindings

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings
    #      *QRhiGraphicsPipeline::shaderResourceBindings() const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline22shaderResourceBindingsEv',
    )
    from . import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  def renderPassDescriptor(self) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QRhiGraphicsPipeline::renderPassDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#renderPassDescriptor

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor *QRhiGraphicsPipeline::renderPassDescriptor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline20renderPassDescriptorEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def patchControlPointCount(self) -> int:
    """
    Calls Qt's 'int QRhiGraphicsPipeline::patchControlPointCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#patchControlPointCount
    """
    #  int QRhiGraphicsPipeline::patchControlPointCount() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline22patchControlPointCountEv',
    )

  def polygonMode(self) -> PolygonMode:
    """
    Calls Qt's 'PolygonMode QRhiGraphicsPipeline::polygonMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#polygonMode

    Returns
    -------

    PolygonMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PolygonMode(number)'
      gives.
    """
    #  PolygonMode QRhiGraphicsPipeline::polygonMode() const
    return QRhiGraphicsPipeline.PolygonMode(self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline11polygonModeEv',
    ))

  def multiViewCount(self) -> int:
    """
    Calls Qt's 'int QRhiGraphicsPipeline::multiViewCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#multiViewCount
    """
    #  int QRhiGraphicsPipeline::multiViewCount() const
    return self.uglySide.call(
        'ritual_ZNK20QRhiGraphicsPipeline14multiViewCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline8setFlagsE6QFlagsINS_4FlagEE',
        f.value,
    )

  @overload(Topology)
  def setTopology(self, t: Topology) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setTopology(Topology t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setTopology

    Parameters
    ----------

    t : Topology
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setTopology(Topology t)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline11setTopologyENS_8TopologyE',
        t.value,
    )

  @overload(CullMode)
  def setCullMode(self, mode: CullMode) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setCullMode(CullMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setCullMode

    Parameters
    ----------

    mode : CullMode
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setCullMode(CullMode mode)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline11setCullModeENS_8CullModeE',
        mode.value,
    )

  @overload(FrontFace)
  def setFrontFace(self, f: FrontFace) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setFrontFace(FrontFace f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setFrontFace

    Parameters
    ----------

    f : FrontFace
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setFrontFace(FrontFace f)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline12setFrontFaceENS_9FrontFaceE',
        f.value,
    )

  @overload(bool)
  def setDepthTest(self, enable: bool) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setDepthTest(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setDepthTest

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setDepthTest(bool enable)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline12setDepthTestEb', enable,
    )

  @overload(bool)
  def setDepthWrite(self, enable: bool) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setDepthWrite(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setDepthWrite

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setDepthWrite(bool enable)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline13setDepthWriteEb', enable,
    )

  @overload(bool)
  def setDepthClamp(self, enable: bool) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setDepthClamp(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setDepthClamp

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setDepthClamp(bool enable)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline13setDepthClampEb', enable,
    )

  @overload(CompareOp)
  def setDepthOp(self, op: CompareOp) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setDepthOp(CompareOp op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setDepthOp

    Parameters
    ----------

    op : CompareOp
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setDepthOp(CompareOp op)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline10setDepthOpENS_9CompareOpE',
        op.value,
    )

  @overload(bool)
  def setStencilTest(self, enable: bool) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setStencilTest(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setStencilTest

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setStencilTest(bool enable)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline14setStencilTestEb', enable,
    )

  @overload(StencilOpState)
  def setStencilFront(self, state: StencilOpState) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setStencilFront(const
    StencilOpState &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setStencilFront

    Parameters
    ----------

    state : StencilOpState
      Passed on as a value: Qt reads the C++
      QRhiGraphicsPipeline::StencilOpState, which stays Python's own.
    """
    #  void QRhiGraphicsPipeline::setStencilFront(const StencilOpState
    #      &state)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline15setStencilFrontERKNS_14StencilOpS'
        'tateE',
        self._valueOf(state),
    )

  @overload(StencilOpState)
  def setStencilBack(self, state: StencilOpState) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setStencilBack(const
    StencilOpState &state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setStencilBack

    Parameters
    ----------

    state : StencilOpState
      Passed on as a value: Qt reads the C++
      QRhiGraphicsPipeline::StencilOpState, which stays Python's own.
    """
    #  void QRhiGraphicsPipeline::setStencilBack(const StencilOpState &state)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline14setStencilBackERKNS_14StencilOpSt'
        'ateE',
        self._valueOf(state),
    )

  @overload(int)
  def setStencilReadMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setStencilReadMask(quint32 mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setStencilReadMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setStencilReadMask(quint32 mask)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline18setStencilReadMaskEj', mask,
    )

  @overload(int)
  def setStencilWriteMask(self, mask: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setStencilWriteMask(quint32
    mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setStencilWriteMask

    Parameters
    ----------

    mask : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setStencilWriteMask(quint32 mask)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline19setStencilWriteMaskEj', mask,
    )

  @overload(int)
  def setSampleCount(self, s: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setSampleCount(int s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setSampleCount

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setSampleCount(int s)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline14setSampleCountEi', s,
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setLineWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setLineWidth(float width)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline12setLineWidthEf', width,
    )

  @overload(int)
  def setDepthBias(self, bias: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setDepthBias(int bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setDepthBias

    Parameters
    ----------

    bias : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setDepthBias(int bias)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline12setDepthBiasEi', bias,
    )

  @overload(float)
  def setSlopeScaledDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setSlopeScaledDepthBias(float
    bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setSlopeScaledDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setSlopeScaledDepthBias(float bias)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline23setSlopeScaledDepthBiasEf', bias,
    )

  @overload(QRhiVertexInputLayout)
  def setVertexInputLayout(self, layout: QRhiVertexInputLayout) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setVertexInputLayout(const
    QRhiVertexInputLayout &layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setVertexInputLayout

    Parameters
    ----------

    layout : QRhiVertexInputLayout
      Passed on as a value: Qt reads the C++ QRhiVertexInputLayout, which
      stays Python's own.
    """
    #  void QRhiGraphicsPipeline::setVertexInputLayout(const
    #      QRhiVertexInputLayout &layout)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline20setVertexInputLayoutERK21QRhiVert'
        'exInputLayout',
        self._valueOf(layout),
    )

  @overload(QRhiShaderResourceBindings)
  @overload(NoneType)
  def setShaderResourceBindings(
      self,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setShaderResourceBindings(
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html

    Parameters
    ----------

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGraphicsPipeline::setShaderResourceBindings(
    #      QRhiShaderResourceBindings *srb)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline25setShaderResourceBindingsEP26QRhi'
        'ShaderResourceBindings',
        self._addressOf(srb),
    )

  @overload(QRhiRenderPassDescriptor)
  @overload(NoneType)
  def setRenderPassDescriptor(
      self,
      desc: Optional[QRhiRenderPassDescriptor],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiGraphicsPipeline::setRenderPassDescriptor(QRhiRenderPassDescriptor
    *desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setRenderPassDescriptor

    Parameters
    ----------

    desc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiGraphicsPipeline::setRenderPassDescriptor(
    #      QRhiRenderPassDescriptor *desc)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline23setRenderPassDescriptorEP24QRhiRe'
        'nderPassDescriptor',
        self._addressOf(desc),
    )

  @overload(int)
  def setPatchControlPointCount(self, count: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setPatchControlPointCount(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setPatchControlPointCount(int count)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline25setPatchControlPointCountEi',
        count,
    )

  @overload(PolygonMode)
  def setPolygonMode(self, mode: PolygonMode) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setPolygonMode(PolygonMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setPolygonMode

    Parameters
    ----------

    mode : PolygonMode
      Passed on as its number.
    """
    #  void QRhiGraphicsPipeline::setPolygonMode(PolygonMode mode)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline14setPolygonModeENS_11PolygonModeE',
        mode.value,
    )

  @overload(int)
  def setMultiViewCount(self, count: int) -> None:
    """
    Calls Qt's 'void QRhiGraphicsPipeline::setMultiViewCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#setMultiViewCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QRhiGraphicsPipeline::setMultiViewCount(int count)
    self.uglySide.call(
        'ritual_ZN20QRhiGraphicsPipeline17setMultiViewCountEi', count,
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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiGraphicsPipeline::QRhiGraphicsPipeline(QRhiImplementation *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhigraphicspipeline.html#QRhiGraphicsPipeline

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiGraphicsPipeline::QRhiGraphicsPipeline(QRhiImplementation *rhi)
    self._noteCreation(QRhiGraphicsPipeline, lambda: Rituals.call(
        'ritual_ZN20QRhiGraphicsPipelineC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiGraphicsPipeline::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhigraphicspipeline.html#create
    """
    #  bool QRhiGraphicsPipeline::create()
    return self.uglySide.call('ritual_ZN20QRhiGraphicsPipeline6createEv')

  @staticmethod
  def setShaderStages(*__, **_) -> Never:
    """
    - Qt's 'void QRhiGraphicsPipeline::setShaderStages(std::
      initializer_list<QRhiShaderStage> list)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QRhiGraphicsPipeline::setShaderStages': a template: a pattern and
      no single function.
    """
    raise NotImplementedError(
        "'QRhiGraphicsPipeline.setShaderStages' has no cute function yet. "
        "Qt's 'void "
        "QRhiGraphicsPipeline::setShaderStages(std::initializer_list<QRhiSha"
        "derStage> list)': takes a type Python has no way to hand over yet. "
        "Qt's 'QRhiGraphicsPipeline::setShaderStages': a template: a "
        "pattern and no single function.")

  @staticmethod
  def setTargetBlends(*__, **_) -> Never:
    """
    - Qt's 'void QRhiGraphicsPipeline::setTargetBlends(std::
      initializer_list<TargetBlend> list)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QRhiGraphicsPipeline::setTargetBlends': a template: a pattern and
      no single function.
    """
    raise NotImplementedError(
        "'QRhiGraphicsPipeline.setTargetBlends' has no cute function yet. "
        "Qt's 'void "
        "QRhiGraphicsPipeline::setTargetBlends(std::initializer_list<TargetB"
        "lend> list)': takes a type Python has no way to hand over yet. "
        "Qt's 'QRhiGraphicsPipeline::setTargetBlends': a template: a "
        "pattern and no single function.")
