"""
SkyboxCubeMapPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SkyboxCubeMapPass to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSSGRenderPass


class SkyboxCubeMapPass(QSSGRenderPass):
  """
  The cute side of Qt's SkyboxCubeMapPass: a plain Python object standing in
  front of one C++ SkyboxCubeMapPass.

  It is built on the cute 'QSSGRenderPass', as Qt's SkyboxCubeMapPass is
  built on Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a SkyboxCubeMapPass around as a copy, so every C++
  SkyboxCubeMapPass behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's SkyboxCubeMapPass that has a ritual and that Python
  can call so far, 2 names in all: 'passType', 'resetForFrame'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SkyboxCubeMapPass::~SkyboxCubeMapPass()': the destructor: Python
    removes its C++ SkyboxCubeMapPass by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ SkyboxCubeMapPass is created at the first use, not by
    'SkyboxCubeMapPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a SkyboxCubeMapPass back gives a copy the ritual made
    for Python, in a new cute SkyboxCubeMapPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SkyboxCubeMapPass'

  #  Qt's '~SkyboxCubeMapPass()'. Naming it makes this a value class: Python
  #  owns every C++ SkyboxCubeMapPass behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17SkyboxCubeMapPassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type SkyboxCubeMapPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/skyboxcubemappass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type SkyboxCubeMapPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK17SkyboxCubeMapPass8passTypeEv',
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

  def resetForFrame(self) -> None:
    """
    Calls Qt's 'void SkyboxCubeMapPass::resetForFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/skyboxcubemappass.html#resetForFrame
    """
    #  void SkyboxCubeMapPass::resetForFrame()
    self.uglySide.call('ritual_ZN17SkyboxCubeMapPass13resetForFrameEv')
