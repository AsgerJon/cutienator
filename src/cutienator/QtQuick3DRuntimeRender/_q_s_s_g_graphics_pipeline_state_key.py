"""
QSSGGraphicsPipelineStateKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGGraphicsPipelineStateKey to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiRenderPassDescriptor, QRhiShaderResourceBindings
  from . import QSSGRhiGraphicsPipelineState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGGraphicsPipelineStateKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGGraphicsPipelineStateKey: a plain Python object
  standing in front of one C++ QSSGGraphicsPipelineStateKey.

  C++ hands a QSSGGraphicsPipelineStateKey around as a copy, so every C++
  QSSGGraphicsPipelineStateKey behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGGraphicsPipelineStateKey that has a ritual and
  that Python can call so far, 1 name in all: 'create'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGGraphicsPipelineStateKey::~QSSGGraphicsPipelineStateKey()': the
    destructor: Python removes its C++ QSSGGraphicsPipelineStateKey by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGGraphicsPipelineStateKey is created at the first use, not by
    'QSSGGraphicsPipelineStateKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGGraphicsPipelineStateKey back gives a copy the
    ritual made for Python, in a new cute QSSGGraphicsPipelineStateKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QSSGRhiGraphicsPipelineState, QRhiRenderPassDescriptor,
      QRhiShaderResourceBindings,
  )
  @overload(QSSGRhiGraphicsPipelineState, QRhiRenderPassDescriptor, NoneType)
  @overload(
      QSSGRhiGraphicsPipelineState, NoneType, QRhiShaderResourceBindings,
  )
  @overload(QSSGRhiGraphicsPipelineState, NoneType, NoneType)
  def create(
      state: QSSGRhiGraphicsPipelineState,
      rpDesc: Optional[QRhiRenderPassDescriptor],
      srb: Optional[QRhiShaderResourceBindings],
  ) -> QSSGGraphicsPipelineStateKey:
    """
    Calls Qt's 'QSSGGraphicsPipelineStateKey
    QSSGGraphicsPipelineStateKey::create(const QSSGRhiGraphicsPipelineState
    &state, const QRhiRenderPassDescriptor *rpDesc, const
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssggraphicspipelinestatekey.html#create

    Parameters
    ----------

    state : QSSGRhiGraphicsPipelineState
      Passed on as a value: Qt reads the C++ QSSGRhiGraphicsPipelineState,
      which stays Python's own.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSSGGraphicsPipelineStateKey
      A new cute QSSGGraphicsPipelineStateKey around the copy Qt gave back.
      Python owns it.
    """
    #  QSSGGraphicsPipelineStateKey
    #      QSSGGraphicsPipelineStateKey::create(const
    #      QSSGRhiGraphicsPipelineState &state, const
    #      QRhiRenderPassDescriptor *rpDesc, const QRhiShaderResourceBindings
    #      *srb)
    address = Rituals.call(
        'ritual_ZN28QSSGGraphicsPipelineStateKey6createERK28QSSGRhiGraphics'
        'PipelineStatePK24QRhiRenderPassDescriptorPK26QRhiShaderResourceBin'
        'dings',
        CuteMixin._valueOf(state), CuteMixin._addressOf(rpDesc),
        CuteMixin._addressOf(srb),
    )
    return QSSGGraphicsPipelineStateKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGGraphicsPipelineStateKey'

  #  Qt's '~QSSGGraphicsPipelineStateKey()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGGraphicsPipelineStateKey behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QSSGGraphicsPipelineStateKeyD1Ev'

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
