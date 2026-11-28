"""
QSSGRhiQuadRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiQuadRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhiRenderPassDescriptor, QRhiResourceUpdateBatch
  from ..QtGui import QRhiShaderResourceBindings, QRhiTextureRenderTarget
  from . import QSSGRhiContext, QSSGRhiGraphicsPipelineState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QRhiTextureRenderTarget = WAIT['QRhiTextureRenderTarget']
  QSSGRhiContext = WAIT['QSSGRhiContext']
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiQuadRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiQuadRenderer: a plain Python object standing
  in front of one C++ QSSGRhiQuadRenderer.

  C++ hands a QSSGRhiQuadRenderer around as a copy, so every C++
  QSSGRhiQuadRenderer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiQuadRenderer that has a ritual and that
  Python can call so far, 4 names in all: 'prepareQuad', 'recordRenderQuad',
  'recordRenderQuadPass', 'ensureBuffers'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiQuadRenderer::~QSSGRhiQuadRenderer()': the destructor:
    Python removes its C++ QSSGRhiQuadRenderer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRhiQuadRenderer is created at the first use, not by
    'QSSGRhiQuadRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiQuadRenderer back gives a copy the ritual made
    for Python, in a new cute QSSGRhiQuadRenderer.
  """

  #  The enums Qt writes inside QSSGRhiQuadRenderer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSSGRhiQuadRenderer::Flag' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QSSGRhiQuadRenderer::Flags'.
    """

    UvCoords = 0x1
    DepthTest = 0x2
    DepthWrite = 0x4
    PremulBlend = 0x8
    RenderBehind = 0x10

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiQuadRenderer'

  #  Qt's '~QSSGRhiQuadRenderer()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiQuadRenderer behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGRhiQuadRendererD1Ev'

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
  def prepareQuad(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      maybeRub: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiQuadRenderer::prepareQuad(QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *maybeRub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhiquadrenderer.html#prepareQuad

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maybeRub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiQuadRenderer::prepareQuad(QSSGRhiContext *rhiCtx,
    #      QRhiResourceUpdateBatch *maybeRub)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiQuadRenderer11prepareQuadEP14QSSGRhiContextP23QR'
        'hiResourceUpdateBatch',
        self._addressOf(rhiCtx), self._addressOf(maybeRub),
    )

  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, QRhiRenderPassDescriptor, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, NoneType, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType, NoneType,
      Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings, NoneType, Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, NoneType, QRhiRenderPassDescriptor, Flags,
  )
  @overload(QSSGRhiContext, NoneType, NoneType, NoneType, Flags)
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      NoneType, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiRenderPassDescriptor, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType, NoneType, Flags,
  )
  @overload(
      NoneType, NoneType, QRhiShaderResourceBindings,
      QRhiRenderPassDescriptor, Flags,
  )
  @overload(NoneType, NoneType, QRhiShaderResourceBindings, NoneType, Flags)
  @overload(NoneType, NoneType, NoneType, QRhiRenderPassDescriptor, Flags)
  @overload(NoneType, NoneType, NoneType, NoneType, Flags)
  def recordRenderQuad(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      ps: Optional[QSSGRhiGraphicsPipelineState],
      srb: Optional[QRhiShaderResourceBindings],
      rpDesc: Optional[QRhiRenderPassDescriptor],
      flags: Flags,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiQuadRenderer::recordRenderQuad(QSSGRhiContext
    *rhiCtx, QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings
    *srb, QRhiRenderPassDescriptor *rpDesc, Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhiquadrenderer.html#recordRenderQuad

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

    flags : Flags
      Passed on as its number.
    """
    #  void QSSGRhiQuadRenderer::recordRenderQuad(QSSGRhiContext *rhiCtx,
    #      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
    #      QRhiRenderPassDescriptor *rpDesc, Flags flags)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiQuadRenderer16recordRenderQuadEP14QSSGRhiContext'
        'P28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP24QRh'
        'iRenderPassDescriptor6QFlagsINS_4FlagEE',
        self._addressOf(rhiCtx), self._addressOf(ps), self._addressOf(srb),
        self._addressOf(rpDesc), flags.value,
    )

  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, QRhiTextureRenderTarget, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState,
      QRhiShaderResourceBindings, NoneType, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiTextureRenderTarget, Flags,
  )
  @overload(
      QSSGRhiContext, QSSGRhiGraphicsPipelineState, NoneType, NoneType,
      Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings,
      QRhiTextureRenderTarget, Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, QRhiShaderResourceBindings, NoneType, Flags,
  )
  @overload(
      QSSGRhiContext, NoneType, NoneType, QRhiTextureRenderTarget, Flags,
  )
  @overload(QSSGRhiContext, NoneType, NoneType, NoneType, Flags)
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      QRhiTextureRenderTarget, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, QRhiShaderResourceBindings,
      NoneType, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType,
      QRhiTextureRenderTarget, Flags,
  )
  @overload(
      NoneType, QSSGRhiGraphicsPipelineState, NoneType, NoneType, Flags,
  )
  @overload(
      NoneType, NoneType, QRhiShaderResourceBindings,
      QRhiTextureRenderTarget, Flags,
  )
  @overload(NoneType, NoneType, QRhiShaderResourceBindings, NoneType, Flags)
  @overload(NoneType, NoneType, NoneType, QRhiTextureRenderTarget, Flags)
  @overload(NoneType, NoneType, NoneType, NoneType, Flags)
  def recordRenderQuadPass(
      self,
      rhiCtx: Optional[QSSGRhiContext],
      ps: Optional[QSSGRhiGraphicsPipelineState],
      srb: Optional[QRhiShaderResourceBindings],
      rt: Optional[QRhiTextureRenderTarget],
      flags: Flags,
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiQuadRenderer::recordRenderQuadPass(QSSGRhiContext
    *rhiCtx, QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings
    *srb, QRhiTextureRenderTarget *rt, Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhiquadrenderer.html#recordRenderQuadPass

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

    rt : Optional[QRhiTextureRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Flags
      Passed on as its number.
    """
    #  void QSSGRhiQuadRenderer::recordRenderQuadPass(QSSGRhiContext *rhiCtx,
    #      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
    #      QRhiTextureRenderTarget *rt, Flags flags)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiQuadRenderer20recordRenderQuadPassEP14QSSGRhiCon'
        'textP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP2'
        '3QRhiTextureRenderTarget6QFlagsINS_4FlagEE',
        self._addressOf(rhiCtx), self._addressOf(ps), self._addressOf(srb),
        self._addressOf(rt), flags.value,
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
    Calls Qt's 'void QSSGRhiQuadRenderer::ensureBuffers(QSSGRhiContext
    *rhiCtx, QRhiResourceUpdateBatch *rub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhiquadrenderer.html#ensureBuffers

    Parameters
    ----------

    rhiCtx : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiQuadRenderer::ensureBuffers(QSSGRhiContext *rhiCtx,
    #      QRhiResourceUpdateBatch *rub)
    self.uglySide.call(
        'ritual_ZN19QSSGRhiQuadRenderer13ensureBuffersEP14QSSGRhiContextP23'
        'QRhiResourceUpdateBatch',
        self._addressOf(rhiCtx), self._addressOf(rub),
    )
