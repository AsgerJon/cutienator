"""
OITRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means OITRenderPass to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSSGRenderLayer, QSSGRenderPass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class OITRenderPass(QSSGRenderPass):
  """
  The cute side of Qt's OITRenderPass: a plain Python object standing in
  front of one C++ OITRenderPass.

  It is built on the cute 'QSSGRenderPass', as Qt's OITRenderPass is built on
  Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a OITRenderPass around as a copy, so every C++ OITRenderPass
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's OITRenderPass that has a ritual and that Python can
  call so far, 4 names in all: 'passType', 'resetForFrame', 'setMethod',
  'linkedListRequiresResize'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'OITRenderPass::~OITRenderPass()': the destructor: Python removes
    its C++ OITRenderPass by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ OITRenderPass is created at the first use, not by
    'OITRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a OITRenderPass back gives a copy the ritual made for
    Python, in a new cute OITRenderPass.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'OITRenderPass'

  #  Qt's '~OITRenderPass()'. Naming it makes this a value class: Python owns
  #  every C++ OITRenderPass behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13OITRenderPassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type OITRenderPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/oitrenderpass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type OITRenderPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK13OITRenderPass8passTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRenderLayer.OITMethod)
  def setMethod(self, m: QSSGRenderLayer.OITMethod) -> None:
    """
    Calls Qt's 'void OITRenderPass::setMethod(QSSGRenderLayer::OITMethod m)'.

    Qt's own words: https://doc.qt.io/qt-6/oitrenderpass.html#setMethod

    Parameters
    ----------

    m : QSSGRenderLayer.OITMethod
      Passed on as its number.
    """
    #  void OITRenderPass::setMethod(QSSGRenderLayer::OITMethod m)
    self.uglySide.call(
        'ritual_ZN13OITRenderPass9setMethodEN15QSSGRenderLayer9OITMethodE',
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
    Calls Qt's 'void OITRenderPass::resetForFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/oitrenderpass.html#resetForFrame
    """
    #  void OITRenderPass::resetForFrame()
    self.uglySide.call('ritual_ZN13OITRenderPass13resetForFrameEv')

  @overload(QSize)
  def linkedListRequiresResize(self, dim: QSize) -> bool:
    """
    Calls Qt's 'bool OITRenderPass::linkedListRequiresResize(QSize dim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/oitrenderpass.html#linkedListRequiresResize

    Parameters
    ----------

    dim : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool OITRenderPass::linkedListRequiresResize(QSize dim)
    return self.uglySide.call(
        'ritual_ZN13OITRenderPass24linkedListRequiresResizeE5QSize',
        self._valueOf(dim),
    )
