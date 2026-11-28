"""
Qt3DRender::Render::FrameGraphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/framegraphnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::FrameGraphNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FrameGraphNode(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::FrameGraphNode: a plain Python
  object standing in front of one C++ Qt3DRender::Render::FrameGraphNode.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::FrameGraphNode is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FrameGraphNode that has a ritual
  and that Python can call so far, 8 names in all: 'nodeType',
  'setFrameGraphManager', 'manager', 'setParentId', 'parentId', 'parent',
  'cleanup', 'syncFromFrontEnd'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FrameGraphNode::~FrameGraphNode()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::FrameGraphNode.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::FrameGraphNode::childrenIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<FrameGraphNode *>
    Qt3DRender::Render::FrameGraphNode::children() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FrameGraphNode is created at the first use,
    not by 'Qt3DRender::Render::FrameGraphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::FrameGraphNode.
  - Each name of Qt's Qt3DRender::Render::FrameGraphNode that has no cute
    function yet, 'children', 'childrenIds', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::FrameGraphNode, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class FrameGraphNodeType(CuteNum):
    """
    The enum 'Qt3DRender::Render::FrameGraphNode::FrameGraphNodeType' of Qt,
    with the 25 names Qt gives in it.
    """

    InvalidNodeType = Kee[int](0)
    CameraSelector = Kee[int](1)
    LayerFilter = Kee[int](2)
    RenderPassFilter = Kee[int](3)
    RenderTarget = Kee[int](4)
    TechniqueFilter = Kee[int](5)
    Viewport = Kee[int](6)
    ClearBuffers = Kee[int](7)
    SortMethod = Kee[int](8)
    SubtreeEnabler = Kee[int](9)
    StateSet = Kee[int](10)
    NoDraw = Kee[int](11)
    FrustumCulling = Kee[int](12)
    Lighting = Kee[int](13)
    ComputeDispatch = Kee[int](14)
    Surface = Kee[int](15)
    RenderCapture = Kee[int](16)
    BufferCapture = Kee[int](17)
    MemoryBarrier = Kee[int](18)
    ProximityFilter = Kee[int](19)
    BlitFramebuffer = Kee[int](20)
    SetFence = Kee[int](21)
    WaitFence = Kee[int](22)
    NoPicking = Kee[int](23)
    DebugOverlay = Kee[int](24)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FrameGraphNode'

  #  A C++ Qt3DRender::Render::FrameGraphNode Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_FrameGraphNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> FrameGraphNodeType:
    """
    Calls Qt's 'FrameGraphNodeType
    Qt3DRender::Render::FrameGraphNode::nodeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#nodeType

    Returns
    -------

    FrameGraphNodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FrameGraphNodeType(number)' gives.
    """
    #  FrameGraphNodeType Qt3DRender::Render::FrameGraphNode::nodeType()
    #      const
    return FrameGraphNode.FrameGraphNodeType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14FrameGraphNode8nodeTypeEv',
    ))

  def manager(self) -> Optional[Qt3DRender.Render.FrameGraphManager]:
    """
    Calls Qt's 'FrameGraphManager
    *Qt3DRender::Render::FrameGraphNode::manager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#manager

    Returns
    -------

    Optional[Qt3DRender.Render.FrameGraphManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FrameGraphManager *Qt3DRender::Render::FrameGraphNode::manager() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14FrameGraphNode7managerEv',
    )
    return Qt3DRender.Render.FrameGraphManager._cuteAt(address)

  def parentId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::FrameGraphNode::parentId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#parentId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::FrameGraphNode::parentId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14FrameGraphNode8parentIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def parent(self) -> Optional[FrameGraphNode]:
    """
    Calls Qt's 'FrameGraphNode *Qt3DRender::Render::FrameGraphNode::parent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#parent

    Returns
    -------

    Optional[FrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FrameGraphNode *Qt3DRender::Render::FrameGraphNode::parent() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14FrameGraphNode6parentEv',
    )
    return FrameGraphNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.FrameGraphManager'])
  @overload(NoneType)
  def setFrameGraphManager(
      self,
      manager: Optional[Qt3DRender.Render.FrameGraphManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphNode::setFrameGraphManager(
    FrameGraphManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.FrameGraphManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameGraphNode::setFrameGraphManager(
    #      FrameGraphManager *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14FrameGraphNode20setFrameGraphManager'
        'EPNS0_17FrameGraphManagerE',
        self._addressOf(manager),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setParentId(self, parentId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphNode::setParentId(Qt3DCore::QNodeId
    parentId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#setParentId

    Parameters
    ----------

    parentId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::FrameGraphNode::setParentId(Qt3DCore::QNodeId
    #      parentId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14FrameGraphNode11setParentIdEN8Qt3DCo'
        're7QNodeIdE',
        self._valueOf(parentId),
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
    'Qt3DRender::Render::FrameGraphNode::FrameGraphNode()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html
    """
    #  Qt3DRender::Render::FrameGraphNode::FrameGraphNode()
    self._noteCreation(FrameGraphNode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14FrameGraphNodeC1Ev',
    ))

  @overload(FrameGraphNodeType)
  @overload(FrameGraphNodeType, Qt3DCore.QBackendNode.Mode)
  def __init__(
      self,
      nodeType: FrameGraphNodeType,
      mode: Qt3DCore.QBackendNode.Mode = Qt3DCore.QBackendNode.Mode.ReadOnly,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::FrameGraphNode::FrameGraphNode(FrameGraphNodeType
    nodeType, QBackendNode::Mode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html

    Parameters
    ----------

    nodeType : FrameGraphNodeType
      Passed on as its number.

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DCore.QBackendNode.Mode.ReadOnly.
    """
    #  Qt3DRender::Render::FrameGraphNode::FrameGraphNode(FrameGraphNodeType
    #      nodeType, QBackendNode::Mode mode)
    self._noteCreation(FrameGraphNode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14FrameGraphNodeC1ENS1_18FrameGraphNod'
        'eTypeEN8Qt3DCore12QBackendNode4ModeE',
        nodeType.value, mode.value,
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
    Calls Qt's 'void Qt3DRender::Render::FrameGraphNode::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html#cleanup
    """
    #  void Qt3DRender::Render::FrameGraphNode::cleanup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14FrameGraphNode7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render14FrameGraphNode16syncFromFrontEndEPKN'
        '8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render14FrameGraphNode16syncFromFrontE'
          'ndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def children(*__, **_) -> Never:
    """
    Qt's 'QList<FrameGraphNode *>
    Qt3DRender::Render::FrameGraphNode::children() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrameGraphNode.children' has no cute function "
        "yet. Qt's 'QList<FrameGraphNode *> "
        "Qt3DRender::Render::FrameGraphNode::children() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def childrenIds(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::FrameGraphNode::childrenIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.FrameGraphNode.childrenIds' has no cute "
        "function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::FrameGraphNode::childrenIds() const': gives a "
        "type Python has no way to take yet.")
