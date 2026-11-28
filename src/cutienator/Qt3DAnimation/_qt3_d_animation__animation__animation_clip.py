"""
Qt3DAnimation::Animation::AnimationClip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationclip_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::AnimationClip to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AnimationClip(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::AnimationClip: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::AnimationClip.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::AnimationClip is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::AnimationClip that has a
  ritual and that Python can call so far, 18 names in all: 'cleanup',
  'setSource', 'source', 'setStatus', 'status', 'syncFromFrontEnd',
  'addDependingClipAnimator', 'addDependingBlendedClipAnimator', 'name',
  'setDuration', 'duration', 'channelIndex', 'channelCount',
  'channelComponentBaseIndex', 'loadAnimationFromData', 'clearData',
  'findDuration', 'findChannelComponentCount'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QVector<Channel>
    &Qt3DAnimation::Animation::AnimationClip::channels() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::AnimationClip is created at the first
    use, not by 'Qt3DAnimation::Animation::AnimationClip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::AnimationClip.
  - Each name of Qt's Qt3DAnimation::Animation::AnimationClip that has no
    cute function yet, 'channels', 'loadAnimation', 'loadAnimationFromUrl',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::AnimationClip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DAnimation::Animation::AnimationClip::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DAnimation::Animation::AnimationClip::source() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Qt3DAnimation.QAnimationClipLoader.Status:
    """
    Calls Qt's 'QAnimationClipLoader::Status
    Qt3DAnimation::Animation::AnimationClip::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html#status

    Returns
    -------

    Qt3DAnimation.QAnimationClipLoader.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DAnimation.QAnimationClipLoader.Status(number)' gives.
    """
    #  QAnimationClipLoader::Status
    #      Qt3DAnimation::Animation::AnimationClip::status() const
    return Qt3DAnimation.QAnimationClipLoader.Status(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6statusEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::Animation::AnimationClip::name()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::Animation::AnimationClip::name() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip4nameEv',
    )

  def duration(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::Animation::AnimationClip::duration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  float Qt3DAnimation::Animation::AnimationClip::duration() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip8durationEv',
    )

  @overload(str, int)
  def channelIndex(self, channelName: str, jointIndex: int) -> int:
    """
    Calls Qt's 'qsizetype
    Qt3DAnimation::Animation::AnimationClip::channelIndex(const QString
    &channelName, qsizetype jointIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    channelName : str
      Passed on as it is: a QString is made of it for the call.

    jointIndex : int
      Passed on as it is.
    """
    #  qsizetype Qt3DAnimation::Animation::AnimationClip::channelIndex(const
    #      QString &channelName, qsizetype jointIndex) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip12channelIndexER'
        'K7QStringx',
        channelName, jointIndex,
    )

  def channelCount(self) -> int:
    """
    Calls Qt's 'qsizetype
    Qt3DAnimation::Animation::AnimationClip::channelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  qsizetype Qt3DAnimation::Animation::AnimationClip::channelCount()
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip12channelCountEv',
    )

  @overload(int)
  def channelComponentBaseIndex(self, channelGroupIndex: int) -> int:
    """
    Calls Qt's 'qsizetype
    Qt3DAnimation::Animation::AnimationClip::channelComponentBaseIndex(
    qsizetype channelGroupIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    channelGroupIndex : int
      Passed on as it is.
    """
    #  qsizetype Qt3DAnimation::Animation::AnimationClip::
    #      channelComponentBaseIndex(qsizetype channelGroupIndex) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13AnimationClip25channelCompone'
        'ntBaseIndexEx',
        channelGroupIndex,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::AnimationClip::setSource(const
    QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::AnimationClip::setSource(const QUrl
    #      &source)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip9setSourceERK4QUr'
        'l',
        self._valueOf(source),
    )

  @overload(Qt3DAnimation.QAnimationClipLoader.Status)
  def setStatus(
      self,
      status: Qt3DAnimation.QAnimationClipLoader.Status,
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::AnimationClip::setStatus(
    QAnimationClipLoader::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    status : Qt3DAnimation.QAnimationClipLoader.Status
      Passed on as its number.
    """
    #  void Qt3DAnimation::Animation::AnimationClip::setStatus(
    #      QAnimationClipLoader::Status status)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip9setStatusENS_20Q'
        'AnimationClipLoader6StatusE',
        status.value,
    )

  @overload(float)
  def setDuration(self, duration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::setDuration(float duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::AnimationClip::setDuration(float
    #      duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip11setDurationEf',
        duration,
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
    Notes what was given, for Qt's
    'Qt3DAnimation::Animation::AnimationClip::AnimationClip()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  Qt3DAnimation::Animation::AnimationClip::AnimationClip()
    self._noteCreation(AnimationClip, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClipC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::AnimationClip::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html#cleanup
    """
    #  void Qt3DAnimation::Animation::AnimationClip::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::AnimationClip::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip16syncFromFrontEn'
        'dEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation13AnimationClip16syncFromF'
          'rontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addDependingClipAnimator(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::addDependingClipAnimator(const
    Qt3DCore::QNodeId &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void
    #      Qt3DAnimation::Animation::AnimationClip::addDependingClipAnimator(
    #      const Qt3DCore::QNodeId &id)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip24addDependingCli'
        'pAnimatorERKN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addDependingBlendedClipAnimator(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::addDependingBlendedClipAnimator(
    const Qt3DCore::QNodeId &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::AnimationClip::
    #      addDependingBlendedClipAnimator(const Qt3DCore::QNodeId &id)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip31addDependingBle'
        'ndedClipAnimatorERKN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  def loadAnimationFromData(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::loadAnimationFromData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  void Qt3DAnimation::Animation::AnimationClip::loadAnimationFromData()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip21loadAnimationFr'
        'omDataEv',
    )

  def clearData(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::AnimationClip::clearData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  void Qt3DAnimation::Animation::AnimationClip::clearData()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip9clearDataEv',
    )

  def findDuration(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::AnimationClip::findDuration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  float Qt3DAnimation::Animation::AnimationClip::findDuration()
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip12findDurationEv',
    )

  def findChannelComponentCount(self) -> int:
    """
    Calls Qt's 'qsizetype
    Qt3DAnimation::Animation::AnimationClip::findChannelComponentCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-animationclip.html
    """
    #  qsizetype Qt3DAnimation::Animation::AnimationClip::
    #      findChannelComponentCount()
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13AnimationClip25findChannelComp'
        'onentCountEv',
    )

  @staticmethod
  def channels(*__, **_) -> Never:
    """
    Qt's 'const QVector<Channel>
    &Qt3DAnimation::Animation::AnimationClip::channels() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.AnimationClip.channels' has no cute "
        "function yet. Qt's 'const QVector<Channel> "
        "&Qt3DAnimation::Animation::AnimationClip::channels() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def loadAnimation(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::AnimationClip::loadAnimation()':
    leans on
    'Qt3DAnimation::Animation::AnimationClip::loadAnimationFromUrl()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.AnimationClip.loadAnimation' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::Animation::AnimationClip::loadAnimation()': leans "
        "on "
        "'Qt3DAnimation::Animation::AnimationClip::loadAnimationFromUrl()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def loadAnimationFromUrl(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::AnimationClip::loadAnimationFromUrl()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'ANIMATION_INDEX_KEY'.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.AnimationClip.loadAnimationFromUrl' has "
        "no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::AnimationClip::loadAnimationFromUrl()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'ANIMATION_INDEX_KEY'.")
