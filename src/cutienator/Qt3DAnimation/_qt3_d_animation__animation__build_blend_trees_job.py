"""
Qt3DAnimation::Animation::BuildBlendTreesJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/buildblendtreesjob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::BuildBlendTreesJob to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
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


class BuildBlendTreesJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DAnimation::Animation::BuildBlendTreesJob: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::BuildBlendTreesJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DAnimation::Animation::BuildBlendTreesJob is built on Qt's
  Qt3DCore::QAspectJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::BuildBlendTreesJob that
  has a ritual and that Python can call so far, 3 names in all: 'setHandler',
  'handler', 'run'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DAnimation::Animation::BuildBlendTreesJob::setBlendedClipAnimators(
    const QVector<HBlendedClipAnimator> &blendedClipAnimatorHandles)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::BuildBlendTreesJob is created at the
    first use, not by 'Qt3DAnimation::Animation::BuildBlendTreesJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::Animation::BuildBlendTreesJob.
  - Each name of Qt's Qt3DAnimation::Animation::BuildBlendTreesJob that has
    no cute function yet, '__init__', 'setBlendedClipAnimators', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::BuildBlendTreesJob'

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
    *Qt3DAnimation::Animation::BuildBlendTreesJob::handler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-buildblendtreesjob.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.Handler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Handler *Qt3DAnimation::Animation::BuildBlendTreesJob::handler() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation18BuildBlendTreesJob7handlerEv',
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
    Qt3DAnimation::Animation::BuildBlendTreesJob::setHandler(Handler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-buildblendtreesjob.html

    Parameters
    ----------

    handler : Optional[Qt3DAnimation.Animation.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::BuildBlendTreesJob::setHandler(Handler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob10setHandler'
        'EPNS0_7HandlerE',
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
    Qt's
    'Qt3DAnimation::Animation::BuildBlendTreesJob::BuildBlendTreesJob()':
    leans on
    'Qt3DAnimation::Animation::buildPropertyMappings(QList<Qt3DAnimation::
    Animation::ChannelMapping*> const&,
    QList<Qt3DAnimation::Animation::ChannelNameAndType> const&,
    QList<QList<long long> > const&, QList<QBitArray> const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BuildBlendTreesJob.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::Animation::BuildBlendTreesJob::BuildBlendTreesJob()"
        "': leans on "
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
    Calls Qt's 'void Qt3DAnimation::Animation::BuildBlendTreesJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-buildblendtreesjob.html
    """
    #  void Qt3DAnimation::Animation::BuildBlendTreesJob::run()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob3runEv',
    )

  @staticmethod
  def setBlendedClipAnimators(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::BuildBlendTreesJob::setBlendedClipAnimators(
    const QVector<HBlendedClipAnimator> &blendedClipAnimatorHandles)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BuildBlendTreesJob.setBlendedClipAnimators"
        "' has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::BuildBlendTreesJob::setBlendedClipAnimato"
        "rs(const QVector<HBlendedClipAnimator> "
        "&blendedClipAnimatorHandles)': takes a type Python has no way to "
        "hand over yet.")
