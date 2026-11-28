"""
Qt3DAnimation::Animation::ClipBlendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ClipBlendNode to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClipBlendNode(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ClipBlendNode: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ClipBlendNode.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::ClipBlendNode is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ClipBlendNode that has a
  ritual and that Python can call so far, 4 names in all:
  'setClipBlendNodeManager', 'clipBlendNodeManager', 'blend', 'duration'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::ClipBlendNode::~ClipBlendNode()': the
    destructor: Python never removes a C++
    Qt3DAnimation::Animation::ClipBlendNode.
  - Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNode::setClipResults(Qt3DCore::QNodeId
    animatorId, const ClipResults &clipResults)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ClipResults
    Qt3DAnimation::Animation::ClipBlendNode::clipResults(Qt3DCore::QNodeId
    animatorId) const': gives a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendNode::allDependencyIds() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendNode::currentDependencyIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'ClipResults Qt3DAnimation::Animation::ClipBlendNode::doBlend(const
    QList<ClipResults> &blendData) const': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ClipBlendNode is created at the first
    use, not by 'Qt3DAnimation::Animation::ClipBlendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::ClipBlendNode.
  - Each name of Qt's Qt3DAnimation::Animation::ClipBlendNode that has no
    cute function yet, '__init__', 'allDependencyIds', 'blendType',
    'clipResults', 'currentDependencyIds', 'doBlend', 'setClipResults', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DAnimation::Animation::ClipBlendNode, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class BlendType(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::ClipBlendNode::BlendType' of Qt, with
    the 4 names Qt gives in it.
    """

    NoneBlendType = Kee[int](0)
    LerpBlendType = Kee[int](1)
    AdditiveBlendType = Kee[int](2)
    ValueType = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ClipBlendNode'

  #  A C++ Qt3DAnimation::Animation::ClipBlendNode Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Animation_ClipBlendNode'

  #  The functions Qt calls itself that
  #  Qt3DAnimation::Animation::ClipBlendNode is the first to declare and that
  #  cannot be handed to Python yet, each as Qt declares it. A class of a
  #  program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'allDependencyIds': (
          'QList<Qt3DCore::QNodeId> '
          'Qt3DAnimation::Animation::ClipBlendNode::allDependencyIds() '
          'const',
      ),
      'currentDependencyIds': (
          'QList<Qt3DCore::QNodeId> '
          'Qt3DAnimation::Animation::ClipBlendNode::currentDependencyIds() '
          'const',
      ),
      'doBlend': (
          'ClipResults '
          'Qt3DAnimation::Animation::ClipBlendNode::doBlend(const '
          'QList<ClipResults> &) const',
      ),
  }

  #  The functions Qt calls itself that
  #  Qt3DAnimation::Animation::ClipBlendNode is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'duration': (
          ('_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv',
           ('double', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clipBlendNodeManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]:
    """
    Calls Qt's 'ClipBlendNodeManager
    *Qt3DAnimation::Animation::ClipBlendNode::clipBlendNodeManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnode.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipBlendNodeManager
    #      *Qt3DAnimation::Animation::ClipBlendNode::clipBlendNodeManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode20clipBlendNodeM'
        'anagerEv',
    )
    return Qt3DAnimation.Animation.ClipBlendNodeManager._cuteAt(address)

  def duration(self) -> float:
    """
    Calls Qt's 'double Qt3DAnimation::Animation::ClipBlendNode::duration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnode.html
    """
    #  double Qt3DAnimation::Animation::ClipBlendNode::duration() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DAnimation.Animation.ClipBlendNodeManager'])
  @overload(NoneType)
  def setClipBlendNodeManager(
      self,
      manager: Optional[Qt3DAnimation.Animation.ClipBlendNodeManager],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNode::setClipBlendNodeManager(
    ClipBlendNodeManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnode.html

    Parameters
    ----------

    manager : Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::ClipBlendNode::setClipBlendNodeManager(
    #      ClipBlendNodeManager *manager)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13ClipBlendNode23setClipBlendNod'
        'eManagerEPNS0_20ClipBlendNodeManagerE',
        self._addressOf(manager),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DAnimation::Animation::ClipBlendNode::ClipBlendNode(BlendType
    blendType)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::Animation::ClipBlendNode::ClipBlendNode(BlendType "
        "blendType)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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
  def blend(self, animatorId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNode::blend(Qt3DCore::QNodeId
    animatorId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendnode.html#blend

    Parameters
    ----------

    animatorId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipBlendNode::blend(Qt3DCore::QNodeId
    #      animatorId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13ClipBlendNode5blendEN8Qt3DCore'
        '7QNodeIdE',
        self._valueOf(animatorId),
    )

  @staticmethod
  def allDependencyIds(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendNode::allDependencyIds() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.allDependencyIds' has no "
        "cute function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DAnimation::Animation::ClipBlendNode::allDependencyIds() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def blendType(*__, **_) -> Never:
    """
    Qt's 'BlendType Qt3DAnimation::Animation::ClipBlendNode::blendType()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'ClipBlendNode'; did you mean 'Animation::ClipBlendNode'?.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.blendType' has no cute "
        "function yet. Qt's 'BlendType "
        "Qt3DAnimation::Animation::ClipBlendNode::blendType() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'ClipBlendNode'; did you mean 'Animation::ClipBlendNode'?.")

  @staticmethod
  def clipResults(*__, **_) -> Never:
    """
    Qt's 'ClipResults
    Qt3DAnimation::Animation::ClipBlendNode::clipResults(Qt3DCore::QNodeId
    animatorId) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.clipResults' has no cute "
        "function yet. Qt's 'ClipResults "
        "Qt3DAnimation::Animation::ClipBlendNode::clipResults(Qt3DCore::QNod"
        "eId animatorId) const': gives a type Python has no way to take yet."
    )

  @staticmethod
  def currentDependencyIds(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendNode::currentDependencyIds() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.currentDependencyIds' has "
        "no cute function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DAnimation::Animation::ClipBlendNode::currentDependencyIds() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def doBlend(*__, **_) -> Never:
    """
    Qt's 'ClipResults Qt3DAnimation::Animation::ClipBlendNode::doBlend(const
    QList<ClipResults> &blendData) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.doBlend' has no cute "
        "function yet. Qt's 'ClipResults "
        "Qt3DAnimation::Animation::ClipBlendNode::doBlend(const "
        "QList<ClipResults> &blendData) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def setClipResults(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::ClipBlendNode::setClipResults(Qt3DCore::QNodeId
    animatorId, const ClipResults &clipResults)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipBlendNode.setClipResults' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipBlendNode::setClipResults(Qt3DCore::Q"
        "NodeId animatorId, const ClipResults &clipResults)': takes a type "
        "Python has no way to hand over yet.")
