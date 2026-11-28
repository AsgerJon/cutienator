"""
QSSGCustomShaderMetaData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderlibrarymanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGCustomShaderMetaData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, CuteFlags, MetaCute


class QSSGCustomShaderMetaData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGCustomShaderMetaData: a plain Python object
  standing in front of one C++ QSSGCustomShaderMetaData.

  C++ hands a QSSGCustomShaderMetaData around as a copy, so every C++
  QSSGCustomShaderMetaData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGCustomShaderMetaData yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGCustomShaderMetaData::~QSSGCustomShaderMetaData()': the
    destructor: Python removes its C++ QSSGCustomShaderMetaData by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGCustomShaderMetaData is created at the first use, not by
    'QSSGCustomShaderMetaData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGCustomShaderMetaData back gives a copy the ritual
    made for Python, in a new cute QSSGCustomShaderMetaData.
  """

  #  The enums Qt writes inside QSSGCustomShaderMetaData, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSSGCustomShaderMetaData::Flag' of Qt, with the 22 names
    Qt gives in it. Qt names the type of its combinations
    'QSSGCustomShaderMetaData::Flags'.
    """

    UsesScreenTexture = 0x1
    UsesDepthTexture = 0x2
    UsesAoTexture = 0x4
    OverridesPosition = 0x8
    UsesProjectionMatrix = 0x10
    UsesInverseProjectionMatrix = 0x20
    UsesScreenMipTexture = 0x40
    UsesVarColor = 0x80
    UsesSharedVars = 0x100
    UsesIblOrientation = 0x200
    UsesLightmap = 0x400
    UsesSkinning = 0x800
    UsesMorphing = 0x1000
    UsesViewIndex = 0x2000
    UsesInputTexture = 0x4000
    UsesClearcoat = 0x8000
    UsesClearcoatFresnelScaleBias = 0x10000
    UsesFresnelScaleBias = 0x20000
    UsesTransmission = 0x40000
    UsesViewMatrix = 0x80000
    UsesNormalTexture = 0x100000
    UsesMotionVectorTexture = 0x200000

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGCustomShaderMetaData'

  #  Qt's '~QSSGCustomShaderMetaData()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGCustomShaderMetaData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSSGCustomShaderMetaDataD1Ev'

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
