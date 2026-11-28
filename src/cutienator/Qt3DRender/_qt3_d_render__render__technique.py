"""
Qt3DRender::Render::Technique binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/technique_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::Technique to be private: it declares the
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


class Technique(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Technique: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Technique.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Technique is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Technique that has a ritual and
  that Python can call so far, 11 names in all: 'cleanup',
  'syncFromFrontEnd', 'appendRenderPass', 'removeRenderPass',
  'appendFilterKey', 'removeFilterKey', 'graphicsApiFilter',
  'isCompatibleWithRenderer', 'setCompatibleWithRenderer', 'setNodeManager',
  'nodeManager'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Technique::~Technique()': the destructor:
    Python never removes a C++ Qt3DRender::Render::Technique.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::parameters() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::filterKeys() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::renderPasses() const': gives a type Python
    has no way to take yet.
  - Qt's 'bool Qt3DRender::Render::Technique::isCompatibleWithFilters(const
    Qt3DCore::QNodeIdVector &filterKeyIds)': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Technique is created at the first use, not by
    'Qt3DRender::Render::Technique(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Technique.
  - Each name of Qt's Qt3DRender::Render::Technique that has no cute function
    yet, 'filterKeys', 'isCompatibleWithFilters', 'parameters',
    'renderPasses', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Technique'

  #  A C++ Qt3DRender::Render::Technique Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Technique'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def graphicsApiFilter(self) -> Optional[Qt3DRender.GraphicsApiFilterData]:
    """
    Calls Qt's 'const GraphicsApiFilterData
    *Qt3DRender::Render::Technique::graphicsApiFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#graphicsApiFilter

    Returns
    -------

    Optional[Qt3DRender.GraphicsApiFilterData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const GraphicsApiFilterData
    #      *Qt3DRender::Render::Technique::graphicsApiFilter() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Technique17graphicsApiFilterEv',
    )
    return Qt3DRender.GraphicsApiFilterData._cuteAt(address)

  def isCompatibleWithRenderer(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::Technique::isCompatibleWithRenderer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html
    """
    #  bool Qt3DRender::Render::Technique::isCompatibleWithRenderer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Technique24isCompatibleWithRendererE'
        'v',
    )

  def nodeManager(self) -> Optional[Qt3DRender.Render.NodeManagers]:
    """
    Calls Qt's 'NodeManagers *Qt3DRender::Render::Technique::nodeManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#nodeManager

    Returns
    -------

    Optional[Qt3DRender.Render.NodeManagers]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  NodeManagers *Qt3DRender::Render::Technique::nodeManager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Technique11nodeManagerEv',
    )
    return Qt3DRender.Render.NodeManagers._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCompatibleWithRenderer(self, compatible: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::setCompatibleWithRenderer(bool
    compatible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html

    Parameters
    ----------

    compatible : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Technique::setCompatibleWithRenderer(bool
    #      compatible)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique25setCompatibleWithRendererE'
        'b',
        compatible,
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManager(
      self,
      nodeManager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::setNodeManager(NodeManagers
    *nodeManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#setNodeManager

    Parameters
    ----------

    nodeManager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Technique::setNodeManager(NodeManagers
    #      *nodeManager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique14setNodeManagerEPNS0_12Node'
        'ManagersE',
        self._addressOf(nodeManager),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::Technique::Technique()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#Technique
    """
    #  Qt3DRender::Render::Technique::Technique()
    self._noteCreation(Technique, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9TechniqueC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::Technique::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#cleanup
    """
    #  void Qt3DRender::Render::Technique::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9Technique7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Technique::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Technique::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render9Technique16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render9Technique16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def appendRenderPass(self, renderPassId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::appendRenderPass(Qt3DCore::QNodeId
    renderPassId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#appendRenderPass

    Parameters
    ----------

    renderPassId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Technique::appendRenderPass(Qt3DCore::QNodeId
    #      renderPassId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique16appendRenderPassEN8Qt3DCor'
        'e7QNodeIdE',
        self._valueOf(renderPassId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeRenderPass(self, renderPassId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::removeRenderPass(Qt3DCore::QNodeId
    renderPassId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#removeRenderPass

    Parameters
    ----------

    renderPassId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Technique::removeRenderPass(Qt3DCore::QNodeId
    #      renderPassId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique16removeRenderPassEN8Qt3DCor'
        'e7QNodeIdE',
        self._valueOf(renderPassId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def appendFilterKey(self, criterionId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::appendFilterKey(Qt3DCore::QNodeId
    criterionId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#appendFilterKey

    Parameters
    ----------

    criterionId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Technique::appendFilterKey(Qt3DCore::QNodeId
    #      criterionId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique15appendFilterKeyEN8Qt3DCore'
        '7QNodeIdE',
        self._valueOf(criterionId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeFilterKey(self, criterionId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Technique::removeFilterKey(Qt3DCore::QNodeId
    criterionId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-technique.html#removeFilterKey

    Parameters
    ----------

    criterionId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Technique::removeFilterKey(Qt3DCore::QNodeId
    #      criterionId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render9Technique15removeFilterKeyEN8Qt3DCore'
        '7QNodeIdE',
        self._valueOf(criterionId),
    )

  @staticmethod
  def filterKeys(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::filterKeys() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Technique.filterKeys' has no cute function yet. "
        "Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::Technique::filterKeys() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def isCompatibleWithFilters(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::Technique::isCompatibleWithFilters(const
    Qt3DCore::QNodeIdVector &filterKeyIds)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Technique.isCompatibleWithFilters' has no cute "
        "function yet. Qt's 'bool "
        "Qt3DRender::Render::Technique::isCompatibleWithFilters(const "
        "Qt3DCore::QNodeIdVector &filterKeyIds)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::parameters() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Technique.parameters' has no cute function yet. "
        "Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::Technique::parameters() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def renderPasses(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::Technique::renderPasses() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Technique.renderPasses' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::Technique::renderPasses() const': gives a type "
        "Python has no way to take yet.")
