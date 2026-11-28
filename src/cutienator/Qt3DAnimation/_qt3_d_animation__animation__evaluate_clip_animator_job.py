"""
Qt3DAnimation::Animation::EvaluateClipAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/evaluateclipanimatorjob_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::EvaluateClipAnimatorJob to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class EvaluateClipAnimatorJob(Qt3DAnimation.Animation.AbstractEvaluateClipAnimatorJob):
  """
  The cute side of Qt's Qt3DAnimation::Animation::EvaluateClipAnimatorJob: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Animation::EvaluateClipAnimatorJob.

  It is built on the cute
  'Qt3DAnimation::Animation::AbstractEvaluateClipAnimatorJob', as Qt's
  Qt3DAnimation::Animation::EvaluateClipAnimatorJob is built on Qt's
  Qt3DAnimation::Animation::AbstractEvaluateClipAnimatorJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::EvaluateClipAnimatorJob
  that has a ritual and that Python can call so far, 4 names in all:
  'setHandler', 'handler', 'clearClipAnimator', 'run'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setClipAnimator(const
    HClipAnimator &clipAnimatorHandle)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'Qt3DAnimation.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::EvaluateClipAnimatorJob is created at
    the first use, not by
    'Qt3DAnimation::Animation::EvaluateClipAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob.
  - Each name of Qt's Qt3DAnimation::Animation::EvaluateClipAnimatorJob that
    has no cute function yet, '__init__', 'setClipAnimator', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::EvaluateClipAnimatorJob'

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
    *Qt3DAnimation::Animation::EvaluateClipAnimatorJob::handler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-evaluateclipanimatorjob.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.Handler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Handler *Qt3DAnimation::Animation::EvaluateClipAnimatorJob::handler()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation23EvaluateClipAnimatorJob7handl'
        'erEv',
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
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setHandler(Handler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-evaluateclipanimatorjob.html

    Parameters
    ----------

    handler : Optional[Qt3DAnimation.Animation.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setHandler(
    #      Handler *handler)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob10setHa'
        'ndlerEPNS0_7HandlerE',
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
    Qt's 'Qt3DAnimation::Animation::EvaluateClipAnimatorJob::
    EvaluateClipAnimatorJob()': leans on
    'Qt3DAnimation::Animation::prepareCallbacks(QList<Qt3DAnimation::
    Animation::MappingData> const&, QList<float> const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.EvaluateClipAnimatorJob.__init__' has no "
        "cute function yet. Qt's "
        "'Qt3DAnimation::Animation::EvaluateClipAnimatorJob::EvaluateClipAni"
        "matorJob()': leans on "
        "'Qt3DAnimation::Animation::prepareCallbacks(QList<Qt3DAnimation::An"
        "imation::MappingData> const&, QList<float> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def clearClipAnimator(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob::clearClipAnimator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-evaluateclipanimatorjob.html
    """
    #  void Qt3DAnimation::Animation::EvaluateClipAnimatorJob::
    #      clearClipAnimator()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob17clear'
        'ClipAnimatorEv',
    )

  def run(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-evaluateclipanimatorjob.html
    """
    #  void Qt3DAnimation::Animation::EvaluateClipAnimatorJob::run()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob3runEv',
    )

  @staticmethod
  def setClipAnimator(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setClipAnimator(const
    HClipAnimator &clipAnimatorHandle)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.EvaluateClipAnimatorJob.setClipAnimator' "
        "has no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setClipAnimator("
        "const HClipAnimator &clipAnimatorHandle)': takes a type Python has "
        "no way to hand over yet.")
