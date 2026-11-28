"""
QSGOpacityNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSGNode


class QSGOpacityNode(QSGNode):
  """
  The cute side of Qt's QSGOpacityNode: a plain Python object standing in
  front of one C++ QSGOpacityNode.

  It is built on the cute 'QSGNode', as Qt's QSGOpacityNode is built on Qt's
  QSGNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGOpacityNode that has a ritual and that Python can
  call so far, 5 names in all: 'setOpacity', 'opacity', 'setCombinedOpacity',
  'combinedOpacity', 'isSubtreeBlocked'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGOpacityNode::~QSGOpacityNode()': the destructor: Python never
    removes a C++ QSGOpacityNode.

  What to expect
  --------------

  - The C++ QSGOpacityNode is created at the first use, not by
    'QSGOpacityNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGOpacityNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGOpacityNode'

  #  A C++ QSGOpacityNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGOpacityNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QSGOpacityNode::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgopacitynode.html#opacity
    """
    #  qreal QSGOpacityNode::opacity() const
    return self.uglySide.call('ritual_ZNK14QSGOpacityNode7opacityEv')

  def combinedOpacity(self) -> float:
    """
    Calls Qt's 'qreal QSGOpacityNode::combinedOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopacitynode.html#combinedOpacity
    """
    #  qreal QSGOpacityNode::combinedOpacity() const
    return self.uglySide.call(
        'ritual_ZNK14QSGOpacityNode15combinedOpacityEv',
    )

  def isSubtreeBlocked(self) -> bool:
    """
    Calls Qt's 'bool QSGOpacityNode::isSubtreeBlocked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopacitynode.html#isSubtreeBlocked
    """
    #  bool QSGOpacityNode::isSubtreeBlocked() const
    ritual = 'ritual_ZNK14QSGOpacityNode16isSubtreeBlockedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSGOpacityNode16isSubtreeBlockedEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSGOpacityNode::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgopacitynode.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSGOpacityNode::setOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN14QSGOpacityNode10setOpacityEd', opacity)

  @overload(float)
  def setCombinedOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSGOpacityNode::setCombinedOpacity(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgopacitynode.html#setCombinedOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSGOpacityNode::setCombinedOpacity(qreal opacity)
    self.uglySide.call(
        'ritual_ZN14QSGOpacityNode18setCombinedOpacityEd', opacity,
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
    Notes what was given, for Qt's 'QSGOpacityNode::QSGOpacityNode()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgopacitynode.html#QSGOpacityNode
    """
    #  QSGOpacityNode::QSGOpacityNode()
    self._noteCreation(QSGOpacityNode, lambda: Rituals.call(
        'ritual_ZN14QSGOpacityNodeC1Ev',
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
