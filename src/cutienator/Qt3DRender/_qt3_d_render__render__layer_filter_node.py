"""
Qt3DRender::Render::LayerFilterNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/layerfilternode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::LayerFilterNode to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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


class LayerFilterNode(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::LayerFilterNode: a plain Python
  object standing in front of one C++ Qt3DRender::Render::LayerFilterNode.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::LayerFilterNode is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LayerFilterNode that has a
  ritual and that Python can call so far, 2 names in all: 'syncFromFrontEnd',
  'filterMode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QNodeIdVector
    Qt3DRender::Render::LayerFilterNode::layerIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::LayerFilterNode::setLayerIds(const
    Qt3DCore::QNodeIdVector &list)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LayerFilterNode is created at the first use,
    not by 'Qt3DRender::Render::LayerFilterNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LayerFilterNode.
  - Each name of Qt's Qt3DRender::Render::LayerFilterNode that has no cute
    function yet, 'layerIds', 'setLayerIds', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::LayerFilterNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filterMode(self) -> Qt3DRender.QLayerFilter.FilterMode:
    """
    Calls Qt's 'QLayerFilter::FilterMode
    Qt3DRender::Render::LayerFilterNode::filterMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-layerfilternode.html#filterMode

    Returns
    -------

    Qt3DRender.QLayerFilter.FilterMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QLayerFilter.FilterMode(number)' gives.
    """
    #  QLayerFilter::FilterMode
    #      Qt3DRender::Render::LayerFilterNode::filterMode() const
    return Qt3DRender.QLayerFilter.FilterMode(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15LayerFilterNode10filterModeEv',
    ))

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
    'Qt3DRender::Render::LayerFilterNode::LayerFilterNode()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-layerfilternode.html
    """
    #  Qt3DRender::Render::LayerFilterNode::LayerFilterNode()
    self._noteCreation(LayerFilterNode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render15LayerFilterNodeC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LayerFilterNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-layerfilternode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::LayerFilterNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render15LayerFilterNode16syncFromFrontEndEPK'
        'N8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render15LayerFilterNode16syncFromFront'
          'EndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def layerIds(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeIdVector
    Qt3DRender::Render::LayerFilterNode::layerIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LayerFilterNode.layerIds' has no cute function "
        "yet. Qt's 'Qt3DCore::QNodeIdVector "
        "Qt3DRender::Render::LayerFilterNode::layerIds() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setLayerIds(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::LayerFilterNode::setLayerIds(const
    Qt3DCore::QNodeIdVector &list)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LayerFilterNode.setLayerIds' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::LayerFilterNode::setLayerIds(const "
        "Qt3DCore::QNodeIdVector &list)': takes a type Python has no way to "
        "hand over yet.")
