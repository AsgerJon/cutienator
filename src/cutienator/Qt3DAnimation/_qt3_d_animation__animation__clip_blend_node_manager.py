"""
Qt3DAnimation::Animation::ClipBlendNodeManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/managers_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ClipBlendNodeManager to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClipBlendNodeManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ClipBlendNodeManager: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Animation::ClipBlendNodeManager.

  C++ hands a Qt3DAnimation::Animation::ClipBlendNodeManager around as a
  copy, so every C++ Qt3DAnimation::Animation::ClipBlendNodeManager behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ClipBlendNodeManager that
  has a ritual and that Python can call so far, 4 names in all:
  'containsNode', 'appendNode', 'lookupNode', 'releaseNode'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DAnimation::Animation::ClipBlendNodeManager::~ClipBlendNodeManager(
    )': the destructor: Python removes its C++
    Qt3DAnimation::Animation::ClipBlendNodeManager by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ClipBlendNodeManager is created at the
    first use, not by 'Qt3DAnimation::Animation::ClipBlendNodeManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DAnimation::Animation::ClipBlendNodeManager back
    gives a copy the ritual made for Python, in a new cute
    Qt3DAnimation::Animation::ClipBlendNodeManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ClipBlendNodeManager'

  #  Qt's '~Qt3DAnimation::Animation::ClipBlendNodeManager()'. Naming it
  #  makes this a value class: Python owns every C++
  #  Qt3DAnimation::Animation::ClipBlendNodeManager behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerD1Ev')

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
    Qt3DAnimation::Animation::ClipBlendNodeManager::containsNode(Qt3DCore::
    QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodemanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DAnimation::Animation::ClipBlendNodeManager::containsNode(
    #      Qt3DCore::QNodeId id) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager12contain'
        'sNodeEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(
      self,
      id: Qt3DCore.QNodeId,
  ) -> Optional[Qt3DAnimation.Animation.ClipBlendNode]:
    """
    Calls Qt's 'ClipBlendNode
    *Qt3DAnimation::Animation::ClipBlendNodeManager::lookupNode(Qt3DCore::
    QNodeId id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodemanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipBlendNode
    #      *Qt3DAnimation::Animation::ClipBlendNodeManager::lookupNode(
    #      Qt3DCore::QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupN'
        'odeEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DAnimation.Animation.ClipBlendNode._cuteAt(address)

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
    'Qt3DAnimation::Animation::ClipBlendNodeManager::ClipBlendNodeManager()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodemanager.html
    """
    #  Qt3DAnimation::Animation::ClipBlendNodeManager::ClipBlendNodeManager()
    self._noteCreation(ClipBlendNodeManager, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerC1Ev',
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
      WAIT['Qt3DCore.QNodeId'],
      WAIT['Qt3DAnimation.Animation.ClipBlendNode'],
  )
  @overload(WAIT['Qt3DCore.QNodeId'], NoneType)
  def appendNode(
      self,
      id: Qt3DCore.QNodeId,
      node: Optional[Qt3DAnimation.Animation.ClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeManager::appendNode(Qt3DCore::
    QNodeId id, ClipBlendNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodemanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    node : Optional[Qt3DAnimation.Animation.ClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::ClipBlendNodeManager::appendNode(
    #      Qt3DCore::QNodeId id, ClipBlendNode *node)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManager10appendNo'
        'deEN8Qt3DCore7QNodeIdEPNS0_13ClipBlendNodeE',
        self._valueOf(id), self._addressOf(node),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def releaseNode(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNodeManager::releaseNode(Qt3DCore::
    QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnodemanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipBlendNodeManager::releaseNode(
    #      Qt3DCore::QNodeId id)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManager11releaseN'
        'odeEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )
