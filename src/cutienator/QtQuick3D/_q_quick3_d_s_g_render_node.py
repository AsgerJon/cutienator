"""
QQuick3DSGRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DSGRenderNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtQuick import QSGRenderNode


class QQuick3DSGRenderNode(QSGRenderNode):
  """
  The cute side of Qt's QQuick3DSGRenderNode: a plain Python object standing
  in front of one C++ QQuick3DSGRenderNode.

  It is built on the cute 'QSGRenderNode', as Qt's QQuick3DSGRenderNode is
  built on Qt's QSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSGRenderNode that has a ritual and that
  Python can call so far, 3 names in all: 'changedStates',
  'releaseResources', 'flags'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DSGRenderNode::~QQuick3DSGRenderNode()': the destructor:
    Python never removes a C++ QQuick3DSGRenderNode.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuick3DSGRenderNode is created at the first use, not by
    'QQuick3DSGRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSGRenderNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSGRenderNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def changedStates(self) -> QSGRenderNode.StateFlags:
    """
    Calls Qt's 'StateFlags QQuick3DSGRenderNode::changedStates() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgrendernode.html#changedStates

    Returns
    -------

    QSGRenderNode.StateFlags
      The value standing for the combination Qt gave back.
    """
    #  StateFlags QQuick3DSGRenderNode::changedStates() const
    return QSGRenderNode.StateFlags(self.uglySide.call(
        'ritual_ZNK20QQuick3DSGRenderNode13changedStatesEv',
    ))

  def flags(self) -> QSGRenderNode.RenderingFlags:
    """
    Calls Qt's 'RenderingFlags QQuick3DSGRenderNode::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dsgrendernode.html#flags

    Returns
    -------

    QSGRenderNode.RenderingFlags
      The value standing for the combination Qt gave back.
    """
    #  RenderingFlags QQuick3DSGRenderNode::flags() const
    return QSGRenderNode.RenderingFlags(self.uglySide.call(
        'ritual_ZNK20QQuick3DSGRenderNode5flagsEv',
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

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DSGRenderNode::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsgrendernode.html#releaseResources
    """
    #  void QQuick3DSGRenderNode::releaseResources()
    self.uglySide.call('ritual_ZN20QQuick3DSGRenderNode16releaseResourcesEv')
