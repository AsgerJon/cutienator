"""
QShaderDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qshaderdescription.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDataStream, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDataStream = WAIT['QDataStream']
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShaderDescription: a plain Python object standing in
  front of one C++ QShaderDescription.

  C++ hands a QShaderDescription around as a copy, so every C++
  QShaderDescription behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShaderDescription that has a ritual and that Python
  can call so far, 11 names in all: 'detach', 'isValid', 'serialize',
  'toJson', 'deserialize', 'tessellationOutputVertexCount',
  'tessellationMode', 'tessellationWindingOrder', 'tessellationPartitioning',
  '__rlshift__', '__eq__'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShaderDescription &QShaderDescription::operator=(const
    QShaderDescription &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QShaderDescription::~QShaderDescription()': the destructor: Python
    removes its C++ QShaderDescription by it, and has no other use for it.
  - Qt's 'QList<InOutVariable> QShaderDescription::inputVariables() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<InOutVariable> QShaderDescription::outputVariables() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<UniformBlock> QShaderDescription::uniformBlocks() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<PushConstantBlock> QShaderDescription::pushConstantBlocks()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<StorageBlock> QShaderDescription::storageBlocks() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<InOutVariable> QShaderDescription::combinedImageSamplers()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<InOutVariable> QShaderDescription::separateImages() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<InOutVariable> QShaderDescription::separateSamplers() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<InOutVariable> QShaderDescription::storageImages() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<BuiltinVariable> QShaderDescription::inputBuiltinVariables()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<BuiltinVariable> QShaderDescription::outputBuiltinVariables()
    const': gives a type Python has no way to take yet.
  - Qt's 'std::array<uint, 3> QShaderDescription::computeShaderLocalSize()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QShaderDescription is created at the first use, not by
    'QShaderDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShaderDescription back gives a copy the ritual made
    for Python, in a new cute QShaderDescription.
  - Each name of Qt's QShaderDescription that has no cute function yet,
    'combinedImageSamplers', 'computeShaderLocalSize',
    'inputBuiltinVariables', 'inputVariables', 'outputBuiltinVariables',
    'outputVariables', 'pushConstantBlocks', 'separateImages',
    'separateSamplers', 'storageBlocks', 'storageImages', 'uniformBlocks',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QShaderDescription, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BuiltinType(CuteNum):
    """
    The enum 'QShaderDescription::BuiltinType' of Qt, with the 30 names Qt
    gives in it.
    """

    PositionBuiltin = Kee[int](0)
    PointSizeBuiltin = Kee[int](1)
    ClipDistanceBuiltin = Kee[int](3)
    CullDistanceBuiltin = Kee[int](4)
    VertexIdBuiltin = Kee[int](5)
    InstanceIdBuiltin = Kee[int](6)
    PrimitiveIdBuiltin = Kee[int](7)
    InvocationIdBuiltin = Kee[int](8)
    LayerBuiltin = Kee[int](9)
    ViewportIndexBuiltin = Kee[int](10)
    TessLevelOuterBuiltin = Kee[int](11)
    TessLevelInnerBuiltin = Kee[int](12)
    TessCoordBuiltin = Kee[int](13)
    PatchVerticesBuiltin = Kee[int](14)
    FragCoordBuiltin = Kee[int](15)
    PointCoordBuiltin = Kee[int](16)
    FrontFacingBuiltin = Kee[int](17)
    SampleIdBuiltin = Kee[int](18)
    SamplePositionBuiltin = Kee[int](19)
    SampleMaskBuiltin = Kee[int](20)
    FragDepthBuiltin = Kee[int](22)
    NumWorkGroupsBuiltin = Kee[int](24)
    WorkgroupSizeBuiltin = Kee[int](25)
    WorkgroupIdBuiltin = Kee[int](26)
    LocalInvocationIdBuiltin = Kee[int](27)
    GlobalInvocationIdBuiltin = Kee[int](28)
    LocalInvocationIndexBuiltin = Kee[int](29)
    VertexIndexBuiltin = Kee[int](42)
    InstanceIndexBuiltin = Kee[int](43)
    ViewIndexBuiltin = Kee[int](4440)

  class ImageFlag(CuteFlags):
    """
    The flags enum 'QShaderDescription::ImageFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QShaderDescription::ImageFlags'.
    """

    ReadOnlyImage = 0x1
    WriteOnlyImage = 0x2

  ImageFlags = ImageFlag

  class ImageFormat(CuteNum):
    """
    The enum 'QShaderDescription::ImageFormat' of Qt, with the 40 names Qt
    gives in it.
    """

    ImageFormatUnknown = Kee[int](0)
    ImageFormatRgba32f = Kee[int](1)
    ImageFormatRgba16f = Kee[int](2)
    ImageFormatR32f = Kee[int](3)
    ImageFormatRgba8 = Kee[int](4)
    ImageFormatRgba8Snorm = Kee[int](5)
    ImageFormatRg32f = Kee[int](6)
    ImageFormatRg16f = Kee[int](7)
    ImageFormatR11fG11fB10f = Kee[int](8)
    ImageFormatR16f = Kee[int](9)
    ImageFormatRgba16 = Kee[int](10)
    ImageFormatRgb10A2 = Kee[int](11)
    ImageFormatRg16 = Kee[int](12)
    ImageFormatRg8 = Kee[int](13)
    ImageFormatR16 = Kee[int](14)
    ImageFormatR8 = Kee[int](15)
    ImageFormatRgba16Snorm = Kee[int](16)
    ImageFormatRg16Snorm = Kee[int](17)
    ImageFormatRg8Snorm = Kee[int](18)
    ImageFormatR16Snorm = Kee[int](19)
    ImageFormatR8Snorm = Kee[int](20)
    ImageFormatRgba32i = Kee[int](21)
    ImageFormatRgba16i = Kee[int](22)
    ImageFormatRgba8i = Kee[int](23)
    ImageFormatR32i = Kee[int](24)
    ImageFormatRg32i = Kee[int](25)
    ImageFormatRg16i = Kee[int](26)
    ImageFormatRg8i = Kee[int](27)
    ImageFormatR16i = Kee[int](28)
    ImageFormatR8i = Kee[int](29)
    ImageFormatRgba32ui = Kee[int](30)
    ImageFormatRgba16ui = Kee[int](31)
    ImageFormatRgba8ui = Kee[int](32)
    ImageFormatR32ui = Kee[int](33)
    ImageFormatRgb10a2ui = Kee[int](34)
    ImageFormatRg32ui = Kee[int](35)
    ImageFormatRg16ui = Kee[int](36)
    ImageFormatRg8ui = Kee[int](37)
    ImageFormatR16ui = Kee[int](38)
    ImageFormatR8ui = Kee[int](39)

  class QualifierFlag(CuteFlags):
    """
    The flags enum 'QShaderDescription::QualifierFlag' of Qt, with the 5
    names Qt gives in it. Qt names the type of its combinations
    'QShaderDescription::QualifierFlags'.
    """

    QualifierReadOnly = 0x1
    QualifierWriteOnly = 0x2
    QualifierCoherent = 0x4
    QualifierVolatile = 0x8
    QualifierRestrict = 0x10

  QualifierFlags = QualifierFlag

  class TessellationMode(CuteNum):
    """
    The enum 'QShaderDescription::TessellationMode' of Qt, with the 4 names
    Qt gives in it.
    """

    UnknownTessellationMode = Kee[int](0)
    TrianglesTessellationMode = Kee[int](1)
    QuadTessellationMode = Kee[int](2)
    IsolineTessellationMode = Kee[int](3)

  class TessellationPartitioning(CuteNum):
    """
    The enum 'QShaderDescription::TessellationPartitioning' of Qt, with the 4
    names Qt gives in it.
    """

    UnknownTessellationPartitioning = Kee[int](0)
    EqualTessellationPartitioning = Kee[int](1)
    FractionalEvenTessellationPartitioning = Kee[int](2)
    FractionalOddTessellationPartitioning = Kee[int](3)

  class TessellationWindingOrder(CuteNum):
    """
    The enum 'QShaderDescription::TessellationWindingOrder' of Qt, with the 3
    names Qt gives in it.
    """

    UnknownTessellationWindingOrder = Kee[int](0)
    CwTessellationWindingOrder = Kee[int](1)
    CcwTessellationWindingOrder = Kee[int](2)

  class VariableType(CuteNum):
    """
    The enum 'QShaderDescription::VariableType' of Qt, with the 70 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    Float = Kee[int](1)
    Vec2 = Kee[int](2)
    Vec3 = Kee[int](3)
    Vec4 = Kee[int](4)
    Mat2 = Kee[int](5)
    Mat2x3 = Kee[int](6)
    Mat2x4 = Kee[int](7)
    Mat3 = Kee[int](8)
    Mat3x2 = Kee[int](9)
    Mat3x4 = Kee[int](10)
    Mat4 = Kee[int](11)
    Mat4x2 = Kee[int](12)
    Mat4x3 = Kee[int](13)
    Int = Kee[int](14)
    Int2 = Kee[int](15)
    Int3 = Kee[int](16)
    Int4 = Kee[int](17)
    Uint = Kee[int](18)
    Uint2 = Kee[int](19)
    Uint3 = Kee[int](20)
    Uint4 = Kee[int](21)
    Bool = Kee[int](22)
    Bool2 = Kee[int](23)
    Bool3 = Kee[int](24)
    Bool4 = Kee[int](25)
    Double = Kee[int](26)
    Double2 = Kee[int](27)
    Double3 = Kee[int](28)
    Double4 = Kee[int](29)
    DMat2 = Kee[int](30)
    DMat2x3 = Kee[int](31)
    DMat2x4 = Kee[int](32)
    DMat3 = Kee[int](33)
    DMat3x2 = Kee[int](34)
    DMat3x4 = Kee[int](35)
    DMat4 = Kee[int](36)
    DMat4x2 = Kee[int](37)
    DMat4x3 = Kee[int](38)
    Sampler1D = Kee[int](39)
    Sampler2D = Kee[int](40)
    Sampler2DMS = Kee[int](41)
    Sampler3D = Kee[int](42)
    SamplerCube = Kee[int](43)
    Sampler1DArray = Kee[int](44)
    Sampler2DArray = Kee[int](45)
    Sampler2DMSArray = Kee[int](46)
    Sampler3DArray = Kee[int](47)
    SamplerCubeArray = Kee[int](48)
    SamplerRect = Kee[int](49)
    SamplerBuffer = Kee[int](50)
    SamplerExternalOES = Kee[int](51)
    Sampler = Kee[int](52)
    Image1D = Kee[int](53)
    Image2D = Kee[int](54)
    Image2DMS = Kee[int](55)
    Image3D = Kee[int](56)
    ImageCube = Kee[int](57)
    Image1DArray = Kee[int](58)
    Image2DArray = Kee[int](59)
    Image2DMSArray = Kee[int](60)
    Image3DArray = Kee[int](61)
    ImageCubeArray = Kee[int](62)
    ImageRect = Kee[int](63)
    ImageBuffer = Kee[int](64)
    Struct = Kee[int](65)
    Half = Kee[int](66)
    Half2 = Kee[int](67)
    Half3 = Kee[int](68)
    Half4 = Kee[int](69)

  #  The classes Qt writes inside QShaderDescription, each a class in here as
  #  in C++.

  class BlockVariable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::BlockVariable: a plain Python
    object standing in front of one C++ QShaderDescription::BlockVariable.

    C++ hands a QShaderDescription::BlockVariable around as a copy, so every
    C++ QShaderDescription::BlockVariable behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::BlockVariable yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::BlockVariable::~BlockVariable()': the
      destructor: Python removes its C++ QShaderDescription::BlockVariable by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QShaderDescription::BlockVariable is created at the first use,
      not by 'QShaderDescription::BlockVariable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::BlockVariable back gives a copy
      the ritual made for Python, in a new cute
      QShaderDescription::BlockVariable.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::BlockVariable'

    #  Qt's '~QShaderDescription::BlockVariable()'. Naming it makes this a
    #  value class: Python owns every C++ QShaderDescription::BlockVariable
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QShaderDescription13BlockVariableD1Ev'

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

  class BuiltinVariable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::BuiltinVariable: a plain Python
    object standing in front of one C++ QShaderDescription::BuiltinVariable.

    C++ hands a QShaderDescription::BuiltinVariable around as a copy, so
    every C++ QShaderDescription::BuiltinVariable behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::BuiltinVariable yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::BuiltinVariable::~BuiltinVariable()': the
      destructor: Python removes its C++ QShaderDescription::BuiltinVariable
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QShaderDescription::BuiltinVariable is created at the first
      use, not by 'QShaderDescription::BuiltinVariable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::BuiltinVariable back gives a
      copy the ritual made for Python, in a new cute
      QShaderDescription::BuiltinVariable.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::BuiltinVariable'

    #  Qt's '~QShaderDescription::BuiltinVariable()'. Naming it makes this a
    #  value class: Python owns every C++ QShaderDescription::BuiltinVariable
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QShaderDescription15BuiltinVariableD1Ev'

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

  class InOutVariable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::InOutVariable: a plain Python
    object standing in front of one C++ QShaderDescription::InOutVariable.

    C++ hands a QShaderDescription::InOutVariable around as a copy, so every
    C++ QShaderDescription::InOutVariable behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::InOutVariable yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::InOutVariable::~InOutVariable()': the
      destructor: Python removes its C++ QShaderDescription::InOutVariable by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QShaderDescription::InOutVariable is created at the first use,
      not by 'QShaderDescription::InOutVariable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::InOutVariable back gives a copy
      the ritual made for Python, in a new cute
      QShaderDescription::InOutVariable.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::InOutVariable'

    #  Qt's '~QShaderDescription::InOutVariable()'. Naming it makes this a
    #  value class: Python owns every C++ QShaderDescription::InOutVariable
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QShaderDescription13InOutVariableD1Ev'

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

  class PushConstantBlock(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::PushConstantBlock: a plain
    Python object standing in front of one C++
    QShaderDescription::PushConstantBlock.

    C++ hands a QShaderDescription::PushConstantBlock around as a copy, so
    every C++ QShaderDescription::PushConstantBlock behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::PushConstantBlock yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::PushConstantBlock::~PushConstantBlock()': the
      destructor: Python removes its C++
      QShaderDescription::PushConstantBlock by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QShaderDescription::PushConstantBlock is created at the first
      use, not by 'QShaderDescription::PushConstantBlock(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::PushConstantBlock back gives a
      copy the ritual made for Python, in a new cute
      QShaderDescription::PushConstantBlock.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::PushConstantBlock'

    #  Qt's '~QShaderDescription::PushConstantBlock()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QShaderDescription::PushConstantBlock behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QShaderDescription17PushConstantBlockD1Ev')

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

  class StorageBlock(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::StorageBlock: a plain Python
    object standing in front of one C++ QShaderDescription::StorageBlock.

    C++ hands a QShaderDescription::StorageBlock around as a copy, so every
    C++ QShaderDescription::StorageBlock behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::StorageBlock yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::StorageBlock::~StorageBlock()': the
      destructor: Python removes its C++ QShaderDescription::StorageBlock by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QShaderDescription::StorageBlock is created at the first use,
      not by 'QShaderDescription::StorageBlock(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::StorageBlock back gives a copy
      the ritual made for Python, in a new cute
      QShaderDescription::StorageBlock.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::StorageBlock'

    #  Qt's '~QShaderDescription::StorageBlock()'. Naming it makes this a
    #  value class: Python owns every C++ QShaderDescription::StorageBlock
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QShaderDescription12StorageBlockD1Ev'

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

  class UniformBlock(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShaderDescription::UniformBlock: a plain Python
    object standing in front of one C++ QShaderDescription::UniformBlock.

    C++ hands a QShaderDescription::UniformBlock around as a copy, so every
    C++ QShaderDescription::UniformBlock behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QShaderDescription::UniformBlock yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShaderDescription::UniformBlock::~UniformBlock()': the
      destructor: Python removes its C++ QShaderDescription::UniformBlock by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QShaderDescription::UniformBlock is created at the first use,
      not by 'QShaderDescription::UniformBlock(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShaderDescription::UniformBlock back gives a copy
      the ritual made for Python, in a new cute
      QShaderDescription::UniformBlock.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShaderDescription::UniformBlock'

    #  Qt's '~QShaderDescription::UniformBlock()'. Naming it makes this a
    #  value class: Python owns every C++ QShaderDescription::UniformBlock
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QShaderDescription12UniformBlockD1Ev'

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
  @overload(QDataStream, int)
  @overload(NoneType, int)
  def deserialize(
      stream: Optional[QDataStream],
      version: int,
  ) -> QShaderDescription:
    """
    Calls Qt's 'QShaderDescription
    QShaderDescription::deserialize(QDataStream *stream, int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#deserialize

    Parameters
    ----------

    stream : Optional[QDataStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : int
      Passed on as it is.

    Returns
    -------

    QShaderDescription
      A new cute QShaderDescription around the copy Qt gave back. Python owns
      it.
    """
    #  QShaderDescription QShaderDescription::deserialize(QDataStream
    #      *stream, int version)
    address = Rituals.call(
        'ritual_ZN18QShaderDescription11deserializeEP11QDataStreami',
        CuteMixin._addressOf(stream), version,
    )
    return QShaderDescription._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShaderDescription'

  #  Qt's '~QShaderDescription()'. Naming it makes this a value class: Python
  #  owns every C++ QShaderDescription behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QShaderDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QShaderDescription::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#isValid
    """
    #  bool QShaderDescription::isValid() const
    return self.uglySide.call('ritual_ZNK18QShaderDescription7isValidEv')

  def toJson(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QShaderDescription::toJson() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#toJson

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QShaderDescription::toJson() const
    address = self.uglySide.call('ritual_ZNK18QShaderDescription6toJsonEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tessellationOutputVertexCount(self) -> int:
    """
    Calls Qt's 'uint QShaderDescription::tessellationOutputVertexCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html
    """
    #  uint QShaderDescription::tessellationOutputVertexCount() const
    return self.uglySide.call(
        'ritual_ZNK18QShaderDescription29tessellationOutputVertexCountEv',
    )

  def tessellationMode(self) -> TessellationMode:
    """
    Calls Qt's 'TessellationMode QShaderDescription::tessellationMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#tessellationMode

    Returns
    -------

    TessellationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TessellationMode(number)'
      gives.
    """
    #  TessellationMode QShaderDescription::tessellationMode() const
    return QShaderDescription.TessellationMode(self.uglySide.call(
        'ritual_ZNK18QShaderDescription16tessellationModeEv',
    ))

  def tessellationWindingOrder(self) -> TessellationWindingOrder:
    """
    Calls Qt's 'TessellationWindingOrder
    QShaderDescription::tessellationWindingOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#tessellationWindingOrder

    Returns
    -------

    TessellationWindingOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TessellationWindingOrder(number)' gives.
    """
    #  TessellationWindingOrder
    #      QShaderDescription::tessellationWindingOrder() const
    return QShaderDescription.TessellationWindingOrder(self.uglySide.call(
        'ritual_ZNK18QShaderDescription24tessellationWindingOrderEv',
    ))

  def tessellationPartitioning(self) -> TessellationPartitioning:
    """
    Calls Qt's 'TessellationPartitioning
    QShaderDescription::tessellationPartitioning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#tessellationPartitioning

    Returns
    -------

    TessellationPartitioning
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TessellationPartitioning(number)' gives.
    """
    #  TessellationPartitioning
    #      QShaderDescription::tessellationPartitioning() const
    return QShaderDescription.TessellationPartitioning(self.uglySide.call(
        'ritual_ZNK18QShaderDescription24tessellationPartitioningEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QShaderDescription &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QShaderDescription &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QShaderDescription',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QShaderDescription) -> bool:
    """
    Calls Qt's 'bool operator==(const QShaderDescription &lhs, const
    QShaderDescription &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#operator==

    Parameters
    ----------

    rhs : QShaderDescription
      Passed on as a value: Qt reads the C++ QShaderDescription, which stays
      Python's own.
    """
    #  bool operator==(const QShaderDescription &lhs, const
    #      QShaderDescription &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QShaderDescriptionS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QShaderDescription::QShaderDescription()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#QShaderDescription
    """
    #  QShaderDescription::QShaderDescription()
    self._noteCreation(QShaderDescription, lambda: Rituals.call(
        'ritual_ZN18QShaderDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QShaderDescription) -> None:
    """
    Notes what was given, for Qt's
    'QShaderDescription::QShaderDescription(const QShaderDescription
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qshaderdescription.html#QShaderDescription

    Parameters
    ----------

    other : QShaderDescription
      Passed on as a value: Qt reads the C++ QShaderDescription, which stays
      Python's own.
    """
    #  QShaderDescription::QShaderDescription(const QShaderDescription
    #      &other)
    self._noteCreation(QShaderDescription, lambda: Rituals.call(
        'ritual_ZN18QShaderDescriptionC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QShaderDescription::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#detach
    """
    #  void QShaderDescription::detach()
    self.uglySide.call('ritual_ZN18QShaderDescription6detachEv')

  @overload(QDataStream, int)
  @overload(NoneType, int)
  def serialize(self, stream: Optional[QDataStream], version: int) -> None:
    """
    Calls Qt's 'void QShaderDescription::serialize(QDataStream *stream, int
    version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qshaderdescription.html#serialize

    Parameters
    ----------

    stream : Optional[QDataStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : int
      Passed on as it is.
    """
    #  void QShaderDescription::serialize(QDataStream *stream, int version)
    #      const
    self.uglySide.call(
        'ritual_ZNK18QShaderDescription9serializeEP11QDataStreami',
        self._addressOf(stream), version,
    )

  @staticmethod
  def combinedImageSamplers(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::combinedImageSamplers()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.combinedImageSamplers' has no cute function "
        "yet. Qt's 'QList<InOutVariable> "
        "QShaderDescription::combinedImageSamplers() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def computeShaderLocalSize(*__, **_) -> Never:
    """
    Qt's 'std::array<uint, 3> QShaderDescription::computeShaderLocalSize()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.computeShaderLocalSize' has no cute function "
        "yet. Qt's 'std::array<uint, 3> "
        "QShaderDescription::computeShaderLocalSize() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def inputBuiltinVariables(*__, **_) -> Never:
    """
    Qt's 'QList<BuiltinVariable> QShaderDescription::inputBuiltinVariables()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.inputBuiltinVariables' has no cute function "
        "yet. Qt's 'QList<BuiltinVariable> "
        "QShaderDescription::inputBuiltinVariables() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def inputVariables(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::inputVariables() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.inputVariables' has no cute function yet. Qt's "
        "'QList<InOutVariable> QShaderDescription::inputVariables() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def outputBuiltinVariables(*__, **_) -> Never:
    """
    Qt's 'QList<BuiltinVariable> QShaderDescription::outputBuiltinVariables()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.outputBuiltinVariables' has no cute function "
        "yet. Qt's 'QList<BuiltinVariable> "
        "QShaderDescription::outputBuiltinVariables() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def outputVariables(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::outputVariables() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.outputVariables' has no cute function yet. "
        "Qt's 'QList<InOutVariable> QShaderDescription::outputVariables() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def pushConstantBlocks(*__, **_) -> Never:
    """
    Qt's 'QList<PushConstantBlock> QShaderDescription::pushConstantBlocks()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.pushConstantBlocks' has no cute function yet. "
        "Qt's 'QList<PushConstantBlock> "
        "QShaderDescription::pushConstantBlocks() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def separateImages(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::separateImages() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.separateImages' has no cute function yet. Qt's "
        "'QList<InOutVariable> QShaderDescription::separateImages() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def separateSamplers(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::separateSamplers() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.separateSamplers' has no cute function yet. "
        "Qt's 'QList<InOutVariable> QShaderDescription::separateSamplers() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def storageBlocks(*__, **_) -> Never:
    """
    Qt's 'QList<StorageBlock> QShaderDescription::storageBlocks() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.storageBlocks' has no cute function yet. Qt's "
        "'QList<StorageBlock> QShaderDescription::storageBlocks() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def storageImages(*__, **_) -> Never:
    """
    Qt's 'QList<InOutVariable> QShaderDescription::storageImages() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.storageImages' has no cute function yet. Qt's "
        "'QList<InOutVariable> QShaderDescription::storageImages() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def uniformBlocks(*__, **_) -> Never:
    """
    Qt's 'QList<UniformBlock> QShaderDescription::uniformBlocks() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShaderDescription.uniformBlocks' has no cute function yet. Qt's "
        "'QList<UniformBlock> QShaderDescription::uniformBlocks() const': "
        "gives a type Python has no way to take yet.")
