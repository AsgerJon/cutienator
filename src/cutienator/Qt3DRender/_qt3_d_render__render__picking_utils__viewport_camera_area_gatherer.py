"""
Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer to
#  be private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ViewportCameraAreaGatherer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer.

  C++ hands a Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer
  around as a copy, so every C++
  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's
  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer that has a
  ritual and that Python can call so far, 2 names in all: 'visit',
  'gatherUpViewportCameraAreas'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::vector<ViewportCameraAreaDetails>
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::gather(
    FrameGraphNode *root)': gives a type Python has no way to take yet.
  - Qt's 'bool
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::isUnique(
    const std::vector<ViewportCameraAreaDetails> &vcaList, const
    ViewportCameraAreaDetails &vca) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    ~ViewportCameraAreaGatherer()': the destructor: Python removes its C++
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer is
    created at the first use, not by
    'Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer.
  - Each name of Qt's
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer that has no
    cute function yet, 'gather', 'isUnique', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer'

  #  Qt's '~Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer()'.
  #  Naming it makes this a value class: Python owns every C++
  #  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGathererD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'])
  @overload(NoneType)
  def gatherUpViewportCameraAreas(
      self,
      node: Optional[Qt3DRender.Render.FrameGraphNode],
  ) -> Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails:
    """
    Calls Qt's 'ViewportCameraAreaDetails
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    gatherUpViewportCameraAreas(Render::FrameGraphNode *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-viewportcameraareagatherer.html

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails
      A new cute Qt3DRender::Render::PickingUtils::ViewportCameraAreaDetails
      around the copy Qt gave back. Python owns it.
    """
    #  ViewportCameraAreaDetails
    #      Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    #      gatherUpViewportCameraAreas(Render::FrameGraphNode *node) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGat'
        'herer27gatherUpViewportCameraAreasEPNS0_14FrameGraphNodeE',
        self._addressOf(node),
    )
    return Qt3DRender.Render.PickingUtils.ViewportCameraAreaDetails._cuteOwning(address)

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
  @overload(WAIT['Qt3DCore.QNodeId'])
  def __init__(self, nodeId: Optional[Qt3DCore.QNodeId] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    ViewportCameraAreaGatherer(const Qt3DCore::QNodeId &nodeId)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-viewportcameraareagatherer.html

    Parameters
    ----------

    nodeId : Optional[Qt3DCore.QNodeId]
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own. May be left out, as in Qt: a new 'Qt3DCore.QNodeId()' is
      then passed on.
    """
    #  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    #      ViewportCameraAreaGatherer(const Qt3DCore::QNodeId &nodeId)
    if nodeId is None:
      nodeId = Qt3DCore.QNodeId()
    self._noteCreation(ViewportCameraAreaGatherer, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGath'
        'ererC1ERKN8Qt3DCore7QNodeIdE',
        self._valueOf(nodeId),
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

  @overload(WAIT['Qt3DRender.Render.FrameGraphNode'])
  @overload(NoneType)
  def visit(self, node: Optional[Qt3DRender.Render.FrameGraphNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::visit(
    FrameGraphNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-pickingutils-viewportcameraareagatherer.html

    Parameters
    ----------

    node : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::
    #      visit(FrameGraphNode *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGath'
        'erer5visitEPNS0_14FrameGraphNodeE',
        self._addressOf(node),
    )

  @staticmethod
  def gather(*__, **_) -> Never:
    """
    Qt's 'std::vector<ViewportCameraAreaDetails>
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::gather(
    FrameGraphNode *root)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.ViewportCameraAreaGatherer.gather' "
        "has no cute function yet. Qt's "
        "'std::vector<ViewportCameraAreaDetails> "
        "Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::gathe"
        "r(FrameGraphNode *root)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def isUnique(*__, **_) -> Never:
    """
    Qt's 'bool
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::isUnique(
    const std::vector<ViewportCameraAreaDetails> &vcaList, const
    ViewportCameraAreaDetails &vca) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.PickingUtils.ViewportCameraAreaGatherer.isUnique"
        "' has no cute function yet. Qt's 'bool "
        "Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::isUni"
        "que(const std::vector<ViewportCameraAreaDetails> &vcaList, const "
        "ViewportCameraAreaDetails &vca) const': takes a type Python has no "
        "way to hand over yet.")
