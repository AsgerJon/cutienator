"""
TransparentPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means TransparentPass to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSSGRenderPass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class TransparentPass(QSSGRenderPass):
  """
  The cute side of Qt's TransparentPass: a plain Python object standing in
  front of one C++ TransparentPass.

  It is built on the cute 'QSSGRenderPass', as Qt's TransparentPass is built
  on Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a TransparentPass around as a copy, so every C++ TransparentPass
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's TransparentPass that has a ritual and that Python
  can call so far, 2 names in all: 'passType', 'resetForFrame'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void TransparentPass::prep(const QSSGRenderContextInterface &ctx,
    QSSGLayerRenderData &data, QSSGPassKey passKey,
    QSSGRhiGraphicsPipelineState &ps, QSSGShaderFeatures shaderFeatures,
    QRhiRenderPassDescriptor *rpDesc, const QSSGRenderableObjectList
    &sortedTransparentObjects, bool oit)': takes a type Python has no way to
    hand over yet.
  - Qt's 'TransparentPass::~TransparentPass()': the destructor: Python
    removes its C++ TransparentPass by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ TransparentPass is created at the first use, not by
    'TransparentPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a TransparentPass back gives a copy the ritual made for
    Python, in a new cute TransparentPass.
  - Each name of Qt's TransparentPass that has no cute function yet, 'prep',
    'render', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TransparentPass'

  #  Qt's '~TransparentPass()'. Naming it makes this a value class: Python
  #  owns every C++ TransparentPass behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15TransparentPassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type TransparentPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/transparentpass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type TransparentPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK15TransparentPass8passTypeEv',
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
    Calls Qt's 'void TransparentPass::resetForFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/transparentpass.html#resetForFrame
    """
    #  void TransparentPass::resetForFrame()
    self.uglySide.call('ritual_ZN15TransparentPass13resetForFrameEv')

  @staticmethod
  def prep(*__, **_) -> Never:
    """
    Qt's 'void TransparentPass::prep(const QSSGRenderContextInterface &ctx,
    QSSGLayerRenderData &data, QSSGPassKey passKey,
    QSSGRhiGraphicsPipelineState &ps, QSSGShaderFeatures shaderFeatures,
    QRhiRenderPassDescriptor *rpDesc, const QSSGRenderableObjectList
    &sortedTransparentObjects, bool oit)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'TransparentPass.prep' has no cute function yet. Qt's 'void "
        "TransparentPass::prep(const QSSGRenderContextInterface &ctx, "
        "QSSGLayerRenderData &data, QSSGPassKey passKey, "
        "QSSGRhiGraphicsPipelineState &ps, QSSGShaderFeatures "
        "shaderFeatures, QRhiRenderPassDescriptor *rpDesc, const "
        "QSSGRenderableObjectList &sortedTransparentObjects, bool oit)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void TransparentPass::render(const QSSGRenderContextInterface &ctx,
    const QSSGRhiGraphicsPipelineState &ps, const QSSGRenderableObjectList
    &sortedTransparentObjects)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'const QSSGRenderContextInterface'.
    """
    raise NotImplementedError(
        "'TransparentPass.render' has no cute function yet. Qt's 'void "
        "TransparentPass::render(const QSSGRenderContextInterface &ctx, "
        "const QSSGRhiGraphicsPipelineState &ps, const "
        "QSSGRenderableObjectList &sortedTransparentObjects)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QSSGRenderContextInterface'.")
