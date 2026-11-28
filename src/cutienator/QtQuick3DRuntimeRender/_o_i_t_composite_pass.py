"""
OITCompositePass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means OITCompositePass to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSSGRenderLayer, QSSGRenderPass


class OITCompositePass(QSSGRenderPass):
  """
  The cute side of Qt's OITCompositePass: a plain Python object standing in
  front of one C++ OITCompositePass.

  It is built on the cute 'QSSGRenderPass', as Qt's OITCompositePass is built
  on Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a OITCompositePass around as a copy, so every C++
  OITCompositePass behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's OITCompositePass that has a ritual and that Python
  can call so far, 3 names in all: 'passType', 'resetForFrame', 'setMethod'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'OITCompositePass::~OITCompositePass()': the destructor: Python
    removes its C++ OITCompositePass by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ OITCompositePass is created at the first use, not by
    'OITCompositePass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a OITCompositePass back gives a copy the ritual made
    for Python, in a new cute OITCompositePass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'OITCompositePass'

  #  Qt's '~OITCompositePass()'. Naming it makes this a value class: Python
  #  owns every C++ OITCompositePass behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16OITCompositePassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type OITCompositePass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/oitcompositepass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type OITCompositePass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK16OITCompositePass8passTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRenderLayer.OITMethod)
  def setMethod(self, m: QSSGRenderLayer.OITMethod) -> None:
    """
    Calls Qt's 'void OITCompositePass::setMethod(QSSGRenderLayer::OITMethod
    m)'.

    Qt's own words: https://doc.qt.io/qt-6/oitcompositepass.html#setMethod

    Parameters
    ----------

    m : QSSGRenderLayer.OITMethod
      Passed on as its number.
    """
    #  void OITCompositePass::setMethod(QSSGRenderLayer::OITMethod m)
    self.uglySide.call(
        'ritual_ZN16OITCompositePass9setMethodEN15QSSGRenderLayer9OITMethod'
        'E',
        m.value,
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
    Calls Qt's 'void OITCompositePass::resetForFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/oitcompositepass.html#resetForFrame
    """
    #  void OITCompositePass::resetForFrame()
    self.uglySide.call('ritual_ZN16OITCompositePass13resetForFrameEv')
