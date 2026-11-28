"""
DepthMapPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means DepthMapPass to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSSGRenderPass


class DepthMapPass(QSSGRenderPass):
  """
  The cute side of Qt's DepthMapPass: a plain Python object standing in front
  of one C++ DepthMapPass.

  It is built on the cute 'QSSGRenderPass', as Qt's DepthMapPass is built on
  Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a DepthMapPass around as a copy, so every C++ DepthMapPass behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's DepthMapPass that has a ritual and that Python can
  call so far, 4 names in all: 'passType', 'resetForFrame',
  'setMultisamplingEnabled', 'isMultisamplingEnabled'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void DepthMapPass::renderPrep(QSSGRenderer &renderer,
    QSSGLayerRenderData &data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void DepthMapPass::renderPass(QSSGRenderer &renderer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'DepthMapPass::~DepthMapPass()': the destructor: Python removes its
    C++ DepthMapPass by it, and has no other use for it.

  What to expect
  --------------

  - The C++ DepthMapPass is created at the first use, not by
    'DepthMapPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a DepthMapPass back gives a copy the ritual made for
    Python, in a new cute DepthMapPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DepthMapPass'

  #  Qt's '~DepthMapPass()'. Naming it makes this a value class: Python owns
  #  every C++ DepthMapPass behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12DepthMapPassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type DepthMapPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/depthmappass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type DepthMapPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK12DepthMapPass8passTypeEv',
    ))

  def isMultisamplingEnabled(self) -> bool:
    """
    Calls Qt's 'bool DepthMapPass::isMultisamplingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/depthmappass.html#isMultisamplingEnabled
    """
    #  bool DepthMapPass::isMultisamplingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK12DepthMapPass22isMultisamplingEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMultisamplingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void DepthMapPass::setMultisamplingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/depthmappass.html#setMultisamplingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void DepthMapPass::setMultisamplingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN12DepthMapPass23setMultisamplingEnabledEb', enabled,
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
    Calls Qt's 'void DepthMapPass::resetForFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/depthmappass.html#resetForFrame
    """
    #  void DepthMapPass::resetForFrame()
    self.uglySide.call('ritual_ZN12DepthMapPass13resetForFrameEv')
