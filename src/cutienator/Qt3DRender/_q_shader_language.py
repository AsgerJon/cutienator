"""
QShaderLanguage stands for the namespace 'QShaderLanguage' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QShaderLanguage:
  """
  The namespace 'QShaderLanguage' of Qt, which holds no objects. It holds the
  2 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class StorageQualifier(CuteNum):
    """
    The enum 'QShaderLanguage::StorageQualifier' of Qt, with the 5 names Qt
    gives in it.
    """

    Const = Kee[int](1)
    Input = Kee[int](2)
    BuiltIn = Kee[int](3)
    Output = Kee[int](4)
    Uniform = Kee[int](5)

  class VariableType(CuteNum):
    """
    The enum 'QShaderLanguage::VariableType' of Qt, with the 84 names Qt
    gives in it.
    """

    Bool = Kee[int](1)
    Int = Kee[int](2)
    Uint = Kee[int](3)
    Float = Kee[int](4)
    Double = Kee[int](5)
    Vec2 = Kee[int](6)
    Vec3 = Kee[int](7)
    Vec4 = Kee[int](8)
    DVec2 = Kee[int](9)
    DVec3 = Kee[int](10)
    DVec4 = Kee[int](11)
    BVec2 = Kee[int](12)
    BVec3 = Kee[int](13)
    BVec4 = Kee[int](14)
    IVec2 = Kee[int](15)
    IVec3 = Kee[int](16)
    IVec4 = Kee[int](17)
    UVec2 = Kee[int](18)
    UVec3 = Kee[int](19)
    UVec4 = Kee[int](20)
    Mat2 = Kee[int](21)
    Mat3 = Kee[int](22)
    Mat4 = Kee[int](23)
    Mat2x2 = Kee[int](24)
    Mat2x3 = Kee[int](25)
    Mat2x4 = Kee[int](26)
    Mat3x2 = Kee[int](27)
    Mat3x3 = Kee[int](28)
    Mat3x4 = Kee[int](29)
    Mat4x2 = Kee[int](30)
    Mat4x3 = Kee[int](31)
    Mat4x4 = Kee[int](32)
    DMat2 = Kee[int](33)
    DMat3 = Kee[int](34)
    DMat4 = Kee[int](35)
    DMat2x2 = Kee[int](36)
    DMat2x3 = Kee[int](37)
    DMat2x4 = Kee[int](38)
    DMat3x2 = Kee[int](39)
    DMat3x3 = Kee[int](40)
    DMat3x4 = Kee[int](41)
    DMat4x2 = Kee[int](42)
    DMat4x3 = Kee[int](43)
    DMat4x4 = Kee[int](44)
    Sampler1D = Kee[int](45)
    Sampler2D = Kee[int](46)
    Sampler3D = Kee[int](47)
    SamplerCube = Kee[int](48)
    Sampler2DRect = Kee[int](49)
    Sampler2DMs = Kee[int](50)
    SamplerBuffer = Kee[int](51)
    Sampler1DArray = Kee[int](52)
    Sampler2DArray = Kee[int](53)
    Sampler2DMsArray = Kee[int](54)
    SamplerCubeArray = Kee[int](55)
    Sampler1DShadow = Kee[int](56)
    Sampler2DShadow = Kee[int](57)
    Sampler2DRectShadow = Kee[int](58)
    Sampler1DArrayShadow = Kee[int](59)
    Sampler2DArrayShadow = Kee[int](60)
    SamplerCubeShadow = Kee[int](61)
    SamplerCubeArrayShadow = Kee[int](62)
    ISampler1D = Kee[int](63)
    ISampler2D = Kee[int](64)
    ISampler3D = Kee[int](65)
    ISamplerCube = Kee[int](66)
    ISampler2DRect = Kee[int](67)
    ISampler2DMs = Kee[int](68)
    ISamplerBuffer = Kee[int](69)
    ISampler1DArray = Kee[int](70)
    ISampler2DArray = Kee[int](71)
    ISampler2DMsArray = Kee[int](72)
    ISamplerCubeArray = Kee[int](73)
    USampler1D = Kee[int](74)
    USampler2D = Kee[int](75)
    USampler3D = Kee[int](76)
    USamplerCube = Kee[int](77)
    USampler2DRect = Kee[int](78)
    USampler2DMs = Kee[int](79)
    USamplerBuffer = Kee[int](80)
    USampler1DArray = Kee[int](81)
    USampler2DArray = Kee[int](82)
    USampler2DMsArray = Kee[int](83)
    USamplerCubeArray = Kee[int](84)
