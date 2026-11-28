"""
QQuickShapeSoftwareRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeSoftwareRenderNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QSGRenderNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import QQuickShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickShape = WAIT['QQuickShape']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeSoftwareRenderNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapeSoftwareRenderNode: a plain Python object
  standing in front of one C++ QQuickShapeSoftwareRenderNode.

  What exists
  -----------

  Every function of Qt's QQuickShapeSoftwareRenderNode that has a ritual and
  that Python can call so far, 5 names in all: 'render', 'releaseResources',
  'changedStates', 'flags', 'rect'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickShapeSoftwareRenderNode::~QQuickShapeSoftwareRenderNode()':
    the destructor: Python never removes a C++ QQuickShapeSoftwareRenderNode.

  What to expect
  --------------

  - The C++ QQuickShapeSoftwareRenderNode is created at the first use, not by
    'QQuickShapeSoftwareRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeSoftwareRenderNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeSoftwareRenderNode'

  #  A C++ QQuickShapeSoftwareRenderNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeSoftwareRenderNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def changedStates(self) -> QSGRenderNode.StateFlags:
    """
    Calls Qt's 'StateFlags QQuickShapeSoftwareRenderNode::changedStates()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html#changedStates

    Returns
    -------

    QSGRenderNode.StateFlags
      The value standing for the combination Qt gave back.
    """
    #  StateFlags QQuickShapeSoftwareRenderNode::changedStates() const
    ritual = 'ritual_ZNK29QQuickShapeSoftwareRenderNode13changedStatesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QQuickShapeSoftwareRenderNode13changedStatesEv')
    return QSGRenderNode.StateFlags(self.uglySide.call(ritual))

  def flags(self) -> QSGRenderNode.RenderingFlags:
    """
    Calls Qt's 'RenderingFlags QQuickShapeSoftwareRenderNode::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html#flags

    Returns
    -------

    QSGRenderNode.RenderingFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderingFlags QQuickShapeSoftwareRenderNode::flags() const
    ritual = 'ritual_ZNK29QQuickShapeSoftwareRenderNode5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickShapeSoftwareRenderNode5flagsEv'
    return QSGRenderNode.RenderingFlags(self.uglySide.call(ritual))

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickShapeSoftwareRenderNode::rect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickShapeSoftwareRenderNode::rect() const
    ritual = 'ritual_ZNK29QQuickShapeSoftwareRenderNode4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickShapeSoftwareRenderNode4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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

  @overload(QQuickShape)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickShape]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickShapeSoftwareRenderNode::QQuickShapeSoftwareRenderNode(QQuickShape
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html

    Parameters
    ----------

    item : Optional[QQuickShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickShapeSoftwareRenderNode::QQuickShapeSoftwareRenderNode(
    #      QQuickShape *item)
    self._noteCreation(QQuickShapeSoftwareRenderNode, lambda: Rituals.call(
        'ritual_ZN29QQuickShapeSoftwareRenderNodeC1EP11QQuickShape',
        self._addressOf(item),
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

  @overload(QSGRenderNode.RenderState)
  @overload(NoneType)
  def render(self, state: Optional[QSGRenderNode.RenderState]) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderNode::render(const RenderState
    *state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html#render

    Parameters
    ----------

    state : Optional[QSGRenderNode.RenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeSoftwareRenderNode::render(const RenderState *state)
    ritual = (
        'ritual_ZN29QQuickShapeSoftwareRenderNode6renderEPKN13QSGRenderNode'
        '11RenderStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickShapeSoftwareRenderNode6renderEPKN13QSGRend'
          'erNode11RenderStateE')
    self.uglySide.call(ritual, self._addressOf(state))

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickShapeSoftwareRenderNode::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapesoftwarerendernode.html
    """
    #  void QQuickShapeSoftwareRenderNode::releaseResources()
    ritual = 'ritual_ZN29QQuickShapeSoftwareRenderNode16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickShapeSoftwareRenderNode16releaseResourcesEv')
    self.uglySide.call(ritual)
