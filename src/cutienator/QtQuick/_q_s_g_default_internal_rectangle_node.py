"""
QSGDefaultInternalRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGDefaultInternalRectangleNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSGBasicInternalRectangleNode


class QSGDefaultInternalRectangleNode(QSGBasicInternalRectangleNode):
  """
  The cute side of Qt's QSGDefaultInternalRectangleNode: a plain Python
  object standing in front of one C++ QSGDefaultInternalRectangleNode.

  It is built on the cute 'QSGBasicInternalRectangleNode', as Qt's
  QSGDefaultInternalRectangleNode is built on Qt's
  QSGBasicInternalRectangleNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultInternalRectangleNode that has a ritual
  and that Python can call so far, 1 name in all:
  'updateMaterialAntialiasing'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QSGDefaultInternalRectangleNode::updateMaterialBlending(QSGNode::
    DirtyState *state)': names 'QSGNode::DirtyState', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QSGDefaultInternalRectangleNode is created at the first use, not
    by 'QSGDefaultInternalRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultInternalRectangleNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultInternalRectangleNode'

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
    'QSGDefaultInternalRectangleNode::QSGDefaultInternalRectangleNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalrectanglenode.html
    """
    #  QSGDefaultInternalRectangleNode::QSGDefaultInternalRectangleNode()
    self._noteCreation(QSGDefaultInternalRectangleNode, lambda: Rituals.call(
        'ritual_ZN31QSGDefaultInternalRectangleNodeC1Ev',
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

  def updateMaterialAntialiasing(self) -> None:
    """
    Calls Qt's 'void
    QSGDefaultInternalRectangleNode::updateMaterialAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultinternalrectanglenode.html
    """
    #  void QSGDefaultInternalRectangleNode::updateMaterialAntialiasing()
    ritual = (
        'ritual_ZN31QSGDefaultInternalRectangleNode26updateMaterialAntialia'
        'singEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN31QSGDefaultInternalRectangleNode26updateMaterialAn'
          'tialiasingEv')
    self.uglySide.call(ritual)
