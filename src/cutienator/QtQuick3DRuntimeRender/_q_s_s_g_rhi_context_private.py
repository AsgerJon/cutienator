"""
QSSGRhiContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRhiContextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiCommandBuffer, QRhiComputePipeline
  from ..QtGui import QRhiGraphicsPipeline, QRhiRenderPassDescriptor
  from ..QtGui import QRhiRenderTarget, QRhiShaderResourceBindings
  from ..QtGui import QRhiTexture, QShader
  from . import QSSGComputePipelineStateKey, QSSGGraphicsPipelineStateKey
  from . import QSSGRenderInstanceTable, QSSGRenderMesh, QSSGRenderModel
  from . import QSSGRhiContext, QSSGRhiGraphicsPipelineState
  from . import QSSGRhiShaderResourceBindingList
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiRenderPassDescriptor = WAIT['QRhiRenderPassDescriptor']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QRhiShaderResourceBindings = WAIT['QRhiShaderResourceBindings']
  QRhiTexture = WAIT['QRhiTexture']
  QSSGComputePipelineStateKey = WAIT['QSSGComputePipelineStateKey']
  QSSGGraphicsPipelineStateKey = WAIT['QSSGGraphicsPipelineStateKey']
  QSSGRenderInstanceTable = WAIT['QSSGRenderInstanceTable']
  QSSGRenderMesh = WAIT['QSSGRenderMesh']
  QSSGRenderModel = WAIT['QSSGRenderModel']
  QSSGRhiContext = WAIT['QSSGRhiContext']
  QSSGRhiGraphicsPipelineState = WAIT['QSSGRhiGraphicsPipelineState']
  QSSGRhiShaderResourceBindingList = WAIT['QSSGRhiShaderResourceBindingList']
  QShader = WAIT['QShader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRhiContextPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRhiContextPrivate: a plain Python object standing
  in front of one C++ QSSGRhiContextPrivate.

  C++ hands a QSSGRhiContextPrivate around as a copy, so every C++
  QSSGRhiContextPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRhiContextPrivate that has a ritual and that
  Python can call so far, 19 names in all: 'q_func', 'get',
  'shaderDebuggingEnabled', 'editorMode', 'setMainRenderPassDescriptor',
  'setCommandBuffer', 'setRenderTarget', 'setMainPassSampleCount',
  'setMainPassViewCount', 'releaseCachedResources', 'registerTexture',
  'releaseTexture', 'registerMesh', 'releaseMesh', 'srb', 'pipeline',
  'computePipeline', 'cleanupDrawCallData', 'releaseInstanceBuffer'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSSGRhiContext *QSSGRhiContextPrivate::q_func() const': takes
    in Python what 'QSSGRhiContext *QSSGRhiContextPrivate::q_func()' takes.
  - Qt's 'QSSGRhiContextPrivate::QSSGRhiContextPrivate(QSSGRhiContext
    &rhiCtx, QRhi *rhi_)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSSGRhiContextPrivate *QSSGRhiContextPrivate::get(const
    QSSGRhiContext *q)': takes in Python what 'QSSGRhiContextPrivate
    *QSSGRhiContextPrivate::get(QSSGRhiContext *q)' takes.
  - Qt's 'void
    QSSGRhiContextPrivate::releaseCachedSrb(QSSGRhiShaderResourceBindingList
    &bindings)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiDrawCallData &QSSGRhiContextPrivate::drawCallData(const
    QSSGRhiDrawCallDataKey &key)': gives a type Python has no way to take
    yet.
  - Qt's 'void QSSGRhiContextPrivate::releaseDrawCallData(QSSGRhiDrawCallData
    &dcd)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiInstanceBufferData
    &QSSGRhiContextPrivate::instanceBufferData(QSSGRenderInstanceTable
    *instanceTable)': gives a type Python has no way to take yet.
  - Qt's 'QSSGRhiInstanceBufferData
    &QSSGRhiContextPrivate::instanceBufferData(const QSSGRenderModel
    *model)': gives a type Python has no way to take yet.
  - Qt's 'QSSGRhiParticleData &QSSGRhiContextPrivate::particleData(const
    QSSGRenderGraphObject *particlesOrModel)': gives a type Python has no way
    to take yet.
  - Qt's 'QSSGRhiContextPrivate::~QSSGRhiContextPrivate()': the destructor:
    Python removes its C++ QSSGRhiContextPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGRhiContextPrivate is created at the first use, not by
    'QSSGRhiContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRhiContextPrivate back gives a copy the ritual
    made for Python, in a new cute QSSGRhiContextPrivate.
  - Each name of Qt's QSSGRhiContextPrivate that has no cute function yet,
    '__init__', 'drawCallData', 'instanceBufferData', 'particleData',
    'releaseCachedSrb', 'releaseDrawCallData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRhiContext)
  @overload(NoneType)
  def get(q: Optional[QSSGRhiContext]) -> Optional[QSSGRhiContextPrivate]:
    """
    Calls Qt's 'QSSGRhiContextPrivate
    *QSSGRhiContextPrivate::get(QSSGRhiContext *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextprivate.html#get

    Parameters
    ----------

    q : Optional[QSSGRhiContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRhiContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRhiContextPrivate *QSSGRhiContextPrivate::get(QSSGRhiContext *q)
    address = Rituals.call(
        'ritual_ZN21QSSGRhiContextPrivate3getEP14QSSGRhiContext',
        CuteMixin._addressOf(q),
    )
    return QSSGRhiContextPrivate._cuteAt(address)

  @staticmethod
  def shaderDebuggingEnabled() -> bool:
    """
    Calls Qt's 'bool QSSGRhiContextPrivate::shaderDebuggingEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#shaderDebuggingEnabled
    """
    #  bool QSSGRhiContextPrivate::shaderDebuggingEnabled()
    return Rituals.call(
        'ritual_ZN21QSSGRhiContextPrivate22shaderDebuggingEnabledEv',
    )

  @staticmethod
  def editorMode() -> bool:
    """
    Calls Qt's 'bool QSSGRhiContextPrivate::editorMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#editorMode
    """
    #  bool QSSGRhiContextPrivate::editorMode()
    return Rituals.call('ritual_ZN21QSSGRhiContextPrivate10editorModeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRhiContextPrivate'

  #  Qt's '~QSSGRhiContextPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRhiContextPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSSGRhiContextPrivateD1Ev'

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

  @overload(QRhiRenderPassDescriptor)
  @overload(NoneType)
  def setMainRenderPassDescriptor(
      self,
      rpDesc: Optional[QRhiRenderPassDescriptor],
  ) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::setMainRenderPassDescriptor(
    QRhiRenderPassDescriptor *rpDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html

    Parameters
    ----------

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::setMainRenderPassDescriptor(
    #      QRhiRenderPassDescriptor *rpDesc)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate27setMainRenderPassDescriptorEP24Q'
        'RhiRenderPassDescriptor',
        self._addressOf(rpDesc),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def setCommandBuffer(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void
    QSSGRhiContextPrivate::setCommandBuffer(QRhiCommandBuffer *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#setCommandBuffer

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::setCommandBuffer(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate16setCommandBufferEP17QRhiCommandB'
        'uffer',
        self._addressOf(cb),
    )

  @overload(QRhiRenderTarget)
  @overload(NoneType)
  def setRenderTarget(self, rt: Optional[QRhiRenderTarget]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::setRenderTarget(QRhiRenderTarget
    *rt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#setRenderTarget

    Parameters
    ----------

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::setRenderTarget(QRhiRenderTarget *rt)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate15setRenderTargetEP16QRhiRenderTar'
        'get',
        self._addressOf(rt),
    )

  @overload(int)
  def setMainPassSampleCount(self, samples: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::setMainPassSampleCount(int
    samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#setMainPassSampleCount

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QSSGRhiContextPrivate::setMainPassSampleCount(int samples)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate22setMainPassSampleCountEi',
        samples,
    )

  @overload(int)
  def setMainPassViewCount(self, viewCount: int) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::setMainPassViewCount(int
    viewCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#setMainPassViewCount

    Parameters
    ----------

    viewCount : int
      Passed on as it is.
    """
    #  void QSSGRhiContextPrivate::setMainPassViewCount(int viewCount)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate20setMainPassViewCountEi',
        viewCount,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiContextPrivate::QSSGRhiContextPrivate(QSSGRhiContext
    &rhiCtx, QRhi *rhi_)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.__init__' has no cute function yet. Qt's "
        "'QSSGRhiContextPrivate::QSSGRhiContextPrivate(QSSGRhiContext "
        "&rhiCtx, QRhi *rhi_)': takes a type Python has no way to hand over "
        "yet.")

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

  def q_func(self) -> Optional[QSSGRhiContext]:
    """
    Calls Qt's 'QSSGRhiContext *QSSGRhiContextPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextprivate.html#q_func

    Returns
    -------

    Optional[QSSGRhiContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRhiContext *QSSGRhiContextPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QSSGRhiContextPrivate6q_funcEv')
    from . import QSSGRhiContext
    return QSSGRhiContext._cuteAt(address)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#releaseCachedResources
    """
    #  void QSSGRhiContextPrivate::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate22releaseCachedResourcesEv',
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def registerTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::registerTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#registerTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::registerTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate15registerTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def releaseTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::releaseTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#releaseTexture

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::releaseTexture(QRhiTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate14releaseTextureEP11QRhiTexture',
        self._addressOf(texture),
    )

  @overload(QSSGRenderMesh)
  @overload(NoneType)
  def registerMesh(self, mesh: Optional[QSSGRenderMesh]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::registerMesh(QSSGRenderMesh
    *mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#registerMesh

    Parameters
    ----------

    mesh : Optional[QSSGRenderMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::registerMesh(QSSGRenderMesh *mesh)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate12registerMeshEP14QSSGRenderMesh',
        self._addressOf(mesh),
    )

  @overload(QSSGRenderMesh)
  @overload(NoneType)
  def releaseMesh(self, mesh: Optional[QSSGRenderMesh]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::releaseMesh(QSSGRenderMesh
    *mesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#releaseMesh

    Parameters
    ----------

    mesh : Optional[QSSGRenderMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::releaseMesh(QSSGRenderMesh *mesh)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate11releaseMeshEP14QSSGRenderMesh',
        self._addressOf(mesh),
    )

  @overload(QSSGRhiShaderResourceBindingList)
  def srb(
      self,
      bindings: QSSGRhiShaderResourceBindingList,
  ) -> Optional[QRhiShaderResourceBindings]:
    """
    Calls Qt's 'QRhiShaderResourceBindings *QSSGRhiContextPrivate::srb(const
    QSSGRhiShaderResourceBindingList &bindings)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrhicontextprivate.html#srb

    Parameters
    ----------

    bindings : QSSGRhiShaderResourceBindingList
      Passed on as a value: Qt reads the C++
      QSSGRhiShaderResourceBindingList, which stays Python's own.

    Returns
    -------

    Optional[QRhiShaderResourceBindings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShaderResourceBindings *QSSGRhiContextPrivate::srb(const
    #      QSSGRhiShaderResourceBindingList &bindings)
    address = self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate3srbERK32QSSGRhiShaderResourceBind'
        'ingList',
        self._valueOf(bindings),
    )
    from ..QtGui import QRhiShaderResourceBindings
    return QRhiShaderResourceBindings._cuteAt(address)

  @overload(
      QSSGRhiGraphicsPipelineState, QRhiRenderPassDescriptor,
      QRhiShaderResourceBindings,
  )
  @overload(QSSGRhiGraphicsPipelineState, QRhiRenderPassDescriptor, NoneType)
  @overload(
      QSSGRhiGraphicsPipelineState, NoneType, QRhiShaderResourceBindings,
  )
  @overload(QSSGRhiGraphicsPipelineState, NoneType, NoneType)
  def pipeline(
      self,
      ps: QSSGRhiGraphicsPipelineState,
      rpDesc: Optional[QRhiRenderPassDescriptor],
      srb: Optional[QRhiShaderResourceBindings],
  ) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
    QSSGRhiGraphicsPipelineState &ps, QRhiRenderPassDescriptor *rpDesc,
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#pipeline

    Parameters
    ----------

    ps : QSSGRhiGraphicsPipelineState
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

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
    #      QSSGRhiGraphicsPipelineState &ps, QRhiRenderPassDescriptor
    #      *rpDesc, QRhiShaderResourceBindings *srb)
    address = self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate8pipelineERK28QSSGRhiGraphicsPipel'
        'ineStateP24QRhiRenderPassDescriptorP26QRhiShaderResourceBindings',
        self._valueOf(ps), self._addressOf(rpDesc), self._addressOf(srb),
    )
    from ..QtGui import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  @overload(
      QSSGGraphicsPipelineStateKey, QRhiRenderPassDescriptor,
      QRhiShaderResourceBindings,
  )
  @overload(QSSGGraphicsPipelineStateKey, QRhiRenderPassDescriptor, NoneType)
  @overload(
      QSSGGraphicsPipelineStateKey, NoneType, QRhiShaderResourceBindings,
  )
  @overload(QSSGGraphicsPipelineStateKey, NoneType, NoneType)
  def pipeline(
      self,
      key: QSSGGraphicsPipelineStateKey,
      rpDesc: Optional[QRhiRenderPassDescriptor],
      srb: Optional[QRhiShaderResourceBindings],
  ) -> Optional[QRhiGraphicsPipeline]:
    """
    Calls Qt's 'QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
    QSSGGraphicsPipelineStateKey &key, QRhiRenderPassDescriptor *rpDesc,
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#pipeline

    Parameters
    ----------

    key : QSSGGraphicsPipelineStateKey
      Passed on as a value: Qt reads the C++ QSSGGraphicsPipelineStateKey,
      which stays Python's own.

    rpDesc : Optional[QRhiRenderPassDescriptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiGraphicsPipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
    #      QSSGGraphicsPipelineStateKey &key, QRhiRenderPassDescriptor
    #      *rpDesc, QRhiShaderResourceBindings *srb)
    address = self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate8pipelineERK28QSSGGraphicsPipeline'
        'StateKeyP24QRhiRenderPassDescriptorP26QRhiShaderResourceBindings',
        self._valueOf(key), self._addressOf(rpDesc), self._addressOf(srb),
    )
    from ..QtGui import QRhiGraphicsPipeline
    return QRhiGraphicsPipeline._cuteAt(address)

  @overload(QShader, QRhiShaderResourceBindings)
  @overload(QShader, NoneType)
  def computePipeline(
      self,
      shader: QShader,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline
    *QSSGRhiContextPrivate::computePipeline(const QShader &shader,
    QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#computePipeline

    Parameters
    ----------

    shader : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QSSGRhiContextPrivate::computePipeline(const
    #      QShader &shader, QRhiShaderResourceBindings *srb)
    address = self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate15computePipelineERK7QShaderP26QRh'
        'iShaderResourceBindings',
        self._valueOf(shader), self._addressOf(srb),
    )
    from ..QtGui import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  @overload(QSSGComputePipelineStateKey, QRhiShaderResourceBindings)
  @overload(QSSGComputePipelineStateKey, NoneType)
  def computePipeline(
      self,
      key: QSSGComputePipelineStateKey,
      srb: Optional[QRhiShaderResourceBindings],
  ) -> Optional[QRhiComputePipeline]:
    """
    Calls Qt's 'QRhiComputePipeline
    *QSSGRhiContextPrivate::computePipeline(const QSSGComputePipelineStateKey
    &key, QRhiShaderResourceBindings *srb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#computePipeline

    Parameters
    ----------

    key : QSSGComputePipelineStateKey
      Passed on as a value: Qt reads the C++ QSSGComputePipelineStateKey,
      which stays Python's own.

    srb : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiComputePipeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiComputePipeline *QSSGRhiContextPrivate::computePipeline(const
    #      QSSGComputePipelineStateKey &key, QRhiShaderResourceBindings *srb)
    address = self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate15computePipelineERK27QSSGComputeP'
        'ipelineStateKeyP26QRhiShaderResourceBindings',
        self._valueOf(key), self._addressOf(srb),
    )
    from ..QtGui import QRhiComputePipeline
    return QRhiComputePipeline._cuteAt(address)

  @overload(QSSGRenderModel)
  @overload(NoneType)
  def cleanupDrawCallData(self, model: Optional[QSSGRenderModel]) -> None:
    """
    Calls Qt's 'void QSSGRhiContextPrivate::cleanupDrawCallData(const
    QSSGRenderModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#cleanupDrawCallData

    Parameters
    ----------

    model : Optional[QSSGRenderModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::cleanupDrawCallData(const QSSGRenderModel
    #      *model)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate19cleanupDrawCallDataEPK15QSSGRend'
        'erModel',
        self._addressOf(model),
    )

  @overload(QSSGRenderInstanceTable)
  @overload(NoneType)
  def releaseInstanceBuffer(
      self,
      instanceTable: Optional[QSSGRenderInstanceTable],
  ) -> None:
    """
    Calls Qt's 'void
    QSSGRhiContextPrivate::releaseInstanceBuffer(QSSGRenderInstanceTable
    *instanceTable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrhicontextprivate.html#releaseInstanceBuffer

    Parameters
    ----------

    instanceTable : Optional[QSSGRenderInstanceTable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGRhiContextPrivate::releaseInstanceBuffer(
    #      QSSGRenderInstanceTable *instanceTable)
    self.uglySide.call(
        'ritual_ZN21QSSGRhiContextPrivate21releaseInstanceBufferEP23QSSGRen'
        'derInstanceTable',
        self._addressOf(instanceTable),
    )

  @staticmethod
  def drawCallData(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiDrawCallData &QSSGRhiContextPrivate::drawCallData(const
    QSSGRhiDrawCallDataKey &key)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.drawCallData' has no cute function yet. "
        "Qt's 'QSSGRhiDrawCallData "
        "&QSSGRhiContextPrivate::drawCallData(const QSSGRhiDrawCallDataKey "
        "&key)': gives a type Python has no way to take yet.")

  @staticmethod
  def instanceBufferData(*__, **_) -> Never:
    """
    - Qt's 'QSSGRhiInstanceBufferData
      &QSSGRhiContextPrivate::instanceBufferData(QSSGRenderInstanceTable
      *instanceTable)': gives a type Python has no way to take yet.
    - Qt's 'QSSGRhiInstanceBufferData
      &QSSGRhiContextPrivate::instanceBufferData(const QSSGRenderModel
      *model)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.instanceBufferData' has no cute function "
        "yet. Qt's 'QSSGRhiInstanceBufferData "
        "&QSSGRhiContextPrivate::instanceBufferData(QSSGRenderInstanceTable "
        "*instanceTable)': gives a type Python has no way to take yet. Qt's "
        "'QSSGRhiInstanceBufferData "
        "&QSSGRhiContextPrivate::instanceBufferData(const QSSGRenderModel "
        "*model)': gives a type Python has no way to take yet.")

  @staticmethod
  def particleData(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiParticleData &QSSGRhiContextPrivate::particleData(const
    QSSGRenderGraphObject *particlesOrModel)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.particleData' has no cute function yet. "
        "Qt's 'QSSGRhiParticleData "
        "&QSSGRhiContextPrivate::particleData(const QSSGRenderGraphObject "
        "*particlesOrModel)': gives a type Python has no way to take yet.")

  @staticmethod
  def releaseCachedSrb(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGRhiContextPrivate::releaseCachedSrb(QSSGRhiShaderResourceBindingList
    &bindings)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.releaseCachedSrb' has no cute function yet. "
        "Qt's 'void "
        "QSSGRhiContextPrivate::releaseCachedSrb(QSSGRhiShaderResourceBindin"
        "gList &bindings)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def releaseDrawCallData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRhiContextPrivate::releaseDrawCallData(QSSGRhiDrawCallData
    &dcd)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRhiContextPrivate.releaseDrawCallData' has no cute function "
        "yet. Qt's 'void "
        "QSSGRhiContextPrivate::releaseDrawCallData(QSSGRhiDrawCallData "
        "&dcd)': takes a type Python has no way to hand over yet.")
