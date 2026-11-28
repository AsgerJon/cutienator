"""
Qt3DRender::Render::JointManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::JointManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class JointManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::JointManager: a plain Python
  object standing in front of one C++ Qt3DRender::Render::JointManager.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::JointManager that has a ritual
  and that Python can call so far, 2 names in all: 'addDirtyJoint',
  'removeDirtyJoint'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<HJoint> Qt3DRender::Render::JointManager::dirtyJoints()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::JointManager is created at the first use, not
    by 'Qt3DRender::Render::JointManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::JointManager.
  - Each name of Qt's Qt3DRender::Render::JointManager that has no cute
    function yet, 'dirtyJoints', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::JointManager'

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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addDirtyJoint(self, jointId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::JointManager::addDirtyJoint(Qt3DCore::QNodeId
    jointId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-jointmanager.html#addDirtyJoint

    Parameters
    ----------

    jointId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::JointManager::addDirtyJoint(Qt3DCore::QNodeId
    #      jointId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12JointManager13addDirtyJointEN8Qt3DCo'
        're7QNodeIdE',
        self._valueOf(jointId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeDirtyJoint(self, jointId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::JointManager::removeDirtyJoint(Qt3DCore::QNodeId
    jointId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-jointmanager.html

    Parameters
    ----------

    jointId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::JointManager::removeDirtyJoint(Qt3DCore::
    #      QNodeId jointId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12JointManager16removeDirtyJointEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(jointId),
    )

  @staticmethod
  def dirtyJoints(*__, **_) -> Never:
    """
    Qt's 'QList<HJoint> Qt3DRender::Render::JointManager::dirtyJoints()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.JointManager.dirtyJoints' has no cute function "
        "yet. Qt's 'QList<HJoint> "
        "Qt3DRender::Render::JointManager::dirtyJoints()': gives a type "
        "Python has no way to take yet.")
