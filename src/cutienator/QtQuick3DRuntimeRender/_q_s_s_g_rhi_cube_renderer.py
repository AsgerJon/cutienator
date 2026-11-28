"""
QSSGRhiCubeRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiCubeRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSSGRhiQuadRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiRenderPassDescriptor, QRhiResourceUpdateBatch
  from ..QtGui import QRhiShaderResourceBindings
  from . import QSSGRhiContext, QSSGRhiGraphicsPipelineState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QSSGRhiContext = WAIT['QSSGRhiContext']
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiCubeRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiCubeRenderer: a plain Python object standing
  in front of one C++ QSSGRhiCubeRenderer.

  C++ hands a QSSGRhiCubeRenderer around as a copy, so every C++
  QSSGRhiCubeRenderer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiCubeRenderer that has a ritual and that
  Python can call so far, 3 names in all: 'prepareCube', 'recordRenderCube',
  'ensureBuffers'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiCubeRenderer::~QSSGRhiCubeRenderer()': the destructor:
    Python removes its C++ QSSGRhiCubeRenderer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRhiCubeRenderer is created at the first use, not by
    'QSSGRhiCubeRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiCubeRenderer back gives a copy the ritual made
    for Python, in a new cute QSSGRhiCubeRenderer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiCubeRenderer'

  #  Qt's '~QSSGRhiCubeRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiCubeRenderer behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRhiCubeRendererD1Ev'

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

  @overload(QSSGRhiContext, QRhiResourceUpdateBatch)
  @overload(QSSGRhiContext, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def prepareCube(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      maybeRub: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiCubeRenderer::prepareCube(QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *maybeRub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicuberenderer.html#prepareCube

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maybeRub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiCubeRenderer::prepareCube(QSSGRhiContext *rhiCtx,
    #      QRhiResourceUpdateBatch *maybeRub)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiCubeRenderer11prepareCubeEP14QSSGRhiContextP23QR'
        'hiResourceUpdateBatch',
        self._addressOf(rhiCtx), self._addressOf(maybeRub),
    )

  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, QRhiRenderPassDescriptor,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, NoneType, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType, NoneType,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings, NoneType,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, NoneType, QRhiRenderPassDescriptor,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, NoneType, NoneType,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      NoneType, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType, NoneType,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, NoneType, QRhiShaderResourceBindings, NoneType,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, NoneType, NoneType, QRhiRenderPassDescriptor,
      QSSGRhiQuadRenderer.Flags,
  )
  @overload(
      NoneType, NoneType, NoneType, NoneType, QSSGRhiQuadRenderer.Flags,
  )
  def recordRenderCube(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      ps: Optional[QSSGRhiGraphicsPipelineState],
      srb: Optional[QRhiShaderResourceBindings],
      rpDesc: Optional[QRhiRenderPassDescriptor],
      flags: QSSGRhiQuadRenderer.Flags,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiCubeRenderer::recordRenderCube(QSSGRhiContext
    *rhiCtx, QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings
    *srb, QRhiRenderPassDescriptor *rpDesc, QSSGRhiQuadRenderer::Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicuberenderer.html#recordRenderCube

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ps : Optional[QSSGRhiGraphicsPipelineState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QSSGRhiQuadRenderer.Flags
      Passed on as its number.
    """
    #  void QSSGRhiCubeRenderer::recordRenderCube(QSSGRhiContext *rhiCtx,
    #      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
    #      QRhiRenderPassDescriptor *rpDesc, QSSGRhiQuadRenderer::Flags
    #      flags)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiCubeRenderer16recordRenderCubeEP14QSSGRhiContext'
        'P28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP24QRh'
        'iRenderPassDescriptor6QFlagsIN19QSSGRhiQuadRenderer4FlagEE',
        self._addressOf(rhiCtx), self._addressOf(ps), self._addressOf(srb),
        self._addressOf(rpDesc), flags.value,
    )

  @overload(QSSGRhiContext, QRhiResourceUpdateBatch)
  @overload(QSSGRhiContext, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def ensureBuffers(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      rub: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiCubeRenderer::ensureBuffers(QSSGRhiContext
    *rhiCtx, QRhiResourceUpdateBatch *rub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicuberenderer.html#ensureBuffers

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiCubeRenderer::ensureBuffers(QSSGRhiContext *rhiCtx,
    #      QRhiResourceUpdateBatch *rub)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiCubeRenderer13ensureBuffersEP14QSSGRhiContextP23'
        'QRhiResourceUpdateBatch',
        self._addressOf(rhiCtx), self._addressOf(rub),
    )
