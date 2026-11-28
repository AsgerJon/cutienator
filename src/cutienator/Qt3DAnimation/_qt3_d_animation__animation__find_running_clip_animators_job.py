"""
Qt3DAnimation::Animation::FindRunningClipAnimatorsJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/findrunningclipanimatorsjob_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::FindRunningClipAnimatorsJob to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FindRunningClipAnimatorsJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's
  Qt3DAnimation::Animation::FindRunningClipAnimatorsJob: a plain Python
  object standing in front of one C++
  Qt3DAnimation::Animation::FindRunningClipAnimatorsJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DAnimation::Animation::FindRunningClipAnimatorsJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's
  Qt3DAnimation::Animation::FindRunningClipAnimatorsJob that has a ritual and
  that Python can call so far, 3 names in all: 'setHandler', 'handler',
  'run'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::
    setDirtyClipAnimators(const QVector<HClipAnimator>
    &animationClipHandles)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::FindRunningClipAnimatorsJob is created
    at the first use, not by
    'Qt3DAnimation::Animation::FindRunningClipAnimatorsJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob.
  - Each name of Qt's Qt3DAnimation::Animation::FindRunningClipAnimatorsJob
    that has no cute function yet, '__init__', 'setDirtyClipAnimators', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::FindRunningClipAnimatorsJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def handler(self) -> Optional[Qt3DAnimation.Animation.Handler]:
    """
    Calls Qt's 'Handler
    *Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::handler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-findrunningclipanimatorsjob.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.Handler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Handler
    #      *Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::handler()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob7h'
        'andlerEv',
    )
    return Qt3DAnimation.Animation.Handler._cuteAt(address)

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
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::setHandler(Handler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-findrunningclipanimatorsjob.html

    Parameters
    ----------

    handler : Optional[Qt3DAnimation.Animation.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::setHandler(
    #      Handler *handler)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob10s'
        'etHandlerEPNS0_7HandlerE',
        self._addressOf(handler),
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
    Qt's 'Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::
    FindRunningClipAnimatorsJob()': leans on
    'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimation::
    Animation::ChannelMapping*> const&,
    QList<Qt3DAnimation::Animation::ChannelNameAndType> const&,
    QList<QList<long long> > const&, QList<QBitArray> const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.FindRunningClipAnimatorsJob.__init__' has "
        "no cute function yet. Qt's "
        "'Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::FindRunning"
        "ClipAnimatorsJob()': leans on "
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

  def run(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-findrunningclipanimatorsjob.html
    """
    #  void Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::run()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob3ru'
        'nEv',
    )

  @staticmethod
  def setDirtyClipAnimators(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::
    setDirtyClipAnimators(const QVector<HClipAnimator>
    &animationClipHandles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.FindRunningClipAnimatorsJob.setDirtyClipAn"
        "imators' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::setDirtyClip"
        "Animators(const QVector<HClipAnimator> &animationClipHandles)': "
        "takes a type Python has no way to hand over yet.")
