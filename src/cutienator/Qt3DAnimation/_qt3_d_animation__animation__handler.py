"""
Qt3DAnimation::Animation::Handler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/handler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DAnimation::Animation::Handler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Handler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DAnimation::Animation::Handler: a plain Python
  object standing in front of one C++ Qt3DAnimation::Animation::Handler.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::Handler that has a ritual
  and that Python can call so far, 10 names in all: 'simulationTime',
  'setDirty', 'animationClipLoaderManager', 'clockManager',
  'clipAnimatorManager', 'blendedClipAnimatorManager',
  'channelMappingManager', 'channelMapperManager', 'clipBlendNodeManager',
  'skeletonManager'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::Handler::~Handler()': the destructor:
    Python never removes a C++ Qt3DAnimation::Animation::Handler.
  - Qt's 'void
    Qt3DAnimation::Animation::Handler::setClipAnimatorRunning(const
    HClipAnimator &handle, bool running)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QVector<HClipAnimator>
    Qt3DAnimation::Animation::Handler::runningClipAnimators() const': gives a
    type Python has no way to take yet.
  - Qt's 'void
    Qt3DAnimation::Animation::Handler::setBlendedClipAnimatorRunning(const
    HBlendedClipAnimator &handle, bool running)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QVector<HBlendedClipAnimator>
    Qt3DAnimation::Animation::Handler::runningBlenndedClipAnimators() const':
    gives a type Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
    QVector<HAnimationClip> *clips)': names
    'QVector<Qt3DAnimation::Animation::HAnimationClip>', which has no cute
    class yet.
  - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
    QVector<HClipAnimator> *animators)': names
    'QVector<Qt3DAnimation::Animation::HClipAnimator>', which has no cute
    class yet.
  - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
    QVector<HBlendedClipAnimator> *animators)': names
    'QVector<Qt3DAnimation::Animation::HBlendedClipAnimator>', which has no
    cute class yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::Handler is created at the first use,
    not by 'Qt3DAnimation::Animation::Handler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::Handler.
  - Each name of Qt's Qt3DAnimation::Animation::Handler that has no cute
    function yet, '__init__', 'cleanupHandleList', 'jobsToExecute',
    'runningBlenndedClipAnimators', 'runningClipAnimators',
    'setBlendedClipAnimatorRunning', 'setClipAnimatorRunning', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DAnimation::Animation::Handler, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DirtyFlag(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::Handler::DirtyFlag' of Qt, with the 4
    names Qt gives in it.
    """

    AnimationClipDirty = Kee[int](0)
    ChannelMappingsDirty = Kee[int](1)
    ClipAnimatorDirty = Kee[int](2)
    BlendedClipAnimatorDirty = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::Handler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def simulationTime(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DAnimation::Animation::Handler::simulationTime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html
    """
    #  qint64 Qt3DAnimation::Animation::Handler::simulationTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler14simulationTimeEv',
    )

  def animationClipLoaderManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.AnimationClipLoaderManager]:
    """
    Calls Qt's 'AnimationClipLoaderManager
    *Qt3DAnimation::Animation::Handler::animationClipLoaderManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.AnimationClipLoaderManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AnimationClipLoaderManager
    #      *Qt3DAnimation::Animation::Handler::animationClipLoaderManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler26animationClipLoaderMa'
        'nagerEv',
    )
    return Qt3DAnimation.Animation.AnimationClipLoaderManager._cuteAt(address)

  def clockManager(self) -> Optional[Qt3DAnimation.Animation.ClockManager]:
    """
    Calls Qt's 'ClockManager
    *Qt3DAnimation::Animation::Handler::clockManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html#clockManager

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ClockManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClockManager *Qt3DAnimation::Animation::Handler::clockManager() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler12clockManagerEv',
    )
    return Qt3DAnimation.Animation.ClockManager._cuteAt(address)

  def clipAnimatorManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.ClipAnimatorManager]:
    """
    Calls Qt's 'ClipAnimatorManager
    *Qt3DAnimation::Animation::Handler::clipAnimatorManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ClipAnimatorManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipAnimatorManager
    #      *Qt3DAnimation::Animation::Handler::clipAnimatorManager() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler19clipAnimatorManagerEv',
    )
    return Qt3DAnimation.Animation.ClipAnimatorManager._cuteAt(address)

  def blendedClipAnimatorManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.BlendedClipAnimatorManager]:
    """
    Calls Qt's 'BlendedClipAnimatorManager
    *Qt3DAnimation::Animation::Handler::blendedClipAnimatorManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.BlendedClipAnimatorManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BlendedClipAnimatorManager
    #      *Qt3DAnimation::Animation::Handler::blendedClipAnimatorManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler26blendedClipAnimatorMa'
        'nagerEv',
    )
    return Qt3DAnimation.Animation.BlendedClipAnimatorManager._cuteAt(address)

  def channelMappingManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.ChannelMappingManager]:
    """
    Calls Qt's 'ChannelMappingManager
    *Qt3DAnimation::Animation::Handler::channelMappingManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ChannelMappingManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChannelMappingManager
    #      *Qt3DAnimation::Animation::Handler::channelMappingManager() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler21channelMappingManager'
        'Ev',
    )
    return Qt3DAnimation.Animation.ChannelMappingManager._cuteAt(address)

  def channelMapperManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.ChannelMapperManager]:
    """
    Calls Qt's 'ChannelMapperManager
    *Qt3DAnimation::Animation::Handler::channelMapperManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ChannelMapperManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChannelMapperManager
    #      *Qt3DAnimation::Animation::Handler::channelMapperManager() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler20channelMapperManagerE'
        'v',
    )
    return Qt3DAnimation.Animation.ChannelMapperManager._cuteAt(address)

  def clipBlendNodeManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]:
    """
    Calls Qt's 'ClipBlendNodeManager
    *Qt3DAnimation::Animation::Handler::clipBlendNodeManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.ClipBlendNodeManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClipBlendNodeManager
    #      *Qt3DAnimation::Animation::Handler::clipBlendNodeManager() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler20clipBlendNodeManagerE'
        'v',
    )
    return Qt3DAnimation.Animation.ClipBlendNodeManager._cuteAt(address)

  def skeletonManager(
      self,
  ) -> Optional[Qt3DAnimation.Animation.SkeletonManager]:
    """
    Calls Qt's 'SkeletonManager
    *Qt3DAnimation::Animation::Handler::skeletonManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.SkeletonManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SkeletonManager *Qt3DAnimation::Animation::Handler::skeletonManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation7Handler15skeletonManagerEv',
    )
    return Qt3DAnimation.Animation.SkeletonManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DirtyFlag, WAIT['Qt3DCore.QNodeId'])
  def setDirty(self, flag: DirtyFlag, nodeId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::Handler::setDirty(DirtyFlag
    flag, Qt3DCore::QNodeId nodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-handler.html#setDirty

    Parameters
    ----------

    flag : DirtyFlag
      Passed on as its number.

    nodeId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::Handler::setDirty(DirtyFlag flag,
    #      Qt3DCore::QNodeId nodeId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation7Handler8setDirtyENS1_9DirtyFlag'
        'EN8Qt3DCore7QNodeIdE',
        flag.value, self._valueOf(nodeId),
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
    Qt's 'Qt3DAnimation::Animation::Handler::Handler()': leans on
    'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimation::
    Animation::ChannelMapping*> const&,
    QList<Qt3DAnimation::Animation::ChannelNameAndType> const&,
    QList<QList<long long> > const&, QList<QBitArray> const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.__init__' has no cute function "
        "yet. Qt's 'Qt3DAnimation::Animation::Handler::Handler()': leans on "
        "'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimatio"
        "n::Animation::ChannelMapping*> const&, "
        "QList<Qt3DAnimation::Animation::ChannelNameAndType> const&, "
        "QList<QList<long long> > const&, QList<QBitArray> const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @staticmethod
  def cleanupHandleList(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
      QVector<HAnimationClip> *clips)': names
      'QVector<Qt3DAnimation::Animation::HAnimationClip>', which has no cute
      class yet.
    - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
      QVector<HClipAnimator> *animators)': names
      'QVector<Qt3DAnimation::Animation::HClipAnimator>', which has no cute
      class yet.
    - Qt's 'void Qt3DAnimation::Animation::Handler::cleanupHandleList(
      QVector<HBlendedClipAnimator> *animators)': names
      'QVector<Qt3DAnimation::Animation::HBlendedClipAnimator>', which has no
      cute class yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.cleanupHandleList' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HAnima"
        "tionClip> *clips)': names "
        "'QVector<Qt3DAnimation::Animation::HAnimationClip>', which has no "
        "cute class yet. Qt's 'void "
        "Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HClipA"
        "nimator> *animators)': names "
        "'QVector<Qt3DAnimation::Animation::HClipAnimator>', which has no "
        "cute class yet. Qt's 'void "
        "Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HBlend"
        "edClipAnimator> *animators)': names "
        "'QVector<Qt3DAnimation::Animation::HBlendedClipAnimator>', which "
        "has no cute class yet.")

  @staticmethod
  def jobsToExecute(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DAnimation::Animation::Handler::jobsToExecute(qint64 time)': leans on
    'Qt3DAnimation::Animation::prepareCallbacks(QList<Qt3DAnimation::
    Animation::MappingData> const&, QList<float> const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.jobsToExecute' has no cute "
        "function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DAnimation::Animation::Handler::jobsToExecute(qint64 time)': "
        "leans on "
        "'Qt3DAnimation::Animation::prepareCallbacks(QList<Qt3DAnimation::An"
        "imation::MappingData> const&, QList<float> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def runningBlenndedClipAnimators(*__, **_) -> Never:
    """
    Qt's 'QVector<HBlendedClipAnimator>
    Qt3DAnimation::Animation::Handler::runningBlenndedClipAnimators() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.runningBlenndedClipAnimators' has "
        "no cute function yet. Qt's 'QVector<HBlendedClipAnimator> "
        "Qt3DAnimation::Animation::Handler::runningBlenndedClipAnimators() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def runningClipAnimators(*__, **_) -> Never:
    """
    Qt's 'QVector<HClipAnimator>
    Qt3DAnimation::Animation::Handler::runningClipAnimators() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.runningClipAnimators' has no cute "
        "function yet. Qt's 'QVector<HClipAnimator> "
        "Qt3DAnimation::Animation::Handler::runningClipAnimators() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setBlendedClipAnimatorRunning(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::Handler::setBlendedClipAnimatorRunning(const
    HBlendedClipAnimator &handle, bool running)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.setBlendedClipAnimatorRunning' "
        "has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::Handler::setBlendedClipAnimatorRunning(co"
        "nst HBlendedClipAnimator &handle, bool running)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setClipAnimatorRunning(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::Handler::setClipAnimatorRunning(const
    HClipAnimator &handle, bool running)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.Handler.setClipAnimatorRunning' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::Handler::setClipAnimatorRunning(const "
        "HClipAnimator &handle, bool running)': takes a type Python has no "
        "way to hand over yet.")
