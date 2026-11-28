"""
Qt3DAnimation::Animation::BackendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/backendnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::BackendNode to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BackendNode(Qt3DCore.QBackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::BackendNode: a plain Python
  object standing in front of one C++ Qt3DAnimation::Animation::BackendNode.

  It is built on the cute 'Qt3DCore::QBackendNode', as Qt's
  Qt3DAnimation::Animation::BackendNode is built on Qt's
  Qt3DCore::QBackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::BackendNode that has a
  ritual and that Python can call so far, 3 names in all: 'setHandler',
  'syncFromFrontEnd', 'setDirty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::BackendNode::~BackendNode()': the
    destructor: Python never removes a C++
    Qt3DAnimation::Animation::BackendNode.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::BackendNode is created at the first
    use, not by 'Qt3DAnimation::Animation::BackendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::BackendNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::BackendNode'

  #  A C++ Qt3DAnimation::Animation::BackendNode Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Animation_BackendNode'

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

  @overload(WAIT['Qt3DAnimation.Animation.Handler'])
  @overload(NoneType)
  def setHandler(
      self,
      handler: Optional[Qt3DAnimation.Animation.Handler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BackendNode::setHandler(Handler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-backendnode.html

    Parameters
    ----------

    handler : Optional[Qt3DAnimation.Animation.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::BackendNode::setHandler(Handler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation11BackendNode10setHandlerEPNS0_7'
        'HandlerE',
        self._addressOf(handler),
    )

  @overload(Qt3DAnimation.Animation.Handler.DirtyFlag)
  def setDirty(
      self,
      flag: Qt3DAnimation.Animation.Handler.DirtyFlag,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BackendNode::setDirty(Handler::DirtyFlag
    flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-backendnode.html#setDirty

    Parameters
    ----------

    flag : Qt3DAnimation.Animation.Handler.DirtyFlag
      Passed on as its number.
    """
    #  void
    #      Qt3DAnimation::Animation::BackendNode::setDirty(Handler::DirtyFlag
    #      flag)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation11BackendNode8setDirtyENS0_7Hand'
        'ler9DirtyFlagE',
        flag.value,
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
  @overload(Qt3DCore.QBackendNode.Mode)
  def __init__(
      self,
      mode: Qt3DCore.QBackendNode.Mode = Qt3DCore.QBackendNode.Mode.ReadOnly,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::Animation::BackendNode::BackendNode(Qt3DCore::
    QBackendNode::Mode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-backendnode.html

    Parameters
    ----------

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DCore.QBackendNode.Mode.ReadOnly.
    """
    #  Qt3DAnimation::Animation::BackendNode::BackendNode(Qt3DCore::
    #      QBackendNode::Mode mode)
    self._noteCreation(BackendNode, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation11BackendNodeC1EN8Qt3DCore12QBac'
        'kendNode4ModeE',
        mode.value,
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
    Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-backendnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndE'
        'PKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation11BackendNode16syncFromFro'
          'ntEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
