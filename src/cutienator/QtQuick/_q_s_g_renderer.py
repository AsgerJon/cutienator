"""
QSGRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRenderer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGAbstractRenderer, QSGMaterialShader, QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QMatrix4x4, QRhi, QRhiResourceUpdateBatch
  from . import QSGNodeUpdater, QSGRenderContext, QSGRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSGNodeUpdater = WAIT['QSGNodeUpdater']
  QSGRenderContext = WAIT['QSGRenderContext']
  QSGRenderTarget = WAIT['QSGRenderTarget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRenderer(QSGAbstractRenderer):
  """
  The cute side of Qt's QSGRenderer: a plain Python object standing in front
  of one C++ QSGRenderer.

  It is built on the cute 'QSGAbstractRenderer', as Qt's QSGRenderer is built
  on Qt's QSGAbstractRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRenderer that has a ritual and that Python can
  call so far, 31 names in all: 'currentProjectionMatrix',
  'currentModelViewMatrix', 'currentCombinedMatrix', 'currentOpacity',
  'determinant', 'setDevicePixelRatio', 'devicePixelRatio', 'context',
  'isMirrored', 'renderScene', 'prepareSceneInline', 'renderSceneInline',
  'nodeChanged', 'nodeUpdater', 'setNodeUpdater', 'state',
  'setVisualizationMode', 'hasVisualizationModeWithContinuousUpdate',
  'releaseCachedResources', 'clearChangedFlag', 'currentUniformData',
  'currentResourceUpdateBatch', 'currentRhi', 'setRenderTarget',
  'renderTarget', 'render', 'prepareInline', 'renderInline', 'preprocess',
  'addNodesToPreprocess', 'removeNodesToPreprocess'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRenderer::~QSGRenderer()': the destructor: Python never removes
    a C++ QSGRenderer.
  - Qt's 'void
    QSGRenderer::setRenderPassRecordingCallbacks(QSGRenderContext::
    RenderPassCallback start, QSGRenderContext::RenderPassCallback end, void
    *userData)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGRenderer is created at the first use, not by
    'QSGRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRenderer.
  - Qt tells when it has removed the C++ QSGRenderer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSGRenderer that has no cute function yet,
    'setRenderPassRecordingCallbacks', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRenderer'

  #  A C++ QSGRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRenderer'

  #  The functions Qt calls itself that QSGRenderer is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setVisualizationMode': (
          ('_ZN11QSGRenderer20setVisualizationModeERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'hasVisualizationModeWithContinuousUpdate': (
          ('_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv',
           ('bool', 'number', ''),
           ()),
      ),
      'releaseCachedResources': (
          ('_ZN11QSGRenderer22releaseCachedResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'render': (
          ('_ZN11QSGRenderer6renderEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'prepareInline': (
          ('_ZN11QSGRenderer13prepareInlineEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'renderInline': (
          ('_ZN11QSGRenderer12renderInlineEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'preprocess': (
          ('_ZN11QSGRenderer10preprocessEv',
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

  @overload(int)
  def currentProjectionMatrix(self, index: int) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSGRenderer::currentProjectionMatrix(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#currentProjectionMatrix

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGRenderer::currentProjectionMatrix(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer23currentProjectionMatrixEi', index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def currentModelViewMatrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSGRenderer::currentModelViewMatrix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#currentModelViewMatrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGRenderer::currentModelViewMatrix() const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer22currentModelViewMatrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(int)
  def currentCombinedMatrix(self, index: int) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSGRenderer::currentCombinedMatrix(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#currentCombinedMatrix

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGRenderer::currentCombinedMatrix(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer21currentCombinedMatrixEi', index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def currentOpacity(self) -> float:
    """
    Calls Qt's 'qreal QSGRenderer::currentOpacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#currentOpacity
    """
    #  qreal QSGRenderer::currentOpacity() const
    return self.uglySide.call('ritual_ZNK11QSGRenderer14currentOpacityEv')

  def determinant(self) -> float:
    """
    Calls Qt's 'qreal QSGRenderer::determinant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#determinant
    """
    #  qreal QSGRenderer::determinant() const
    return self.uglySide.call('ritual_ZNK11QSGRenderer11determinantEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QSGRenderer::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#devicePixelRatio
    """
    #  qreal QSGRenderer::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK11QSGRenderer16devicePixelRatioEv')

  def context(self) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext *QSGRenderer::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#context

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext *QSGRenderer::context() const
    address = self.uglySide.call('ritual_ZNK11QSGRenderer7contextEv')
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QSGRenderer::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#isMirrored
    """
    #  bool QSGRenderer::isMirrored() const
    return self.uglySide.call('ritual_ZNK11QSGRenderer10isMirroredEv')

  def nodeUpdater(self) -> Optional[QSGNodeUpdater]:
    """
    Calls Qt's 'QSGNodeUpdater *QSGRenderer::nodeUpdater() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#nodeUpdater

    Returns
    -------

    Optional[QSGNodeUpdater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNodeUpdater *QSGRenderer::nodeUpdater() const
    address = self.uglySide.call('ritual_ZNK11QSGRenderer11nodeUpdaterEv')
    from . import QSGNodeUpdater
    return QSGNodeUpdater._cuteAt(address)

  @overload(QSGMaterialShader.RenderState.DirtyStates)
  def state(
      self,
      dirty: QSGMaterialShader.RenderState.DirtyStates,
  ) -> QSGMaterialShader.RenderState:
    """
    Calls Qt's 'QSGMaterialShader::RenderState
    QSGRenderer::state(QSGMaterialShader::RenderState::DirtyStates dirty)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#state

    Parameters
    ----------

    dirty : QSGMaterialShader.RenderState.DirtyStates
      Passed on as its number.

    Returns
    -------

    QSGMaterialShader.RenderState
      A new cute QSGMaterialShader::RenderState around the copy Qt gave back.
      Python owns it.
    """
    #  QSGMaterialShader::RenderState
    #      QSGRenderer::state(QSGMaterialShader::RenderState::DirtyStates
    #      dirty) const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer5stateE6QFlagsIN17QSGMaterialShader11Render'
        'State10DirtyStateEE',
        dirty.value,
    )
    return QSGMaterialShader.RenderState._cuteOwning(address)

  def hasVisualizationModeWithContinuousUpdate(self) -> bool:
    """
    Calls Qt's 'bool QSGRenderer::hasVisualizationModeWithContinuousUpdate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html
    """
    #  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
    ritual = (
        'ritual_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QSGRenderer40hasVisualizationModeWithContinuousU'
          'pdateEv')
    return self.uglySide.call(ritual)

  def currentUniformData(self) -> Optional[QByteArray]:
    """
    Calls Qt's 'QByteArray *QSGRenderer::currentUniformData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#currentUniformData

    Returns
    -------

    Optional[QByteArray]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QByteArray *QSGRenderer::currentUniformData() const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer18currentUniformDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteAt(address)

  def currentResourceUpdateBatch(self) -> Optional[QRhiResourceUpdateBatch]:
    """
    Calls Qt's 'QRhiResourceUpdateBatch
    *QSGRenderer::currentResourceUpdateBatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#currentResourceUpdateBatch

    Returns
    -------

    Optional[QRhiResourceUpdateBatch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatch *QSGRenderer::currentResourceUpdateBatch()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QSGRenderer26currentResourceUpdateBatchEv',
    )
    from ..QtGui import QRhiResourceUpdateBatch
    return QRhiResourceUpdateBatch._cuteAt(address)

  def currentRhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSGRenderer::currentRhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#currentRhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSGRenderer::currentRhi() const
    address = self.uglySide.call('ritual_ZNK11QSGRenderer10currentRhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def renderTarget(self) -> QSGRenderTarget:
    """
    Calls Qt's 'const QSGRenderTarget &QSGRenderer::renderTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#renderTarget

    Returns
    -------

    QSGRenderTarget
      A new cute QSGRenderTarget around the copy Qt gave back. Python owns
      it.
    """
    #  const QSGRenderTarget &QSGRenderer::renderTarget() const
    address = self.uglySide.call('ritual_ZNK11QSGRenderer12renderTargetEv')
    from . import QSGRenderTarget
    return QSGRenderTarget._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGRenderer::setDevicePixelRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGRenderer::setDevicePixelRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN11QSGRenderer19setDevicePixelRatioEd', ratio,
    )

  @overload(QSGNodeUpdater)
  @overload(NoneType)
  def setNodeUpdater(self, updater: Optional[QSGNodeUpdater]) -> None:
    """
    Calls Qt's 'void QSGRenderer::setNodeUpdater(QSGNodeUpdater *updater)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#setNodeUpdater

    Parameters
    ----------

    updater : Optional[QSGNodeUpdater]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderer::setNodeUpdater(QSGNodeUpdater *updater)
    self.uglySide.call(
        'ritual_ZN11QSGRenderer14setNodeUpdaterEP14QSGNodeUpdater',
        self._addressOf(updater),
    )

  @overload(QByteArray)
  def setVisualizationMode(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void QSGRenderer::setVisualizationMode(const QByteArray
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#setVisualizationMode

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
    ritual = 'ritual_ZN11QSGRenderer20setVisualizationModeERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSGRenderer20setVisualizationModeERK10QByteArray')
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QSGRenderTarget)
  def setRenderTarget(self, rt: QSGRenderTarget) -> None:
    """
    Calls Qt's 'void QSGRenderer::setRenderTarget(const QSGRenderTarget
    &rt)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#setRenderTarget

    Parameters
    ----------

    rt : QSGRenderTarget
      Passed on as a value: Qt reads the C++ QSGRenderTarget, which stays
      Python's own.
    """
    #  void QSGRenderer::setRenderTarget(const QSGRenderTarget &rt)
    self.uglySide.call(
        'ritual_ZN11QSGRenderer15setRenderTargetERK15QSGRenderTarget',
        self._valueOf(rt),
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's 'QSGRenderer::QSGRenderer(QSGRenderContext
    *context)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#QSGRenderer

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGRenderer::QSGRenderer(QSGRenderContext *context)
    self._noteCreation(QSGRenderer, lambda: Rituals.call(
        'ritual_ZN11QSGRendererC1EP16QSGRenderContext',
        self._addressOf(context),
    ))

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

  def renderScene(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::renderScene()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#renderScene
    """
    #  void QSGRenderer::renderScene()
    ritual = 'ritual_ZN11QSGRenderer11renderSceneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer11renderSceneEv'
    self.uglySide.call(ritual)

  def prepareSceneInline(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::prepareSceneInline()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#prepareSceneInline
    """
    #  void QSGRenderer::prepareSceneInline()
    ritual = 'ritual_ZN11QSGRenderer18prepareSceneInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer18prepareSceneInlineEv'
    self.uglySide.call(ritual)

  def renderSceneInline(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::renderSceneInline()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#renderSceneInline
    """
    #  void QSGRenderer::renderSceneInline()
    ritual = 'ritual_ZN11QSGRenderer17renderSceneInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer17renderSceneInlineEv'
    self.uglySide.call(ritual)

  @overload(QSGNode, QSGNode.DirtyState)
  @overload(NoneType, QSGNode.DirtyState)
  def nodeChanged(
      self,
      node: Optional[QSGNode],
      state: QSGNode.DirtyState,
  ) -> None:
    """
    Calls Qt's 'void QSGRenderer::nodeChanged(QSGNode *node,
    QSGNode::DirtyState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#nodeChanged

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QSGNode.DirtyState
      Passed on as its number.
    """
    #  void QSGRenderer::nodeChanged(QSGNode *node, QSGNode::DirtyState
    #      state)
    ritual = (
        'ritual_ZN11QSGRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtySt'
        'ateBitEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSGRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13D'
          'irtyStateBitEE')
    self.uglySide.call(ritual, self._addressOf(node, 'QSGNode'), state.value)

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#releaseCachedResources
    """
    #  void QSGRenderer::releaseCachedResources()
    ritual = 'ritual_ZN11QSGRenderer22releaseCachedResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer22releaseCachedResourcesEv'
    self.uglySide.call(ritual)

  def clearChangedFlag(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::clearChangedFlag()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#clearChangedFlag
    """
    #  void QSGRenderer::clearChangedFlag()
    self.uglySide.call('ritual_ZN11QSGRenderer16clearChangedFlagEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#render
    """
    #  void QSGRenderer::render()
    self.uglySide.call('ritual_ZN11QSGRenderer6renderEv')

  def prepareInline(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::prepareInline()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#prepareInline
    """
    #  void QSGRenderer::prepareInline()
    ritual = 'ritual_ZN11QSGRenderer13prepareInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer13prepareInlineEv'
    self.uglySide.call(ritual)

  def renderInline(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::renderInline()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#renderInline
    """
    #  void QSGRenderer::renderInline()
    ritual = 'ritual_ZN11QSGRenderer12renderInlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer12renderInlineEv'
    self.uglySide.call(ritual)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGRenderer::preprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderer.html#preprocess
    """
    #  void QSGRenderer::preprocess()
    ritual = 'ritual_ZN11QSGRenderer10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSGRenderer10preprocessEv'
    self.uglySide.call(ritual)

  @overload(QSGNode)
  @overload(NoneType)
  def addNodesToPreprocess(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGRenderer::addNodesToPreprocess(QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#addNodesToPreprocess

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderer::addNodesToPreprocess(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN11QSGRenderer20addNodesToPreprocessEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def removeNodesToPreprocess(self, node: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGRenderer::removeNodesToPreprocess(QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderer.html#removeNodesToPreprocess

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderer::removeNodesToPreprocess(QSGNode *node)
    self.uglySide.call(
        'ritual_ZN11QSGRenderer23removeNodesToPreprocessEP7QSGNode',
        self._addressOf(node, 'QSGNode'),
    )

  @staticmethod
  def setRenderPassRecordingCallbacks(*__, **_) -> Never:
    """
    Qt's 'void
    QSGRenderer::setRenderPassRecordingCallbacks(QSGRenderContext::
    RenderPassCallback start, QSGRenderContext::RenderPassCallback end, void
    *userData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGRenderer.setRenderPassRecordingCallbacks' has no cute function "
        "yet. Qt's 'void "
        "QSGRenderer::setRenderPassRecordingCallbacks(QSGRenderContext::Rend"
        "erPassCallback start, QSGRenderContext::RenderPassCallback end, "
        "void *userData)': takes a type Python has no way to hand over yet.")
