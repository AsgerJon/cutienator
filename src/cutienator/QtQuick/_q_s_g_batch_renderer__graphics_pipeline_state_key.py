"""
QSGBatchRenderer::GraphicsPipelineStateKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::GraphicsPipelineStateKey to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSGBatchRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiRenderPassDescriptor, QRhiShaderResourceBindings
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GraphicsPipelineStateKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::GraphicsPipelineStateKey: a plain
  Python object standing in front of one C++
  QSGBatchRenderer::GraphicsPipelineStateKey.

  C++ hands a QSGBatchRenderer::GraphicsPipelineStateKey around as a copy, so
  every C++ QSGBatchRenderer::GraphicsPipelineStateKey behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::GraphicsPipelineStateKey that has
  a ritual and that Python can call so far, 1 name in all: 'create'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSGBatchRenderer::GraphicsPipelineStateKey::~GraphicsPipelineStateKey(
    )': the destructor: Python removes its C++
    QSGBatchRenderer::GraphicsPipelineStateKey by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::GraphicsPipelineStateKey is created at the
    first use, not by 'QSGBatchRenderer::GraphicsPipelineStateKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGBatchRenderer::GraphicsPipelineStateKey back gives
    a copy the ritual made for Python, in a new cute
    QSGBatchRenderer::GraphicsPipelineStateKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'],
      WAIT['QSGBatchRenderer.ShaderManagerShader'], QRhiRenderPassDescriptor,
      QRhiShaderResourceBindings,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'],
      WAIT['QSGBatchRenderer.ShaderManagerShader'], QRhiRenderPassDescriptor,
      NoneType,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'],
      WAIT['QSGBatchRenderer.ShaderManagerShader'], NoneType,
      QRhiShaderResourceBindings,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'],
      WAIT['QSGBatchRenderer.ShaderManagerShader'], NoneType, NoneType,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'], NoneType,
      QRhiRenderPassDescriptor, QRhiShaderResourceBindings,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'], NoneType,
      QRhiRenderPassDescriptor, NoneType,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'], NoneType, NoneType,
      QRhiShaderResourceBindings,
  )
  @overload(
      WAIT['QSGBatchRenderer.GraphicsState'], NoneType, NoneType, NoneType,
  )
  def create(
      state: QSGBatchRenderer.GraphicsState,
      sms: Optional[QSGBatchRenderer.ShaderManagerShader],
      rpDesc: Optional[QRhiRenderPassDescriptor],
      srb: Optional[QRhiShaderResourceBindings],
  ) -> GraphicsPipelineStateKey:
    """
    Calls Qt's 'GraphicsPipelineStateKey
    QSGBatchRenderer::GraphicsPipelineStateKey::create(const GraphicsState
    &state, const ShaderManagerShader *sms, const QRhiRenderPassDescriptor
    *rpDesc, const QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-graphicspipelinestatekey.html

    Parameters
    ----------

    state : QSGBatchRenderer.GraphicsState
      Passed on as a value: Qt reads the C++ QSGBatchRenderer::GraphicsState,
      which stays Python's own.

    sms : Optional[QSGBatchRenderer.ShaderManagerShader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    GraphicsPipelineStateKey
      A new cute QSGBatchRenderer::GraphicsPipelineStateKey around the copy
      Qt gave back. Python owns it.
    """
    #  GraphicsPipelineStateKey
    #      QSGBatchRenderer::GraphicsPipelineStateKey::create(const
    #      GraphicsState &state, const ShaderManagerShader *sms, const
    #      QRhiRenderPassDescriptor *rpDesc, const QRhiShaderResourceBindings
    #      *srb)
    address = Rituals.call(
        'ritual_ZN16QSGBatchRenderer24GraphicsPipelineStateKey6createERKNS_'
        '13GraphicsStateEPKNS_19ShaderManagerShaderEPK24QRhiRenderPassDescr'
        'iptorPK26QRhiShaderResourceBindings',
        CuteMixin._valueOf(state), CuteMixin._addressOf(sms),
        CuteMixin._addressOf(rpDesc), CuteMixin._addressOf(srb),
    )
    return GraphicsPipelineStateKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::GraphicsPipelineStateKey'

  #  Qt's '~QSGBatchRenderer::GraphicsPipelineStateKey()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QSGBatchRenderer::GraphicsPipelineStateKey behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN16QSGBatchRenderer24GraphicsPipelineStateKeyD1Ev')

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
