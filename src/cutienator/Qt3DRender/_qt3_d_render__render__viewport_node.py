"""
Qt3DRender::Render::ViewportNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/viewportnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ViewportNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ViewportNode(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::ViewportNode: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ViewportNode.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::ViewportNode is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ViewportNode that has a ritual
  and that Python can call so far, 12 names in all: 'xMin', 'setXMin',
  'yMin', 'setYMin', 'xMax', 'setXMax', 'yMax', 'setYMax', 'gamma',
  'setGamma', 'syncFromFrontEnd', 'computeViewport'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ViewportNode is created at the first use, not
    by 'Qt3DRender::Render::ViewportNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::ViewportNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRectF, THIS)
  @overload(QRectF, NoneType)
  def computeViewport(
      childViewport: QRectF,
      parentViewport: Optional[ViewportNode],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    Qt3DRender::Render::ViewportNode::computeViewport(const QRectF
    &childViewport, const ViewportNode *parentViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html

    Parameters
    ----------

    childViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    parentViewport : Optional[ViewportNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DRender::Render::ViewportNode::computeViewport(const QRectF
    #      &childViewport, const ViewportNode *parentViewport)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode15computeViewportERK6QRe'
        'ctFPKS1_',
        CuteMixin._valueOf(childViewport),
        CuteMixin._addressOf(parentViewport),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::ViewportNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def xMin(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ViewportNode::xMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#xMin
    """
    #  float Qt3DRender::Render::ViewportNode::xMin() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ViewportNode4xMinEv',
    )

  def yMin(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ViewportNode::yMin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#yMin
    """
    #  float Qt3DRender::Render::ViewportNode::yMin() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ViewportNode4yMinEv',
    )

  def xMax(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ViewportNode::xMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#xMax
    """
    #  float Qt3DRender::Render::ViewportNode::xMax() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ViewportNode4xMaxEv',
    )

  def yMax(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ViewportNode::yMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#yMax
    """
    #  float Qt3DRender::Render::ViewportNode::yMax() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ViewportNode4yMaxEv',
    )

  def gamma(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::Render::ViewportNode::gamma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#gamma
    """
    #  float Qt3DRender::Render::ViewportNode::gamma() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12ViewportNode5gammaEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXMin(self, xMin: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::setXMin(float xMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#setXMin

    Parameters
    ----------

    xMin : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::setXMin(float xMin)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode7setXMinEf', xMin,
    )

  @overload(float)
  def setYMin(self, yMin: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::setYMin(float yMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#setYMin

    Parameters
    ----------

    yMin : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::setYMin(float yMin)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode7setYMinEf', yMin,
    )

  @overload(float)
  def setXMax(self, xMax: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::setXMax(float xMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#setXMax

    Parameters
    ----------

    xMax : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::setXMax(float xMax)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode7setXMaxEf', xMax,
    )

  @overload(float)
  def setYMax(self, yMax: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::setYMax(float yMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#setYMax

    Parameters
    ----------

    yMax : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::setYMax(float yMax)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode7setYMaxEf', yMax,
    )

  @overload(float)
  def setGamma(self, gamma: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::setGamma(float
    gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#setGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::setGamma(float gamma)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNode8setGammaEf', gamma,
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
    'Qt3DRender::Render::ViewportNode::ViewportNode()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html#ViewportNode
    """
    #  Qt3DRender::Render::ViewportNode::ViewportNode()
    self._noteCreation(ViewportNode, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12ViewportNodeC1Ev',
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
    Calls Qt's 'void Qt3DRender::Render::ViewportNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-viewportnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::ViewportNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render12ViewportNode16syncFromFrontEndEPKN8Q'
        't3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render12ViewportNode16syncFromFrontEnd'
          'EPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
