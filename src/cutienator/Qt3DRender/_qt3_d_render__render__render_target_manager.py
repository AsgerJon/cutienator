"""
Qt3DRender::Render::RenderTargetManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::RenderTargetManager to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class RenderTargetManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::RenderTargetManager: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::RenderTargetManager.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderTargetManager that has a
  ritual and that Python can call so far, 2 names in all:
  'addRenderTargetIdToCleanup', 'removeRenderTargetToCleanup'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderTargetManager::takeRenderTargetIdsToCleanup()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderTargetManager is created at the first
    use, not by 'Qt3DRender::Render::RenderTargetManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderTargetManager.
  - Each name of Qt's Qt3DRender::Render::RenderTargetManager that has no
    cute function yet, 'takeRenderTargetIdsToCleanup', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderTargetManager'

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
    'Qt3DRender::Render::RenderTargetManager::RenderTargetManager()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetmanager.html
    """
    #  Qt3DRender::Render::RenderTargetManager::RenderTargetManager()
    self._noteCreation(RenderTargetManager, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render19RenderTargetManagerC1Ev',
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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addRenderTargetIdToCleanup(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderTargetManager::addRenderTargetIdToCleanup(
    Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderTargetManager::
    #      addRenderTargetIdToCleanup(Qt3DCore::QNodeId id)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render19RenderTargetManager26addRenderTarget'
        'IdToCleanupEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeRenderTargetToCleanup(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderTargetManager::removeRenderTargetToCleanup(
    Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-rendertargetmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::RenderTargetManager::
    #      removeRenderTargetToCleanup(Qt3DCore::QNodeId id)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render19RenderTargetManager27removeRenderTar'
        'getToCleanupEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @staticmethod
  def takeRenderTargetIdsToCleanup(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::RenderTargetManager::takeRenderTargetIdsToCleanup()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderTargetManager.takeRenderTargetIdsToCleanup"
        "' has no cute function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::RenderTargetManager::takeRenderTargetIdsToClean"
        "up()': gives a type Python has no way to take yet.")
