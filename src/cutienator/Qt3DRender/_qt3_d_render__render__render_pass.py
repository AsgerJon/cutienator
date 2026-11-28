"""
Qt3DRender::Render::RenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/renderpass_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::RenderPass to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderPass(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::RenderPass: a plain Python object
  standing in front of one C++ Qt3DRender::Render::RenderPass.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::RenderPass is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderPass that has a ritual and
  that Python can call so far, 8 names in all: 'cleanup', 'syncFromFrontEnd',
  'shaderProgram', 'hasRenderStates', 'appendFilterKey', 'removeFilterKey',
  'addRenderState', 'removeRenderState'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::RenderPass::~RenderPass()': the destructor:
    Python never removes a C++ Qt3DRender::Render::RenderPass.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::filterKeys() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::parameters() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::renderStates() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderPass is created at the first use, not
    by 'Qt3DRender::Render::RenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderPass.
  - Each name of Qt's Qt3DRender::Render::RenderPass that has no cute
    function yet, 'filterKeys', 'parameters', 'renderStates', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderPass'

  #  A C++ Qt3DRender::Render::RenderPass Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_RenderPass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shaderProgram(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::RenderPass::shaderProgram() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#shaderProgram

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::RenderPass::shaderProgram()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10RenderPass13shaderProgramEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def hasRenderStates(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::RenderPass::hasRenderStates()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#hasRenderStates
    """
    #  bool Qt3DRender::Render::RenderPass::hasRenderStates() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render10RenderPass15hasRenderStatesEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::RenderPass::RenderPass()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#RenderPass
    """
    #  Qt3DRender::Render::RenderPass::RenderPass()
    self._noteCreation(RenderPass, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render10RenderPassC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RenderPass::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#cleanup
    """
    #  void Qt3DRender::Render::RenderPass::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render10RenderPass7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RenderPass::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::RenderPass::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render10RenderPass16syncFromFrontEndEPKN8Qt3'
        'DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render10RenderPass16syncFromFrontEndEP'
          'KN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def appendFilterKey(self, filterKeyId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderPass::appendFilterKey(Qt3DCore::QNodeId
    filterKeyId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#appendFilterKey

    Parameters
    ----------

    filterKeyId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderPass::appendFilterKey(Qt3DCore::QNodeId
    #      filterKeyId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10RenderPass15appendFilterKeyEN8Qt3DCo'
        're7QNodeIdE',
        self._valueOf(filterKeyId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeFilterKey(self, filterKeyId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderPass::removeFilterKey(Qt3DCore::QNodeId
    filterKeyId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#removeFilterKey

    Parameters
    ----------

    filterKeyId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderPass::removeFilterKey(Qt3DCore::QNodeId
    #      filterKeyId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10RenderPass15removeFilterKeyEN8Qt3DCo'
        're7QNodeIdE',
        self._valueOf(filterKeyId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addRenderState(self, renderStateId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderPass::addRenderState(Qt3DCore::QNodeId
    renderStateId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html#addRenderState

    Parameters
    ----------

    renderStateId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderPass::addRenderState(Qt3DCore::QNodeId
    #      renderStateId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10RenderPass14addRenderStateEN8Qt3DCor'
        'e7QNodeIdE',
        self._valueOf(renderStateId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeRenderState(self, renderStateId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderPass::removeRenderState(Qt3DCore::QNodeId
    renderStateId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderpass.html

    Parameters
    ----------

    renderStateId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderPass::removeRenderState(Qt3DCore::
    #      QNodeId renderStateId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render10RenderPass17removeRenderStateEN8Qt3D'
        'Core7QNodeIdE',
        self._valueOf(renderStateId),
    )

  @staticmethod
  def filterKeys(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::filterKeys() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderPass.filterKeys' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::RenderPass::filterKeys() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::parameters() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderPass.parameters' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::RenderPass::parameters() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def renderStates(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderPass::renderStates() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderPass.renderStates' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::RenderPass::renderStates() const': gives a "
        "type Python has no way to take yet.")
