"""
Qt3DRender::Render::FrameGraphManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::FrameGraphManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FrameGraphManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::FrameGraphManager: a plain Python
  object standing in front of one C++ Qt3DRender::Render::FrameGraphManager.

  C++ hands a Qt3DRender::Render::FrameGraphManager around as a copy, so
  every C++ Qt3DRender::Render::FrameGraphManager behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::FrameGraphManager that has a
  ritual and that Python can call so far, 4 names in all: 'containsNode',
  'appendNode', 'lookupNode', 'releaseNode'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::FrameGraphManager::~FrameGraphManager()': the
    destructor: Python removes its C++ Qt3DRender::Render::FrameGraphManager
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::FrameGraphManager is created at the first
    use, not by 'Qt3DRender::Render::FrameGraphManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::FrameGraphManager back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::Render::FrameGraphManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::FrameGraphManager'

  #  Qt's '~Qt3DRender::Render::FrameGraphManager()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::FrameGraphManager
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render17FrameGraphManagerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def containsNode(self, id: Qt3DCore.QNodeId) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::FrameGraphManager::containsNode(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DRender::Render::FrameGraphManager::containsNode(Qt3DCore::
    #      QNodeId id) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render17FrameGraphManager12containsNodeEN8Q'
        't3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(
      self,
      id: Qt3DCore.QNodeId,
  ) -> Optional[Qt3DRender.Render.FrameGraphNode]:
    """
    Calls Qt's 'FrameGraphNode
    *Qt3DRender::Render::FrameGraphManager::lookupNode(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DRender.Render.FrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FrameGraphNode
    #      *Qt3DRender::Render::FrameGraphManager::lookupNode(Qt3DCore::
    #      QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render17FrameGraphManager10lookupNodeEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DRender.Render.FrameGraphNode._cuteAt(address)

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
    'Qt3DRender::Render::FrameGraphManager::FrameGraphManager()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphmanager.html
    """
    #  Qt3DRender::Render::FrameGraphManager::FrameGraphManager()
    self._noteCreation(FrameGraphManager, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render17FrameGraphManagerC1Ev',
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

  @overload(
      WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DRender.Render.FrameGraphNode'],
  )
  @overload(WAIT['Qt3DCore.QNodeId'], NoneType)
  def appendNode(
      self,
      id: Qt3DCore.QNodeId,
      node: Optional[Qt3DRender.Render.FrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphManager::appendNode(Qt3DCore::QNodeId id,
    FrameGraphNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    node : Optional[Qt3DRender.Render.FrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::FrameGraphManager::appendNode(Qt3DCore::
    #      QNodeId id, FrameGraphNode *node)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrameGraphManager10appendNodeEN8Qt3D'
        'Core7QNodeIdEPNS0_14FrameGraphNodeE',
        self._valueOf(id), self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def releaseNode(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::FrameGraphManager::releaseNode(Qt3DCore::QNodeId
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-framegraphmanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::FrameGraphManager::releaseNode(Qt3DCore::
    #      QNodeId id)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render17FrameGraphManager11releaseNodeEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(id),
    )
