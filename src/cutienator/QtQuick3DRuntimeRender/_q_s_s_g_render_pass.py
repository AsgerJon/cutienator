"""
QSSGRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderPass to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderPass(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderPass: a plain Python object standing in
  front of one C++ QSSGRenderPass.

  What exists
  -----------

  Every function of Qt's QSSGRenderPass that has a ritual and that Python can
  call so far, 2 names in all: 'passType', 'resetForFrame'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderPass::~QSSGRenderPass()': the destructor: Python never
    removes a C++ QSSGRenderPass.
  - Qt's 'void QSSGRenderPass::renderPrep(QSSGRenderer &renderer,
    QSSGLayerRenderData &data)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QSSGRenderPass::renderPass(QSSGRenderer &renderer)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGRenderPass is created at the first use, not by
    'QSSGRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderPass.
  - Each name of Qt's QSSGRenderPass that has no cute function yet,
    'renderPass', 'renderPrep', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderPass, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderPass::Type' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Standalone = Kee[int](0)
    Main = Kee[int](1)
    Extension = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderPass'

  #  A C++ QSSGRenderPass Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGRenderPass'

  #  The functions Qt calls itself that QSSGRenderPass is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'renderPrep': (
          'void QSSGRenderPass::renderPrep(QSSGRenderer &, '
          'QSSGLayerRenderData &)',
      ),
      'renderPass': (
          'void QSSGRenderPass::renderPass(QSSGRenderer &)',
      ),
  }

  #  The functions Qt calls itself that QSSGRenderPass is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'passType': (
          ('_ZNK14QSSGRenderPass8passTypeEv',
           ('int', 'enum', 'QtQuick3DRuntimeRender:QSSGRenderPass.Type'),
           ()),
      ),
      'resetForFrame': (
          ('_ZN14QSSGRenderPass13resetForFrameEv',
           ('nothing', 'nothing', ''),
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

  def passType(self) -> Type:
    """
    Calls Qt's 'Type QSSGRenderPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpass.html#passType

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSSGRenderPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK14QSSGRenderPass8passTypeEv',
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
    Calls Qt's 'void QSSGRenderPass::resetForFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderpass.html#resetForFrame
    """
    #  void QSSGRenderPass::resetForFrame()
    self.uglySide.call('ritual_ZN14QSSGRenderPass13resetForFrameEv')

  @staticmethod
  def renderPass(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderPass::renderPass(QSSGRenderer &renderer)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderPass.renderPass' has no cute function yet. Qt's 'void "
        "QSSGRenderPass::renderPass(QSSGRenderer &renderer)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def renderPrep(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderPass::renderPrep(QSSGRenderer &renderer,
    QSSGLayerRenderData &data)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSSGRenderPass.renderPrep' has no cute function yet. Qt's 'void "
        "QSSGRenderPass::renderPrep(QSSGRenderer &renderer, "
        "QSSGLayerRenderData &data)': takes a type Python has no way to "
        "hand over yet.")
